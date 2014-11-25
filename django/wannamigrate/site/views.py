from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.utils.translation import ugettext as _
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.forms.models import inlineformset_factory
from django.db import transaction
from django.utils.translation import activate
from django.contrib.auth import get_user_model
from django.conf import settings
import math
from wannamigrate.core.immigration_calculator import ImmigrationCalculator
from wannamigrate.core.util import get_object_or_false, get_list_or_false, get_country_points_css_class, get_user_progress_css_class
from wannamigrate.site.forms import (
    UserForm, ContactForm, LoginForm, SignupForm, PasswordRecoveryForm, PasswordResetForm,
    UserPersonalForm, UserPersonalFamilyForm, BaseUserPersonalFamilyFormSet,
    UserLanguageForm, UserLanguageProficiencyForm, BaseUserLanguageProficiencyFormSet,
    UserEducationForm, UserEducationHistoryForm, UserWorkForm, UserWorkExperienceForm,
    UserWorkOfferForm, BaseUserWorkOfferFormSet
)
from wannamigrate.core.models import (
    User, UserPersonalFamily, UserPersonal, UserEducation, UserEducationHistory,
    UserLanguage, UserLanguageProficiency, UserWork, UserWorkExperience, UserWorkOffer,
    Country, UserResult, UserStats
)
from wannamigrate.core.mailer import Mailer
from django.utils import translation

#######################
# HOME-PAGE VIEWS
#######################
def home( request ):
    """
    Home-Page - Used as a provocative landing page to conquer new users

    :param request:
    :return String - The contact page rendered:
    """

    # Initialize template data dictionary
    template_data = {}

    # Instantiate Forms
    template_data['login_form'] = LoginForm()
    template_data['signup_form'] = SignupForm()
    template_data['recovery_form'] = PasswordRecoveryForm()


    # Print Template
    return render( request, 'site/home.html', template_data )


def home_older_browsers( request ):
    """
    Home-Page - Used as a provocative landing page to conquer new users
    (for browsers that doesn't support css3)

    :param request:
    :return String - The home page rendered:
    """

    # Initialize template data dictionary
    template_data = {}

    # Instantiate Forms
    template_data['login_form'] = LoginForm()
    template_data['signup_form'] = SignupForm()
    template_data['recovery_form'] = PasswordRecoveryForm()


    # Print Template
    return render( request, 'site/home_older_browsers.html', template_data )


#######################
# LOGIN and SIGNUP VIEWS
#######################
def login( request ):
    """
    Ajax action to execute user login

    :param request:
    :return String - The html page rendered:
    """

    # Only accepts AJAX Call
    if request.is_ajax() and request.method == 'POST':

        # Create form
        form = LoginForm( request.POST )

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate( email = email, password = password )

            if user is not None and user.is_active:

                # Login Successfully
                auth_login( request, user )

                # Return success to Ajax
                return HttpResponse( 'OK' )

            else:
                return HttpResponse( _( 'Invalid Login. Please try again.' ) ) # invalid login :(

        else:
            return HttpResponse( _( 'Invalid Login. Please try again.' ) ) # invalid login :(

    else:
        raise Http404


def logout( request ):
    """
    Process Logout

    :param request:
    :return HTTP Redirection:
    """

    # Executes auth Logout
    auth_logout( request )

    # Redirect to home-page
    return HttpResponseRedirect( reverse( "site:home" ) )


def signup( request ):
    """
    Ajax action to create new user

    :param request:
    :return String - The html page rendered:
    """

    # Only accepts AJAX Call
    if request.is_ajax() and request.method == 'POST':

        # Create form
        form = SignupForm( request.POST )

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create user
            user = get_user_model().objects.create_user( email, name = '', password = password )

            if user is not None:

                # Login user
                user = authenticate( email = email, password = password )
                auth_login( request, user )

                # Sends Welcome Email to User
                # TODO Change this to a celery/signal background task
                Mailer.send_welcome_email( user )

                # Return success to Ajax
                return HttpResponse( 'OK' )

            else:
                return HttpResponse( _( 'There was an error while creating your user account.' ) ) # user creation failed

        else:

            if form.non_field_errors:
                msg = ''
                for k, v in form.errors.items():
                    msg += v + '<br />'
                return HttpResponse( msg )

            return HttpResponse( _( 'Invalid Information!<br />Make sure all fields are filled in and email and confirmation match.' ) ) # user creation failed

    else:
        raise Http404


def recover_password( request ):
    """
    Ajax action to send link to redefine password

    :param request:
    :return String - The html page rendered:
    """

    # Only accepts AJAX Call
    if request.is_ajax() and request.method == 'POST':

        # Create form
        form = PasswordRecoveryForm( request.POST )

        if form.is_valid():

            email = form.cleaned_data['email']
            user = get_object_or_false( get_user_model(), email = email )

            if user is not None and user.is_active:

                # Send email with link to reset password
                # TODO: Change this to a celery background event and use a try/exception block
                Mailer.send_reset_password_email( user )

                # Return success to Ajax
                return HttpResponse( 'EMAIL_SENT' )

            else:
                return HttpResponse( _( 'No user found with this e-mail address.' ) )

        else:
            return HttpResponse( _( 'Invalid e-mail address.' ) )

    else:
        raise Http404


@sensitive_post_parameters()
@never_cache
def reset_password( request, uidb64 = None, token = None ):
    """
    Page to set a new password after clicking on a link from email sent by 'recover password feature'

    :param request:
    :param uidb64:
    :param token:
    :return String - The html page rendered:
    """

    # Try to find user by the uid given
    uid = urlsafe_base64_decode( uidb64 )
    user = get_object_or_404( get_user_model(), pk = uid )

    # Check if token is valid
    token_generator = PasswordResetTokenGenerator()
    if user is None or not token_generator.check_token( user, token ):
        raise Http404

    # Initialize template data dictionary
    template_data = { 'finished': False }

    # Create form
    form = PasswordResetForm( request.POST or None )

    # If form was submitted, it tries to validate and save new password
    if form.is_valid():

        # Saves New password for user
        user.set_password( form.cleaned_data['password'] )
        user.save()

        # mark in the template that it was successfully finished
        template_data['finished'] = True

    # Pass form to template
    template_data['form'] = form

    # Print Template
    return render( request, 'site/reset_password.html', template_data )



#######################
# CONTACT US VIEWS
#######################
def contact( request ):
    """
    Displays the contact page with a form to send us a message by email.

    :param request:
    :return String - The contact page rendered:
    """

    # Initialize template data dictionary
    template_data = { 'finished': False }

    # Create form
    form = ContactForm( request.POST or None )

    # If the form has been submitted...
    if form.is_valid():

        email = form.cleaned_data[ 'email' ]
        name = form.cleaned_data[ 'name' ]
        message = form.cleaned_data[ 'message' ]

        # Send Email with message
        # TODO: Change this to a celery background event and use a try/exception block
        send_result = Mailer.send_contact_email( email, name, message )
        template_data['finished'] = True

    # pass form to template
    template_data['form'] = form

    # Print Template
    return render( request, 'site/contact.html', template_data )


#######################
# TOUR VIEWS
#######################
def tour( request ):
    """
    Displays "how It Works" static page

    :param request:
    :return String - HTML from The dashboard page.
    """

    # Print Template
    return render( request, 'site/tour.html' )



#######################
# MY ACCOUNT VIEWS
#######################
@login_required
def account( request ):
    """
    Displays "My Account" page

    :param request:
    :return String - HTML from The dashboard page.
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in user_form.cleaned_data as required
            # TODO: save the provided data.
            # TODO: Remember to ignore e-mail edition.
            # Render the account page with a success message.
            return render( request, 'site/account.html', { 'user_form': user_form, 'success': "Changes saved." } )

    # if a GET (or any other method) we'll create a form
    # filled with user's information.
    # fields: name, e-mail, preferred language and avatar.
    # TODO: fill the user_form with the user's info.
    else:
        user_form = UserForm()

    return render( request, 'site/account.html', { 'user_form': user_form } )



#######################
# DASHBOARD VIEWS
#######################
@login_required
def dashboard( request ):
    """
    Process the dashboard page.

    The dashboard is the main screen of the system,
    where the users can view its informations, progress, etc.

    :param request:
    :return String - HTML from The dashboard page.
    """

    # If User edited data, but did not calculate points by clicking in save and exit
    try:
        user_stats = UserStats.objects.get( user = request.user )
    except UserStats.DoesNotExist:
        user_stats = False
    if user_stats and user_stats.updating_now:
        return HttpResponseRedirect( reverse( "site:calculate_points" ) )

    # Initial settings
    template_data = {}
    template_data['au_min_points'] = settings.MINIMUM_POINTS_AUSTRALIA
    template_data['ca_min_points'] = settings.MINIMUM_POINTS_CANADA
    template_data['nz_min_points'] = settings.MINIMUM_POINTS_NEW_ZEALAND
    template_data['au_points'] = 0
    template_data['ca_points'] = 0
    template_data['nz_points'] = 0
    template_data['personal_percentage'] = 0
    template_data['language_percentage'] = 0
    template_data['education_percentage'] = 0
    template_data['work_percentage'] = 0

    # Get User Results per country
    try:
        user_result = UserResult.objects.filter( user = request.user )
    except UserResult.DoesNotExist:
        user_result = False

    # Pass total points per country to template
    if user_result:
        for item in user_result:
            if item.country.id == settings.ID_COUNTRY_AUSTRALIA:
                template_data['au_points'] = item.score_total
            elif item.country.id == settings.ID_COUNTRY_CANADA:
                template_data['ca_points'] = item.score_total
            elif item.country.id == settings.ID_COUNTRY_NEW_ZEALAND:
                template_data['nz_points'] = item.score_total

    # Define the percentage CSS class to use around country flags for progress bar
    au_percentage = math.floor( ( 100 * template_data['au_points'] ) / template_data['au_min_points'] )
    ca_percentage = math.floor( ( 100 * template_data['ca_points'] ) / template_data['ca_min_points'] )
    nz_percentage = math.floor( ( 100 * template_data['nz_points'] ) / template_data['nz_min_points'] )
    template_data['au_percentage_css_class'] = get_country_points_css_class( au_percentage )
    template_data['ca_percentage_css_class'] = get_country_points_css_class( ca_percentage )
    template_data['nz_percentage_css_class'] = get_country_points_css_class( nz_percentage )

    # pass user registration percentages to template
    if user_stats:
        template_data['personal_percentage'] = user_stats.percentage_personal
        template_data['language_percentage'] = user_stats.percentage_language
        template_data['education_percentage'] = user_stats.percentage_education
        template_data['work_percentage'] = user_stats.percentage_work

    # Define the percentage css class for progress bar on forms (personal, language, education and work)
    template_data['personal_percentage_css_class'] = get_user_progress_css_class( template_data['personal_percentage'] )
    template_data['language_percentage_css_class'] = get_user_progress_css_class( template_data['language_percentage'] )
    template_data['education_percentage_css_class'] = get_user_progress_css_class( template_data['education_percentage'] )
    template_data['work_percentage_css_class'] = get_user_progress_css_class( template_data['work_percentage'] )

    # Print Template
    return render( request, 'site/dashboard.html', template_data )



#######################
# EDIT USER INFORMATION VIEWS
#######################
@login_required
def edit_personal( request ):
    """
    Form to edit PERSONAL user data

    :param request:
    :return String - HTML.
    """

    # Initial Settings
    template_data = {}

    # Set top bar css class to be fixed on top
    template_data['top_bar_css_class'] = "fixTopBar"

    # Identify UserPersonal object (if it exists)
    try:
        user_personal = request.user.userpersonal
    except UserPersonal.DoesNotExist:
        user_personal = False

    # Instantiate UserPersonal Form
    if user_personal:
        user_personal_form = UserPersonalForm( request.POST or None, instance = user_personal )
    else:
        user_personal_form = UserPersonalForm( request.POST or None, user = request.user )

    # Instantiate UserPersonalFamily Formset
    UserPersonalFamilyInlineFormset = inlineformset_factory( User, UserPersonalFamily, form = UserPersonalFamilyForm, formset = BaseUserPersonalFamilyFormSet, extra = 0, can_delete = True, validate_min = True, min_num = 1 )
    user_personal_family_formset = UserPersonalFamilyInlineFormset( request.POST or None, instance = request.user )

    # Form was submitted so it tries to validate and save data
    if user_personal_form.is_valid():

        # Start a DB Transaction, so if there are any errors in answers/points, question is not saved
        with transaction.atomic():

            # Saves UserPersonal
            user_personal = user_personal_form.save()

            # Saves UserPersonalFamily Formset
            success = False
            if not user_personal.family_overseas:
                UserPersonalFamily.objects.filter( user = request.user ).delete()
                success = True

            else:
                if user_personal_family_formset.is_valid():
                    instances = user_personal_family_formset.save()
                    success = True

                else:
                    transaction.set_rollback( True )

            # If success, update stats and redirect
            if success:
                UserStats.objects.update_or_create(
                    user = request.user, defaults = {
                        'percentage_personal': user_personal.get_completed_percentage(),
                        'updating_now': True
                    }
                )
                return HttpResponseRedirect( request.POST.get( 'next' ) )

    # pass the forms to the template
    template_data['user_personal_form'] = user_personal_form
    template_data['user_personal_family_formset'] = user_personal_family_formset

    # Print Template
    return render( request, 'site/edit_personal.html', template_data )


@login_required
def edit_language( request ):
    """
    Form to edit LANGUAGE data from the user

    :param request:
    :return String - HTML.
    """

    # Initial Settings
    template_data = {}

    # Set top bar css class to be fixed on top
    template_data['top_bar_css_class'] = "fixTopBar"

    # Identify UserPersonal object (if it exists)
    try:
        user_language = request.user.userlanguage
    except UserLanguage.DoesNotExist:
        user_language = False

    # Instantiate UserPersonal Form
    if user_language:
        user_language_form = UserLanguageForm( request.POST or None, instance = user_language )
    else:
        user_language_form = UserLanguageForm( request.POST or None, user = request.user )

    # search for language proficiency
    try:
        count = request.user.userlanguageproficiency_set.count()
        user_language_proficiency_exists = True if count > 0 else False
    except UserWorkExperience.DoesNotExist:
        user_language_proficiency_exists = False

    # count if is there any languages added
    if user_language_proficiency_exists:
        extra = 0
    else:
        extra = 1

    # Instantiate UserLanguageProficiency Formset
    UserLanguageProficiencyInlineFormset = inlineformset_factory( User, UserLanguageProficiency, form = UserLanguageProficiencyForm, formset = BaseUserLanguageProficiencyFormSet, extra = extra, can_delete = True )
    user_language_proficiency_formset = UserLanguageProficiencyInlineFormset( request.POST or None, instance = request.user )

    # Form was submitted so it tries to validate and save data
    if user_language_form.is_valid():

        # Start a DB Transaction, so if there are any errors in answers/points, question is not saved
        with transaction.atomic():

            # Saves UserLanguage
            user_language = user_language_form.save()

            # Saves UserLanguageProficiency Formset
            success = False
            if user_language_proficiency_formset.is_valid():
                instances = user_language_proficiency_formset.save()
                success = True
            else:
                transaction.set_rollback( True )

            # If success, update stats and redirect
            if success:
                UserStats.objects.update_or_create(
                    user = request.user, defaults = {
                        'percentage_language': user_language.get_completed_percentage(),
                        'updating_now': True
                    }
                )
                return HttpResponseRedirect( request.POST.get( 'next' ) )

    # pass the forms to the template
    template_data['user_language_form'] = user_language_form
    template_data['user_language_proficiency_formset'] = user_language_proficiency_formset

    # Print Template
    return render( request, 'site/edit_language.html', template_data )


@login_required
def edit_education( request ):
    """
    Form to edit LANGUAGE data from the user

    :param request:
    :return String - HTML.
    """

    # Initial Settings
    template_data = {}

    # Set top bar css class to be fixed on top
    template_data['top_bar_css_class'] = "fixTopBar"

    # Identify UserEducation object (if it exists)
    try:
        user_education = request.user.usereducation
    except UserEducation.DoesNotExist:
        user_education = False

    # Instantiate UserEducationForm
    if user_education:
        user_education_form = UserEducationForm( request.POST or None, instance = user_education )
    else:
        user_education_form = UserEducationForm( request.POST or None, user = request.user )

    # search for education history
    try:
        count = request.user.usereducationhistory_set.count()
        user_education_history_exists = True if count > 0 else False
    except UserWorkExperience.DoesNotExist:
        user_education_history_exists = False

    # count if is there any education degrees added
    if user_education_history_exists:
        extra = 0
    else:
        extra = 1

    # Instantiate UserEducationHistory Formset
    UserEducationHistoryInlineFormset = inlineformset_factory( User, UserEducationHistory, form = UserEducationHistoryForm, extra = extra, can_delete = True )
    user_education_history_formset = UserEducationHistoryInlineFormset( request.POST or None, instance = request.user )

    # Form was submitted so it tries to validate and save data
    if user_education_form.is_valid():

        # Start a DB Transaction, so if there are any errors in answers/points, question is not saved
        with transaction.atomic():

            # Saves UserEducation
            user_education = user_education_form.save()

            # Saves UserEducationHistory Formset
            success = False
            if user_education_history_formset.is_valid():
                instances = user_education_history_formset.save()
                success = True
            else:
                transaction.set_rollback( True )

            # If success, update stats and redirect
            if success:
                UserStats.objects.update_or_create(
                    user = request.user, defaults = {
                        'percentage_education': user_education.get_completed_percentage(),
                        'updating_now': True
                    }
                )
                return HttpResponseRedirect( request.POST.get( 'next' ) )

    # pass the forms to the template
    template_data['user_education_form'] = user_education_form
    template_data['user_education_history_formset'] = user_education_history_formset

    # Print Template
    return render( request, 'site/edit_education.html', template_data )


@login_required
def edit_work( request ):
    """
    Form to edit WORK data from the user

    :param request:
    :return String - HTML.
    """

    # Initial Settings
    template_data = {}

    # Set top bar css class to be fixed on top
    template_data['top_bar_css_class'] = "fixTopBar"

    # Identify UserWork object (if it exists)
    try:
        user_work = request.user.userwork
    except UserWork.DoesNotExist:
        user_work = False

    # Instantiate UserWorkForm
    if user_work:
        user_work_form = UserWorkForm( request.POST or None, instance = user_work )
    else:
        user_work_form = UserWorkForm( request.POST or None, user = request.user )

    # search for education history
    try:
        count = request.user.userworkexperience_set.count()
        user_work_experience_exists = True if count > 0 else False
    except UserWorkExperience.DoesNotExist:
        user_work_experience_exists = False

    # count if is there any work experiences added
    if user_work_experience_exists:
        extra_work_experience = 0
    else:
        extra_work_experience = 1

    # Instantiate UserWorkExperience Formset
    UserWorkExperienceInlineFormset = inlineformset_factory( User, UserWorkExperience, form = UserWorkExperienceForm, extra = extra_work_experience, can_delete = True )
    user_work_experience_formset = UserWorkExperienceInlineFormset( request.POST or None, instance = request.user )

    # Instantiate UserWorkOffer Formset
    UserWorkOfferInlineFormset = inlineformset_factory(
        User, UserWorkOffer, form = UserWorkOfferForm, formset = BaseUserWorkOfferFormSet,
        extra = 0, can_delete = True, validate_min = True, min_num = 1
    )
    user_work_offer_formset = UserWorkOfferInlineFormset( request.POST or None, instance = request.user  )
    
    # Form was submitted so it tries to validate and save data
    if user_work_form.is_valid():

        # Start a DB Transaction, so if there are any errors in answers/points, question is not saved
        with transaction.atomic():

            # Saves UserWork
            user_work = user_work_form.save()

            # Saves UserWorkExperience Formset
            success = False
            if user_work_experience_formset.is_valid():
                user_work_experience_formset.save()

                # Saves UserWorkOffer Formset
                if not user_work.work_offer:
                    UserWorkOffer.objects.filter( user = request.user ).delete()
                    success = True
                else:
                    if user_work_offer_formset.is_valid():
                        user_work_offer_formset.save()
                        success = True
                    else:
                        transaction.set_rollback( True )

            else:
                transaction.set_rollback( True )

            # If success, update stats and redirect
            if success:
                UserStats.objects.update_or_create(
                    user = request.user, defaults = {
                        'percentage_work': user_work.get_completed_percentage(),
                        'updating_now': True
                    }
                )
                return HttpResponseRedirect( request.POST.get( 'next' ) )



    # pass the forms to the template
    template_data['user_work_form'] = user_work_form
    template_data['user_work_experience_formset'] = user_work_experience_formset
    template_data['user_work_offer_formset'] = user_work_offer_formset

    # Print Template
    return render( request, 'site/edit_work.html', template_data )


#######################
# CALCULATE POINTS VIEWS
#######################
@login_required
def calculate_points( request ):
    """
    Heart of the system.
    It process all user data and calculate his points to all countries with
    immigration support enabled

    :param request:
    :return Redirect
    """

    # instantiate the calculator class
    immigration_calculator = ImmigrationCalculator( request.user )

    # First we get every country with immigration support enabled
    countries = Country.objects.filter( immigration_enabled = True )
    for country in countries:

        # calculate points for this country
        results = immigration_calculator.get_total_results( country )

        # save results for this country
        updated_values = {
            'score_total': results['total'],
            'score_personal': results['personal'],
            'score_language': results['language'],
            'score_education': results['education'],
            'score_work': results['work'],
        }
        UserResult.objects.update_or_create(
            user = request.user, country = country, defaults = updated_values
        )

    # Remove flag for 'updating_now'
    UserStats.objects.update_or_create(
        user = request.user, defaults = { 'updating_now': False }
    )

    # Redirect to Dashboard
    return HttpResponseRedirect( reverse( "site:dashboard" ) )


#######################
# MY SITUATION VIEWS
#######################
@login_required
def situation( request, country_name ):
    """
    My Situation

    :param request:
    :param country_name:
    :return String - HTML.
    """

    return HttpResponse( "My Situation " + country_name )


@login_required
def visa_application( request, country_name ):
    """
    Visa Application

    :param request:
    :param country_name:
    :return String - HTML.
    """

    return HttpResponse( "Visa Application " + country_name )


@login_required
def moving( request, country_name ):
    """
    Moving

    :param request:
    :param country_name:
    :return String - HTML.
    """

    return HttpResponse( "Moving to " + country_name )


#######################
# INTERNATIONALIZATION VIEWS
#######################
def setlang( request, language_code ):
    """
    Changes the current language to the desired language defined by language_code parameter.
    If you want to redirect the user to other page that isn't '/' provide a parameter named "next" in the GET request.

    :param request: Default request param.
    :param language_code: The code of the language to localize.
    :return Sets the desired language and redirects the user to '/' or to a next page defined via GET.
    """

    # Checks if next paramters is set.
    next = '/'
    if request.GET[ "next" ]:
        next = request.GET[ "next" ]


    translation.activate( language_code )
    request.session[translation.LANGUAGE_SESSION_KEY] = language_code

    return redirect( next )






"""
Points Views

These are the views that control logic flow for
the templates on points app
"""

##########################
# Imports
##########################
import math

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.forms.models import inlineformset_factory
from django.db import transaction
from django.conf import settings

from wannamigrate.points.immigration_calculator import ImmigrationCalculator
from wannamigrate.core.util import (
    get_dashboard_country_progress_css_color, get_dashboard_user_progress_css_color
)
from wannamigrate.points.forms import (
    UserPersonalForm, UserPersonalFamilyForm, BaseUserPersonalFamilyFormSet,
    UserLanguageForm, UserLanguageProficiencyForm, BaseUserLanguageProficiencyFormSet,
    UserEducationForm, UserEducationHistoryForm, UserWorkForm, UserWorkExperienceForm,
    UserWorkOfferForm, BaseUserWorkOfferFormSet
)
from wannamigrate.core.models import (
    User, UserPersonalFamily, UserPersonal, UserEducation, UserEducationHistory,
    UserLanguage, UserLanguageProficiency, UserWork, UserWorkExperience, UserWorkOffer,
    Country, UserStats
)
from wannamigrate.points.models import (
    UserResult, Occupation, UserResultStatus, CountryConfig
)






#######################
# DASHBOARD VIEWS
#######################
@login_required
def dashboard( request ):
    """
    Process the dashboard page.

    The dashboard is the main screen of the system,
    where the users can view its informations, progress, etc.

    :param: request
    :return String - HTML from The dashboard page.
    """

    # If User edited data, but did not calculate points by clicking in save and exit
    try:
        user_stats = UserStats.objects.get( user = request.user )
    except UserStats.DoesNotExist:
        user_stats = False
    if user_stats and user_stats.updating_now:
        return HttpResponseRedirect( reverse( "points:calculate_points" ) )

    # Instantiate all country_config
    country_config = CountryConfig.objects.all()
    country_config_data = {}
    for item in country_config:
        if item.country_id not in country_config_data:
            country_config_data[item.country_id] = {}
        country_config_data[item.country_id] = item

    # Initializes template data
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Immigration Calculator - Check your chances for Australia, Canada and New Zealand - Wanna Migrate' )
    template_data['meta_description'] = _( 'Check your chances of obtaining a permanent visa to move to Canada, Australia or New Zealand.' )

    # Initial Settings
    template_data['au_min_points'] = country_config_data[settings.ID_COUNTRY_AUSTRALIA].pass_mark_points
    template_data['ca_min_points'] = country_config_data[settings.ID_COUNTRY_CANADA].pass_mark_points
    template_data['nz_min_points'] = country_config_data[settings.ID_COUNTRY_NEW_ZEALAND].pass_mark_points
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
    template_data['au_percentage'] = math.floor( ( 100 * template_data['au_points'] ) / template_data['au_min_points'] )
    template_data['ca_percentage'] = math.floor( ( 100 * template_data['ca_points'] ) / template_data['ca_min_points'] )
    template_data['nz_percentage'] = math.floor( ( 100 * template_data['nz_points'] ) / template_data['nz_min_points'] )
    template_data['au_percentage_css_color'] = get_dashboard_country_progress_css_color( template_data['au_percentage'] )
    template_data['ca_percentage_css_color'] = get_dashboard_country_progress_css_color( template_data['ca_percentage'] )
    template_data['nz_percentage_css_color'] = get_dashboard_country_progress_css_color( template_data['nz_percentage'] )

    # pass user registration percentages to template
    if user_stats:
        template_data['personal_percentage'] = user_stats.percentage_personal
        template_data['language_percentage'] = user_stats.percentage_language
        template_data['education_percentage'] = user_stats.percentage_education
        template_data['work_percentage'] = user_stats.percentage_work

    # Define the percentage css class for progress bar on forms (personal, language, education and work)
    template_data['personal_percentage_css_color'] = get_dashboard_user_progress_css_color( template_data['personal_percentage'] )
    template_data['language_percentage_css_color'] = get_dashboard_user_progress_css_color( template_data['language_percentage'] )
    template_data['education_percentage_css_color'] = get_dashboard_user_progress_css_color( template_data['education_percentage'] )
    template_data['work_percentage_css_color'] = get_dashboard_user_progress_css_color( template_data['work_percentage'] )

    # Print Template
    return render( request, 'points/dashboard/dashboard.html', template_data )





#######################
# EDIT USER INFORMATION VIEWS
#######################
@login_required
def edit_personal( request ):
    """
    Form to edit PERSONAL user data

    :param: request
    :return: String - HTML.
    """

    # Initial Settings
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Edit Personal - Immigration Calculator - Wanna Migrate' )
    template_data['meta_description'] = _( 'Check your chances of obtaining a permanent visa to move to Canada, Australia or New Zealand.' )

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
        initial_data = { 'australian_regional_immigration': False, 'family_overseas': False }
        user_personal_form = UserPersonalForm( request.POST or None, user = request.user, initial = initial_data )

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
    return render( request, 'points/user/edit_personal.html', template_data )


@login_required
def edit_language( request ):
    """
    Form to edit LANGUAGE data from the user

    :param: request
    :return: String - HTML
    """

    # Initial Settings
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Edit Language - Immigration Calculator - Wanna Migrate' )
    template_data['meta_description'] = _( 'Check your chances of obtaining a permanent visa to move to Canada, Australia or New Zealand.' )

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
        initial_data = { 'partner_english_level_answer': 896, 'partner_french_level_answer': 900 }
        user_language_form = UserLanguageForm( request.POST or None, user = request.user, initial = initial_data )

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
    return render( request, 'points/user/edit_language.html', template_data )


@login_required
def edit_education( request ):
    """
    Form to edit LANGUAGE data from the user

    :param: request
    :return: String - HTML
    """

    # Initial Settings
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Edit Education - Immigration Calculator - Wanna Migrate' )
    template_data['meta_description'] = _( 'Check your chances of obtaining a permanent visa to move to Canada, Australia or New Zealand.' )

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
        initial_data = { 'regional_australia_study': False, 'partner_education_level_answer': 904 }
        user_education_form = UserEducationForm( request.POST or None, user = request.user, initial = initial_data )

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
    return render( request, 'points/user/edit_education.html', template_data )


@login_required
def edit_work( request ):
    """
    Form to edit WORK data from the user

    :param: request
    :return: String - HTML
    """

    # Initial Settings
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Edit Work - Immigration Calculator - Wanna Migrate' )
    template_data['meta_description'] = _( 'Check your chances of obtaining a permanent visa to move to Canada, Australia or New Zealand.' )

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
        initial_data = {
            'partner_skills': False, 'willing_to_invest': False, 'canadian_startup_letter': False,
            'australian_professional_year': False, 'canadian_partner_work_study_experience': False,
            'work_offer': False
        }
        user_work_form = UserWorkForm( request.POST or None, user = request.user, initial = initial_data )

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
    return render( request, 'points/user/edit_work.html', template_data )


def get_occupations_html( request ):
    """
    Return json dictionary of occupations filtered by category ID

    :param: request
    :return String JSON
    """

    result = ''

    if request.is_ajax() and request.method == 'POST':

        occupation_category_id = request.POST['id_occupation_category']

        html = '<option value="">' + _( 'Select Occupation' ) + '</option>'
        occupations = Occupation.objects.filter( occupation_category_id = occupation_category_id ).order_by( 'name' )
        for occupation in occupations:
            html += '<option value="' + str( occupation.id ) + '">' + str( occupation.name ) + '</option>'

        result = html

    return HttpResponse( result )





#######################
# CALCULATE POINTS VIEWS
#######################
@login_required
def calculate_points( request ):
    """
    Heart of the system.
    It process all user data and calculate his points to all countries with
    immigration support enabled

    :param: request
    :return Redirect
    """

    # instantiate the calculator class
    immigration_calculator = ImmigrationCalculator( request.user )

    # First we get every country with immigration support enabled
    countries_list = [settings.ID_COUNTRY_AUSTRALIA, settings.ID_COUNTRY_CANADA, settings.ID_COUNTRY_NEW_ZEALAND]
    countries = Country.objects.filter( id__in = countries_list )
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
            'user_result_status': UserResultStatus.objects.get( pk = results['user_result_status_id'] ),
        }

        UserResult.objects.update_or_create(
            user = request.user, country = country, defaults = updated_values
        )

    # Remove flag for 'updating_now'
    UserStats.objects.update_or_create(
        user = request.user, defaults = { 'updating_now': False }
    )

    # Redirect to Dashboard
    return HttpResponseRedirect( reverse( "points:dashboard" ) )





#######################
# USER PER COUNTRY VIEWS
#######################
@login_required
def situation( request, country_name ):
    """
    My Situation

    :param: request
    :param country_name:
    :return: String - HTML
    """

    # Initializes template data
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Situation - Immigration Calculator - Wanna Migrate' )
    template_data['meta_description'] = _( 'Check your chances of obtaining a permanent visa to move to Canada, Australia or New Zealand.' )

    # Initial settings
    template_data['top_bar_css_class'] = "fixTopBar"
    template_data['country_name'] = country_name
    template_data['total_points'] = 0
    template_data['personal_points'] = 0
    template_data['language_points'] = 0
    template_data['education_points'] = 0
    template_data['work_points'] = 0
    template_data['status_success'] = False
    template_data['status_message'] = _( "You don’t have enough points" )

    # Instantiate all country_config
    country_config = CountryConfig.objects.all()
    country_config_data = {}
    for item in country_config:
        if item.country_id not in country_config_data:
            country_config_data[item.country_id] = {}
        country_config_data[item.country_id] = item

    # Get Country and set options for it
    if country_name == 'australia':
        country = Country.objects.get( pk = settings.ID_COUNTRY_AUSTRALIA )
        template_data['country_name_as_label'] = _( 'Australia' )
        template_data['map_css_class'] = 'australia'
        template_data['min_points'] = country_config_data[settings.ID_COUNTRY_AUSTRALIA].pass_mark_points
        template_data['personal_max_points'] = country_config_data[settings.ID_COUNTRY_AUSTRALIA].max_personal_points
        template_data['language_max_points'] = country_config_data[settings.ID_COUNTRY_AUSTRALIA].max_language_points
        template_data['education_max_points'] = country_config_data[settings.ID_COUNTRY_AUSTRALIA].max_education_points
        template_data['work_max_points'] = country_config_data[settings.ID_COUNTRY_AUSTRALIA].max_work_points

    elif country_name == 'canada':
        country = Country.objects.get( pk = settings.ID_COUNTRY_CANADA )
        template_data['country_name_as_label'] = _( 'Canada' )
        template_data['map_css_class'] = 'canada'
        template_data['min_points'] = country_config_data[settings.ID_COUNTRY_CANADA].pass_mark_points
        template_data['personal_max_points'] = country_config_data[settings.ID_COUNTRY_CANADA].max_personal_points
        template_data['language_max_points'] = country_config_data[settings.ID_COUNTRY_CANADA].max_language_points
        template_data['education_max_points'] = country_config_data[settings.ID_COUNTRY_CANADA].max_education_points
        template_data['work_max_points'] = country_config_data[settings.ID_COUNTRY_CANADA].max_work_points

    elif country_name == 'new-zealand':
        country = Country.objects.get( pk = settings.ID_COUNTRY_NEW_ZEALAND )
        template_data['country_name_as_label'] = _( 'New Zealand' )
        template_data['map_css_class'] = 'newzealand'
        template_data['min_points'] = country_config_data[settings.ID_COUNTRY_NEW_ZEALAND].pass_mark_points
        template_data['personal_max_points'] = country_config_data[settings.ID_COUNTRY_NEW_ZEALAND].max_personal_points
        template_data['language_max_points'] = country_config_data[settings.ID_COUNTRY_NEW_ZEALAND].max_language_points
        template_data['education_max_points'] = country_config_data[settings.ID_COUNTRY_NEW_ZEALAND].max_education_points
        template_data['work_max_points'] = country_config_data[settings.ID_COUNTRY_NEW_ZEALAND].max_work_points

    else:
        return HttpResponseRedirect( reverse( "points:dashboard" ) )


    # Get User Results for this country
    try:
        user_result = UserResult.objects.get( user = request.user, country = country )
    except UserResult.DoesNotExist:
        user_result = False

    # Pass user results to template
    if user_result:

        # points
        template_data['total_points'] = user_result.score_total
        template_data['personal_points'] = user_result.score_personal
        template_data['language_points'] = user_result.score_language
        template_data['education_points'] = user_result.score_education
        template_data['work_points'] = user_result.score_work

        # Status and message
        if user_result.user_result_status_id == settings.ID_RESULT_STATUS_ALLOWED:
            template_data['status_success'] = True
            template_data['status_message'] = _( "Enough points" )
        elif user_result.user_result_status_id == settings.ID_RESULT_STATUS_DENIED_POINTS:
            template_data['status_success'] = False
            template_data['status_message'] = _( "Not enough points" )
        elif user_result.user_result_status_id == settings.ID_RESULT_STATUS_DENIED_OCCUPATION:
            template_data['status_success'] = False
            template_data['status_message'] = _( "Occupation not in demand" )
        elif user_result.user_result_status_id == settings.ID_RESULT_STATUS_DENIED_AGE:
            template_data['status_success'] = False
            template_data['status_message'] = _( "Age not allowed" )
        elif user_result.user_result_status_id == settings.ID_RESULT_STATUS_DENIED_LANGUAGE:
            template_data['status_success'] = False
            template_data['status_message'] = _( "Language requirements not met" )
        elif user_result.user_result_status_id == settings.ID_RESULT_STATUS_DENIED_WORK_EXPERIENCE:
            template_data['status_success'] = False
            template_data['status_message'] = _( "Work experience not enough" )

    # Define the percentage CSS class to use around country flag for progress bar for total points
    template_data['percentage_total'] = math.floor( ( 100 * template_data['total_points'] ) / template_data['min_points'] )
    template_data['percentage_total_css_color'] = get_dashboard_country_progress_css_color( template_data['percentage_total'] )

    # Define the percentage CSS class for PERSONAL points
    if template_data['personal_points'] == 0 or template_data['personal_max_points'] == 0:
        template_data['personal_percentage'] = 0
    else:
        template_data['personal_percentage'] = math.floor( ( 100 * template_data['personal_points'] ) / template_data['personal_max_points'] )
    template_data['personal_percentage_css_color'] = get_dashboard_user_progress_css_color( template_data['personal_percentage'] )

    # Define the percentage CSS class for LANGUAGE points
    if template_data['language_points'] == 0 or template_data['language_max_points'] == 0:
        template_data['language_percentage'] = 0
    else:
        template_data['language_percentage'] = math.floor( ( 100 * template_data['language_points'] ) / template_data['language_max_points'] )
    template_data['language_percentage_css_color'] = get_dashboard_user_progress_css_color( template_data['language_percentage'] )

    # Define the percentage CSS class for EDUCATION points
    if template_data['education_points'] == 0 or template_data['education_max_points'] == 0:
        template_data['education_percentage'] = 0
    else:
        template_data['education_percentage'] = math.floor( ( 100 * template_data['education_points'] ) / template_data['education_max_points'] )
    template_data['education_percentage_css_color'] = get_dashboard_user_progress_css_color( template_data['education_percentage'] )

    # Define the percentage CSS class for WORK points
    if template_data['work_points'] == 0 or template_data['work_max_points'] == 0:
        template_data['work_percentage'] = 0
    else:
        template_data['work_percentage'] = math.floor( ( 100 * template_data['work_points'] ) / template_data['work_max_points'] )
    template_data['work_percentage_css_color'] = get_dashboard_user_progress_css_color( template_data['work_percentage'] )

    # If user does not have enough points, we build a list of hints for that country on how to get more points
    template_data['hints'] = []
    if template_data['total_points'] < template_data['min_points']:

        if country_name == 'australia':

            # Australia community language
            template_data['hints'].append( _( "You can get 5 extra points if you can get recognized as a translator for your native language.  You will have to do a test with <a href='www.naati.com.au/' target='blank'>NAATI</a>" ) )

            # work offer
            template_data['hints'].append( _( "If you can get a job offer from an Australia Employer (<a href='http://www.seek.com.au' target='blank'>Find jobs here</a>), You should ask your him to sponsor your visa.  It will be quicker and cheaper." ) )

            # skilled partner
            template_data['hints'].append( _( "You can get 5 extra points if you have a partner/espouse (stable union) and he/she is under 50 years old and in the same occupation as you." ) )

            # Regional Australia
            template_data['hints'].append( _( "If you are willing to live in a regional part of Australia in the beginning, it's easier to get the visa (more details soon)." ) )

            # Investments
            template_data['hints'].append( _( "If you have money/assets that you will take with you, you can apply for an investment visa." ) )

        elif country_name == 'canada':

            # Partner Language Level
            template_data['hints'].append( _( "You can get 5 extra points if your partner/spouse (stable union) has a basic level of english or french." ) )

            # Past study
            template_data['hints'].append( _( "You can get 5 extra points if you or your partner/espouse (stable union) complete any studies or have a past job in Canada." ) )

            # Family Member
            template_data['hints'].append( _( "You can get 5 extra points if you have a close family member in Canada." ) )

            # work offer
            template_data['hints'].append( _( "You can get 15 extra points if you can get a job offer from an Canada Employer (<a href='http://www.jobbank.gc.ca/' target='blank'>Find jobs here</a>)." ) )

            # Provincial visas
            template_data['hints'].append( _( "Each state of canada has its own additional immigration program, usually easier to get in. (<a href='http://www.immigration-quebec.gouv.qc.ca/en/' target='blank'>Check the Québec Immigration</a>)." ))

            # Investments
            template_data['hints'].append( _( "If you have money/assets that you will take with you, you can apply for an investment visa." ) )

        elif country_name == 'new-zealand':

            # Family Member
            template_data['hints'].append( _( "You can get 10 extra points if you have a close family member in New-Zealand." ) )

            # skilled partner
            template_data['hints'].append( _( "You can get 20 extra points if you have a partner/espouse with a skilled occupation or job offer." ) )

            # Work on Regional NEw Zealand
            template_data['hints'].append( _( "You can get up to 30 extra points if you have worked (or job offer) on a regional part of New Zealand." ) )

             # Investments
            template_data['hints'].append( _( "If you have money/assets that you will take with you, you can apply for an investment visa." ) )

    else:
        template_data['hints'].append( _( "<strong>Congratulations!</strong> You have enough points to apply for a visa" ) )


    # Print Template
    return render( request, 'points/country/situation.html', template_data )


@login_required
def visa_application( request, country_name ):
    """
    Visa Application

    :param: request
    :param country_name:
    :return: String - HTML
    """

    # Initializes template data
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Visa Application - Immigration Calculator - Wanna Migrate' )
    template_data['meta_description'] = _( 'Check your chances of obtaining a permanent visa to move to Canada, Australia or New Zealand.' )

    # Initial settings
    template_data['top_bar_css_class'] = "fixTopBar"
    template_data['country_name'] = country_name

    # Get Country and set options for it
    if country_name == 'australia':
        country = Country.objects.get( pk = settings.ID_COUNTRY_AUSTRALIA )
        template_data['map_css_class'] = 'australia'
        template_data['country_name_as_label'] = _( 'Australia' )

    elif country_name == 'canada':
        country = Country.objects.get( pk = settings.ID_COUNTRY_CANADA )
        template_data['map_css_class'] = 'canada'
        template_data['country_name_as_label'] = _( 'Canada' )

    elif country_name == 'new-zealand':
        country = Country.objects.get( pk = settings.ID_COUNTRY_NEW_ZEALAND )
        template_data['map_css_class'] = 'newzealand'
        template_data['country_name_as_label'] = _( 'New Zealand' )

    else:
        return HttpResponseRedirect( reverse( "points:dashboard" ) )

    # Print Template
    return render( request, 'points/country/visa_application.html', template_data )


@login_required
def professional_help( request, country_name ):
    """
    Moving

    :param: request
    :param country_name:
    :return: String - HTML
    """

    # Initial settings
    template_data = { 'country_name': country_name }

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Professional Help - Immigration Calculator - Wanna Migrate' )
    template_data['meta_description'] = _( 'Check your chances of obtaining a permanent visa to move to Canada, Australia or New Zealand.' )

    # Get Country and set options for it
    if country_name == 'australia':
        country = Country.objects.get( pk = settings.ID_COUNTRY_AUSTRALIA )
        template_data['map_css_class'] = 'australia'
        template_data['country_name_as_label'] = _( 'Australia' )

    elif country_name == 'canada':
        country = Country.objects.get( pk = settings.ID_COUNTRY_CANADA )
        template_data['map_css_class'] = 'canada'
        template_data['country_name_as_label'] = _( 'Canada' )

    elif country_name == 'new-zealand':
        country = Country.objects.get( pk = settings.ID_COUNTRY_NEW_ZEALAND )
        template_data['map_css_class'] = 'newzealand'
        template_data['country_name_as_label'] = _( 'New Zealand' )

    else:
        return HttpResponseRedirect( reverse( "points:dashboard" ) )

    # Print Template
    return render( request, 'points/country/professional_help.html', template_data )


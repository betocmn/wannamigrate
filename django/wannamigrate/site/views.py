"""
Site Views

These are the views that control logic flow for
the templates on site app
"""

##########################
# Imports
##########################
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.utils.translation import ugettext as _
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.conf import settings
import math
from wannamigrate.core.util import (
    get_object_or_false, get_dashboard_country_progress_css_class, get_dashboard_user_progress_css_class
)
from wannamigrate.site.forms import (
    ContactForm, LoginForm, SignupForm, PasswordRecoveryForm, PasswordResetForm,
    EditAccountInfoForm, EditAccountPasswordForm, SituationForm
)
from wannamigrate.core.models import (
    Country, UserSituation, Goal, Situation
)
from wannamigrate.marketplace.models import (
    Provider
)
from wannamigrate.core.mailer import Mailer
from django.utils import translation
from django.contrib.gis.geoip import GeoIP





#######################
# SITUATION FORM
#######################
def get_situation_form( request ):
    """
    It checks if it's a visitor or a logged user to
    return the correct situation form.

    The situation form is the one on landing-page and on
    top of every page, so it's used for many apps and views.

    Situation: "I'm From Brazil and wanna study in Canada"

    :param: request
    :return Object - Form object
    """

    # initializes the dict that will store values to be selected on the form by default
    initial_data = {}

    # Checks if there's an active session from this visitor/users
    if 'situation' in request.session and 'from_country' in request.session['situation']:
        initial_data['from_country'] = request.session['situation']['from_country']
        initial_data['to_country'] = request.session['situation']['to_country']
        initial_data['goal'] = request.session['situation']['goal']

    else:

        # Defaults to country by IP and other default values
        initial_data['to_country'] = Country.objects.get( pk = settings.ID_COUNTRY_CANADA )
        initial_data['goal'] = Goal.objects.get( pk = 1 )
        if 'situation' in request.session and 'country_code' in request.session['situation'] and request.session['situation']['country_code']:
            initial_data['from_country'] = Country.objects.get( code = request.session['situation']['country_code'] )
        else:
            initial_data['from_country'] = Country.objects.get( pk = settings.ID_COUNTRY_BRAZIL )

        # Makes sure sessions are set
        request.session['situation']['from_country'] = initial_data['from_country']
        request.session['situation']['goal'] = initial_data['goal']
        request.session['situation']['to_country'] = initial_data['to_country']
        try:
            situation = Situation.objects.get(
                from_country = initial_data['from_country'],
                to_country = initial_data['to_country'],
                goal = initial_data['goal']
            )
            request.session['situation']['total_users'] = situation.total_users
        except Situation.DoesNotExist:
            request.session['situation']['total_users'] = 0

    # Returns filled form
    if request.user.is_authenticated():
        return SituationForm( request.POST or None, initial = initial_data, user = request.user )
    else:
        return SituationForm( request.POST or None, initial = initial_data )


def change_situation( request ):
    """
    Action for the change situation form on the top of dashboard
    and internal pages

    :param: request
    :return: Boolean
    """

    # Creates form
    form = get_situation_form( request )

    # If the form has been submitted and is valid...
    if form.is_valid():

        # Saves in DB
        situation = form.save()

        # Saves this information in the session
        request.session['situation'] = {}
        request.session['situation']['from_country'] = situation.from_country
        request.session['situation']['to_country'] = situation.to_country
        request.session['situation']['goal'] = situation.goal
        request.session['situation']['total_users'] = situation.total_users

    # Redirects to dashboard
    return HttpResponseRedirect( reverse( 'site:dashboard' ) )





#######################
# HOME-PAGE VIEWS
#######################
def home( request ):
    """
    Home-Page - Used as a provocative landing page to conquer new users

    :param: request
    :return: String - The html page rendered
    """

    # Initializes template data dictionary
    template_data = {}

    # passes form to template
    template_data['form'] = get_situation_form( request )

    # Prints Template
    return render( request, 'site/home/home.html', template_data )





#######################
# LOGIN and SIGNUP VIEWS
#######################
def login( request ):
    """
    Process user login.

    :param: request
    :return: String - The html page rendered
    """

    # Checks if the user is already authenticated.
    if request.user.is_authenticated():
        # Redirects the user to the dashboard
        return HttpResponse( request.user.email )
        return HttpResponseRedirect( reverse( "site:dashboard" ) )


    email = 'humberto@wannamigrate.com'
    password = 'javascript3'
    user = authenticate( email = email, password = password )

    if user is not None and user.is_active:

        # Logins Successfully
        auth_login( request, user )

        # Checks if situation already exists
        try:
            user_situation = user.usersituation
        except UserSituation.DoesNotExist:
            user_situation = False

        # Update situation on session and DB
        if user_situation:
            situation = user_situation.situation
            request.session['situation']['from_country'] = situation.from_country
            request.session['situation']['to_country'] = situation.to_country
            request.session['situation']['goal'] = situation.goal
            request.session['situation']['total_users'] = situation.total_users

        # Make sure the user goes to the dashboard
        return HttpResponseRedirect( reverse( "site:dashboard" ) )
    else:
        return HttpResponse( 'Invalid Login' )

    """
    # Instantiates the forms on the template_data
    template_data = {}
    template_data['form'] = LoginForm()
    template_data['form_template'] = "site/signin/login_form.html"

    # Form submitted?
    if request.method == 'POST':

        # Create form
        form = LoginForm( request.POST )

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate( email = email, password = password )

            if user is not None and user.is_active:
                # Login Successfully
                auth_login( request, user )
                # Make sure the user goes to the dashboard
                return HttpResponseRedirect( reverse( "site:dashboard" ) )
            else:
                template_data[ 'error' ] = _( "Invalid login. Please try again." )
                template_data[ 'form' ] = form
                return render( request, "site/signin/container.html", template_data )

        else:
            if form.non_field_errors:
                msg = ''
                for k, v in form.errors.items():
                    msg += v
                template_data['error'] = msg
                template_data['form'] = form
                return render( request, "site/signin/container.html", template_data )
            
            template_data[ 'error' ] = _( "Invalid login. Please try again." )
            template_data[ 'form' ] = form
            return render( request, "site/signin/container.html", template_data )

    else:
        # Instantiate Forms
        template_data['form'] = LoginForm()
        return render( request, "site/signin/container.html", template_data )

    """

def logout( request ):
    """
    Process Logout

    :param: request
    :return HTTP Redirection:
    """

    # Executes auth Logout
    if request.user.is_authenticated():
        auth_logout( request )

    # Redirect to home-page
    return HttpResponseRedirect( reverse( "site:home" ) )


def signup( request ):
    """
    Signup action. It creates a new user on the platform

    :param: request
    :return: String - The html page rendered
    """

    # Checks if the user is already authenticated.
    if request.user.is_authenticated():
        # Redirects the user to the dashboard
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Instantiates the forms on the template_data
    template_data = {}
    template_data['form'] = SignupForm()
    template_data['form_template'] = "site/signin/signup_form.html"

    # Form submitted?
    if request.method == 'POST':

        # Create form
        form = SignupForm( request.POST )

        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create user
            user = get_user_model().objects.create_user( email, name = name, password = password )

            if user is not None:

                # Login user
                user = authenticate( email = email, password = password )
                auth_login( request, user )

                # Sends Welcome Email to User
                # TODO Change this to a celery/signal background task
                Mailer.send_welcome_email( user )

                # Return success to Ajax
                return HttpResponseRedirect( reverse( 'site:dashboard' ) )

            else:
                template_data['error'] = _( 'There was an error while creating your user account.' )
                template_data['form'] = form
                return render( request, "site/signin/container.html", template_data )

        else:

            if form.non_field_errors:
                msg = ''
                for k, v in form.errors.items():
                    msg += v
                template_data['error'] = msg
                template_data['form'] = form
                return render( request, "site/signin/container.html", template_data )

            template_data['error'] = _( 'Invalid Information! Make sure all fields are filled in and email and confirmation match.' )
            return render( request, "site/signin/container.html", template_data )

    else:
        return render( request, "site/signin/container.html", template_data )


def recover_password( request ):
    """
    Send a link to user redefine it password

    :param: request
    :return: String - The html page rendered
    """

    # Checks if the user is already authenticated.
    if request.user.is_authenticated():
        # Redirects the user to the dashboard
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Instantiates the forms on the template_data
    template_data = {}
    template_data['form'] = PasswordRecoveryForm()
    template_data['form_template'] = "site/signin/recover_password.html"

    # Form submitted?
    if request.method == 'POST':

        # Create form
        form = PasswordRecoveryForm( request.POST )
        template_data['form'] = form
        
        if form.is_valid():

            email = form.cleaned_data['email']
            user = get_object_or_false( get_user_model(), email = email )

            if user and user is not None and user.is_active:

                # Send email with link to reset password
                # TODO: Change this to a celery background event and use a try/exception block
                Mailer.send_reset_password_email( user )

                # Return success message to template
                template_data['success'] = _( 'Password reset instructions were successfully sent to your e-mail.' )
                template_data['form'] = PasswordRecoveryForm() # Create an empty form to clean e-mail field
                return render( request, "site/signin/container.html", template_data )

            else:
                # Return an error message to the template
                template_data['error'] = _( 'No user found with this e-mail address.' )
                return render( request, "site/signin/container.html", template_data )

        else:
            # Return an error message to the template
            template_data['error'] = _( 'Invalid e-mail address.' )
            return render( request, "site/signin/container.html", template_data )
    else:
        return render( request, "site/signin/container.html", template_data )


@sensitive_post_parameters()
@never_cache
def reset_password( request, uidb64 = None, token = None ):
    """
    Page to set a new password after clicking on a link from email sent by 'recover password feature'

    :param: request
    :param: uidb64
    :param: token
    :return: String - The html page rendered
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
    return render( request, 'site/signin/reset_password.html', template_data )





#######################
# CONTACT US VIEWS
#######################
def contact( request ):
    """
    Displays the contact page with a form to send us a message by email.

    :param: request
    :return: String - The html page rendered
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
    return render( request, 'site/contact/contact.html', template_data )





#######################
# HOW IT WORKS VIEW
#######################
def how_it_works( request ):
    """
    Displays "how It Works" static page

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Print Template
    return HttpResponse( "How It Works" )
    return render( request, 'site/about/tour.html')





#######################
# SERVICE PROVIDERS VIEWS
#######################
def service_providers( request ):
    """
    Displays "I'm a Service Provider" page

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Print Template
    return HttpResponse( "Service Providers" )
    return render( request, 'site/about/tour.html')





#######################
# TERMS, CONDITIONS AND PRIVACY
#######################
def terms( request ):
    """
    Displays "Terms and Conditions" static page

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Print Template
    return render( request, 'site/terms/terms.html')


def privacy( request ):
    """
    Displays "Privacy Policy" static page

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Print Template
    return render( request, 'site/terms/privacy.html')





#######################
# MY ACCOUNT VIEWS
#######################
@login_required
def view_account( request ):
    """
    Displays "My Account" page with user's info.

    :param: request
    :return String - HTML from my account page.
    """
    
    # Gets the user object.
    user = request.user

    # Renders the page
    return render( request, 'site/myaccount/view.html', { 'user': user } )


@login_required
def edit_account_info( request ):
    """
    Edit "My Account" page.

    :param: request
    :return String - HTML from Edit My Account page.
    """

    # Form submitted via POST
    if request.method == 'POST':

        user = request.POST.copy()
        user['email'] = request.user.email
        
        form = EditAccountInfoForm( user, instance = request.user )

        # Is valid? Save..
        if form.is_valid():
            # Save
            user = form.save()
            
            # Changes the active language
            translation.activate( user.preferred_language )
            request.session[translation.LANGUAGE_SESSION_KEY] = user.preferred_language

            messages.success( request, _('Data successfully updated.') )
            return HttpResponseRedirect( reverse( 'site:view_account' ) )
        # Form errors.
        else:
            return render( request, 'site/myaccount/edit_info.html', { 'form' : form } )

    # GET or any other method. Reads the user's info from session
    # and render the edit page.
    else:
        user = request.user
        form = EditAccountInfoForm( instance = user )
        return render( request, 'site/myaccount/edit_info.html', { 'form' : form } )


@login_required
def edit_account_avatar( request ):
    pass


@login_required
def edit_account_password( request ):
    """
    Edit account's password page.

    :param: request
    :return String - HTML from Edit account's password page.
    """
    # Form submitted via POST
    if request.method == 'POST':

        form = EditAccountPasswordForm( request.user, request.POST )

        # Is valid? Save..
        if form.is_valid():
            # TODO: Change the user's password
            form.save()

            messages.success( request, _('Data successfully updated.') )
            return HttpResponseRedirect( reverse( 'site:view_account' ) )
        # Form errors.
        else:
            return render( request, 'site/myaccount/edit_password.html', { 'form' : form } )

    # GET or any other method. Reads the user's info from session
    # and render the edit page.
    else:
        form = EditAccountPasswordForm( request.user )
        return render( request, 'site/myaccount/edit_password.html', { 'form' : form } )





#######################
# DASHBOARD VIEWS
#######################
def dashboard( request ):
    """
    Process the dashboard page.

    The dashboard is the main screen of the system,
    where the users can view its informations, progress, etc.

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initial template
    template_data = {}

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # Gets Service Providers
    template_data['providers'] = Provider.get_listing( 204, 0, 5 )

    # Print Template
    return render( request, 'site/dashboard/dashboard.html', template_data )

    # Print SQL Queries
    """
    from django.db import connection
    queries_text = ''
    for query in connection.queries:
        queries_text += '<br /><br /><br />' + str( query['sql'] )
    return HttpResponse( queries_text )
    """





#######################
# INTERNATIONALIZATION VIEWS
#######################
def setlang( request, language_code ):
    """
    Changes the current language to the desired language defined by language_code parameter.
    If you want to redirect the user to other page that isn't '/' provide a parameter named "next" in the GET request.

    :param: request Default request param.
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






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
    EditAccountInfoForm, EditAccountPasswordForm, VisitorGoalForm
)
from wannamigrate.core.models import (
    Country
)
from wannamigrate.points.models import (
    UserResult, CountryConfig
)
from wannamigrate.core.mailer import Mailer
from django.utils import translation
from django.contrib.gis.geoip import GeoIP





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

    # Check if there's an active session, or if not, country from IP
    initial_data = {}
    if 'visitor' in request.session:

        initial_data['from_country'] = request.session['visitor']['from_country']
        initial_data['to_country'] = request.session['visitor']['to_country']
        initial_data['goal'] = request.session['visitor']['goal']

    else:

        # Gets country code from IP address of user
        x_forwarded_for = request.META.get( 'HTTP_X_FORWARDED_FOR' )
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get( 'REMOTE_ADDR' )
        geo_ip = GeoIP()
        #result = geo_ip.country( ip ) # THIS IS THE CORRECT LINE
        result = geo_ip.country( '191.189.150.101' ) # USING THIS JUST FOR TESTING PURPOSES
        country_code = result['country_code']
        initial_data['from_country'] = Country.objects.get( code = country_code )
        initial_data['to_country'] = settings.ID_COUNTRY_CANADA
        initial_data['goal'] = 1

    # Creates form
    form = VisitorGoalForm( request.POST or None, initial = initial_data )

    # If the form has been submitted and is valid...
    if form.is_valid():

        if 'visitor' not in request.session:

            # Saves in DB
            visitor_goal = form.save()

            # Saves this information in the session
            request.session['visitor'] = {}
            request.session['visitor']['from_country'] = visitor_goal.from_country.id
            request.session['visitor']['to_country'] = visitor_goal.to_country.id
            request.session['visitor']['goal'] = visitor_goal.goal.id

        # Redirects to dashboard
        return HttpResponseRedirect( reverse( 'site:dashboard' ) )

    # passes form to template
    template_data['form'] = form

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
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

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
# TOUR VIEWS
#######################
def tour( request ):
    """
    Displays "how It Works" static page

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Print Template
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
@login_required
def not_supported( request ):
    """
    Displays a page saying that the device is not supported.

    :param: request
    :return String - HTML from The not_supported page.
    """
    username_explode = request.user.name.split( ' ' )
    first_name = username_explode[0]
    return render( request, "site/home/not_supported.html", { "first_name" : first_name } )


def maintenance( request ):
    """
    Displays a page saying that the device is not supported.

    :param: request
    :return String - HTML from The not_supported page.
    """
    return render( request, "site/home/maintenance.html" )



def dashboard( request ):
    """
    Process the dashboard page.

    The dashboard is the main screen of the system,
    where the users can view its informations, progress, etc.

    :param: request
    :return String - HTML from The dashboard page.
    """

    # If User edited data, but did not calculate points by clicking in save and exit
    return HttpResponse( request.session['visitor']['from_country'] )

    # Print Template
    #return render( request, 'site/dashboard/dashboard.html', template_data )





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






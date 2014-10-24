from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from wannamigrate.core.util import get_object_or_false
from wannamigrate.site.forms import ContactForm, LoginForm, SignupForm, PasswordRecoveryForm, PasswordResetForm
from wannamigrate.core.mailer import Mailer


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

    # Print Template
    return render( request, 'site/dashboard.html' )



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
    return render( request, 'site/account.html' )
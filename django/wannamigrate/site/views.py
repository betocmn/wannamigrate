from django.shortcuts import render
from wannamigrate.site.forms import ContactForm
from wannamigrate.core.mailer import Mailer
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


#######################
# HOME-PAGE VIEWS
#######################
def home( request ):
    """
    Home-Page - Used as a provocative landing page to conquer new users

    :param request:
    :return String - The contact page rendered:
    """

    # Print Template
    return render( request, 'site/home.html' )


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
    template_data = {}

    # If the form has been submitted...
    if request.method == 'POST':

        form = ContactForm( request.POST )
        template_data[ 'form' ] = form

        if form.is_valid():
            email = form.cleaned_data[ 'email' ]
            message = form.cleaned_data[ 'message' ]

            # Send Email with message
            # TODO: Change this to a celery background event and use a try/exception block
            send_result = Mailer.send_contact_email( { 'email': email, 'message': message } )
            
            if send_result == True:
                template_data[ 'error' ] = False
            else:
                template_data[ 'error' ] = 'Error, please try again.'

        else:
            template_data[ 'error' ] = 'Please provide valid information.'

    else:
        template_data[ 'form' ] = ContactForm()

    # Print Template
    return render( request, 'site/contact.html', template_data )


#######################
# LOGIN VIEWS
#######################
def login( request ):
    """
    Process traditional login with email/password combination

    :param request:
    :return String - The html page rendered:
    """

    # -----> code here, márcio boy


def logout( request ):
    """
    Process Logout

    :param request:
    :return HTTP Redirection:
    """

    # Executes auth Logout
    auth_logout( request )

    # Print Template
    return HttpResponseRedirect( reverse( "site:home" ) )



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



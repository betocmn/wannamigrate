from django.shortcuts import render
from wannamigrate.site.forms import ContactForm
from wannamigrate.core.mailer import Mailer
from django.http import HttpResponse, HttpResponseRedirect
from wannamigrate.constants import *
from django.core.urlresolvers import reverse

# Contact page
def contact( request ):
    """
    Displays the contact page.

    :param request:
    :return The contact page rendered
    """

    # The url to open when the user is logged.
    login_redirect_url = request.build_absolute_uri( '/site/login' )
    

    template_data = {
        'login_redirect' : login_redirect_url
    }


    # If the form has been submitted...
    if request.method == 'POST':
        form = ContactForm( request.POST )
        template_data[ 'form' ] = form

        if form.is_valid():
            email = form.cleaned_data[ 'email' ]
            message = form.cleaned_data[ 'message' ]

            send_result = Mailer.send_contact_email( { 'email': email, 'message': message } )
            
            if send_result == True:
                template_data[ 'error' ] = False
            else:
                template_data[ 'error' ] = 'Error, please try again.'

        else:
            template_data[ 'error' ] = 'Please provide valid information.'

    else:
        # Creates a form and renders the page.
        template_data[ 'form' ] = ContactForm()
    
    return render( request, 'site/contact.html', template_data )

def home_index( request ):
    pass

#TODO: fix this
from django_facebook.api import *

def login( request ):

    # E-mail authentication
    if request.method == 'POST':
        return HttpResponse( "email" )

    else:

        if "facebook_login" in request.GET:
            access_token = request.GET[ 'access_token' ]
            graph = get_facebook_graph( request, access_token )
            profile = graph.get('me')

            # Informações uteis do facebook:
            # profile[ 'first_name' ]
            # profile[ 'last_name' ]
            # profile[ 'email' ]

            #TODO: Check if the user is already registered
            # and if not, register the user on the plataform.
            return HttpResponse( 'FACEBOOK' )

        elif "linkedin" in request.GET:
            pass


def logout( request ):
    pass


def linkedin_auth( request ):

    # Checks if the authorization code is returned via get and then logs the user on the platform
    if "code" in request.GET:
        if request.GET[ 'state' ] != LINKEDIN_STATE:
            return HttpResponse( "error" )  #TODO: FIX THIS

        # Imports the linkedin lib.
        from wannamigrate.core.linkedin import linkedin

        # Gets the authorization code
        authorization_code = request.GET[ 'code' ]        

        # TODO: try-catch this to handle linkedin errors 
        redirect_uri = request.build_absolute_uri( '/site/linkedin_auth' )
        # Creates the authentication object
        authentication = linkedin.LinkedInAuthentication( LINKEDIN_API_KEY, LINKEDIN_API_SECRET, redirect_uri, linkedin.PERMISSIONS.enums.values() )
        authentication.authorization_code = authorization_code # Sets the authorization code
        authentication.get_access_token() # Gets the access token
        
        # Pass it in to the app...
        application = linkedin.LinkedInApplication(authentication)

        # Use the app....
        t = application.get_profile()

        return HttpResponse( t['firstName'] )

    # No code given, means that it's not returning from linkedin.
    else:
        redirect_uri = request.build_absolute_uri( '/site/linkedin_auth' ) # The URL to return when user allows the app.
        linkedin_auth_url = "https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=" + LINKEDIN_API_KEY + "&scope=" + LINKEDIN_SCOPE + "&state=" + LINKEDIN_STATE + "&redirect_uri=" + redirect_uri
        return HttpResponseRedirect( linkedin_auth_url )



def facebook_auth( request ):
    return_url = reverse( "site:login" ) # The URL to return when user allows the app.


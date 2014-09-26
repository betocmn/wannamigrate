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

    #####################################################################################################################################
    # The following code should be placed on the view that handles the template containing signing up with social networks.
    #####################################################################################################################################
    # The URL to authenticate on linkedin and the REDIRECT_URL when users authenticate the Wanna Migrate to get their informations.
    linkedin_redirect_uri = request.build_absolute_uri( '/site/linkedin_auth' ) # The URL to return when user allows the app.
    linkedin_auth_url = "https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=" + SOCIAL_AUTH_LINKEDIN_KEY + "&redirect_uri=" + linkedin_redirect_uri
    # The URL to authenticate on facebook and the REDIRECT_URL when users authenticate the Wanna Migrate to get their informations.
    facebook_redirect_uri = request.build_absolute_uri( '/site/facebook_auth' )
    facebook_auth_url = "https://www.facebook.com/dialog/oauth?client_id=" + SOCIAL_AUTH_FACEBOOK_KEY + "&redirect_uri=" + facebook_redirect_uri
    #####################################################################################################################################

    # The url to open when the user is logged.
    login_redirect_url = request.build_absolute_uri( '/site/login' )
    

    template_data = {
        'login_redirect' : login_redirect_url,
        'linkedin_auth_url' : linkedin_auth_url,
        'facebook_auth_url' : facebook_auth_url
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
    pass
    
def facebook_auth( request ):
    pass



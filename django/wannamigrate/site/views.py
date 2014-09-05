from django.shortcuts import render
from wannamigrate.site.forms import ContactForm
from wannamigrate.core.mailer import Mailer

# Contact page
def contact( request ):

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

def login_index( request ):
    pass

def login_logout( request ):
    pass
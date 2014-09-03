from django.shortcuts import render
from wannamigrate.site.forms import ContactForm
from wannamigrate.core.mailer import Mailer

# Contact page
def contact( request ):
    # If the form has been submitted...
    if request.method == 'POST':
        form = ContactForm( request.POST )

        if form.is_valid():
            email = form.cleaned_data[ 'email' ]
            message = form.cleaned_data[ 'message' ]

            send_result = Mailer.send_contact_email( { 'email': email, 'message': message } )
            
            if send_result == True:
                return render( request, 'site/contact.html', { 'form': form, 'error': False } )
            else:
                return render( request, 'site/contact.html', { 'form': form, 'error': 'Error, try again.' } )

        else:
            return render( request, 'site/contact.html', { 'form': form, 'error': 'Please provide valid information.' } )

    else:
        # Creates an e-mail form and renders the page.
        form = ContactForm()
        return render( request, 'site/contact.html', { 'form': form, } )

def home_index( request ):
    pass

def login_index( request ):
    pass

def login_logout( request ):
    pass
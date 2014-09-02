from django.shortcuts import render
from wannamigrate.landing_page.models import LandingPageEmail
from wannamigrate.landing_page.forms import LandingPageEmailForm
from django.http import HttpResponse
import json



# Create your views here.
def index( request ):
    # If the form has been submitted...
    if request.method == 'POST': 
        
        # The response data should be like bellow, where
        # email_saved == 1 means that everything was ok and
        # message is the message to be displayed to the user.
        response_data = {
            'email_saved' : 0,
            'message' : "Unknown Error.. Please try again."
        }
        
        # Get the posted data
        form = LandingPageEmailForm( request.POST ) 
        if form.is_valid(): # If all validation rules passed
            cleaned_email = form.cleaned_data[ 'email' ]
            # Checks if e-mail already registered on database.
            if not LandingPageEmail.objects.filter( email = cleaned_email ):
                user_email = LandingPageEmail( email = cleaned_email )
                user_email.save()
                if user_email.pk is not None: # email saved?
                    response_data[ 'email_saved' ] = 1
                    response_data[ 'message' ] = 'Thank you! You\'ll be notified.' 
            else:
                response_data[ 'email_saved' ] = 1
                response_data[ 'message' ] = 'You\'re already registered.' 
        else:
            response_data[ 'email_saved' ] = 0
            response_data[ 'message' ] = 'Please enter a valid e-mail.' 
        
        # Returns a HttpResponse in JSON format.
        return HttpResponse( json.dumps( response_data ), content_type = "application/json" )

    else:
        # Creates an e-mail form and renders the page.
        form = LandingPageEmailForm()
        return render( request, 'index.html', { 'form': form, } )
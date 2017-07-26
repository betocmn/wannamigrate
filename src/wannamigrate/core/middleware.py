"""
Custom MIDDLEWARE
https://docs.djangoproject.com/en/1.11/topics/http/middleware/

Used to setup sessions before the request is processed by the views

"""

##########################
# Imports
##########################
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.templatetags.static import static
from wannamigrate.core.models import Country


##########################
# Function definitions
##########################
class SetupMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):

        # If country is not set, default to Australia
        if 'country_id' not in request.session or not request.session['country_id']:
            request.session['country_id'] = settings.DB_ID_COUNTRY_AUSTRALIA
            request.session['country_name'] = 'Australia'
            request.session['country_slug'] = 'australia'
            request.session.modified = True

        # If a different country slug was passed, updates the session
        if 'country_slug' in view_kwargs:
            if view_kwargs['country_slug'] != request.session['country_slug']:
                country = Country.objects.filter(
                    slug=view_kwargs['country_slug'], id__in=settings.DB_ID_COUNTRIES_ENABLED
                ).first()
                if country:
                    request.session['country_id'] = country.id
                    request.session['country_name'] = country.name
                    request.session['country_slug'] = country.slug
                    request.session.modified = True
                else:
                    messages.error(request, 'This country is not enabled at the moment.')
                    return redirect('landing:home')

        # If avatar is not present, sets the default one
        if 'avatar_url' not in request.session:
            request.session['avatar_url'] = static('site/img/avatar-default.png')

        return None

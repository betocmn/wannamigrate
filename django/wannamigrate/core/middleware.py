"""
Custom MIDDLEWARES for Wanna Migrate

Middleware is a framework of hooks into Django’s request/response processing.
It’s a light, low-level “plugin” system for globally altering Django’s input or output.
https://docs.djangoproject.com/en/1.7/topics/http/middleware/

"""

##########################
# Imports
##########################
from django.conf import settings
import pytz
from django.utils import timezone, translation
from django.contrib.gis.geoip import GeoIP





##########################
# Class definitions
##########################
class SituationLocaleMiddleware( object ):

    def process_request( self, request ):

        # if this is a guest visitor's first visit
        if not request.user.is_authenticated() and 'situation' not in request.session:

            # Gets country code from IP address of user
            x_forwarded_for = request.META.get( 'HTTP_X_FORWARDED_FOR' )
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get( 'REMOTE_ADDR' )
            geo_ip = GeoIP()
            result = geo_ip.country( ip )
            if not settings.IS_PROD:
                result = geo_ip.country( '191.189.150.101' )
            country_code = result['country_code']

            # stores country_code in session to be used on views
            request.session['situation'] = {}
            request.session['situation']['country_code'] = country_code

            # sets language
            lower_country_code = country_code.lower()
            for language in settings.COUNTRIES_BY_LANGUAGE:
                if lower_country_code in settings.COUNTRIES_BY_LANGUAGE[language]:
                    translation.activate( language )
                    request.session[translation.LANGUAGE_SESSION_KEY] = language

            # sets timezone
            timezone_name = pytz.country_timezones[country_code.lower()][0]
            if timezone_name:
                timezone.activate( pytz.timezone( timezone_name ) )
                request.session['django_timezone'] = timezone_name
            else:
                timezone.deactivate()
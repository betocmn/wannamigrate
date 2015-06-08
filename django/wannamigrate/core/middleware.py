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
from wannamigrate.core.models import Situation, Country, Goal, Notification




##########################
# Class definitions
##########################
class SituationLocaleMiddleware( object ):

    def process_request( self, request ):



        # If a language subdomain was forced (eg: 'https://pt.wannamigrate.com' - SEO
        subdomain = request.get_host().split( '.', 2 )[0]
        if subdomain not in [ 'www', 'dev' ] and subdomain in settings.COUNTRIES_BY_LANGUAGE:
            translation.activate( subdomain )
            request.session[translation.LANGUAGE_SESSION_KEY] = subdomain

        # if this is a guest visitor's first visit we try to get their country
        if not request.user.is_authenticated() and 'situation' not in request.session:

            request.session['situation'] = {}
            request.session['situation']['country_code'] = 'br'

            #TODO - When we install the geoIP library, just uncommnet the code below and erase the above

            """
            from django.contrib.gis.geoip import GeoIP

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
            """

        # If there's no situation session, sets one with default values
        if 'situation' not in request.session or 'from_country' not in request.session['situation']:

            # Defaults to country by IP and other default values
            to_country = Country.objects.get( pk = settings.ID_COUNTRY_CANADA )
            goal = Goal.objects.get( pk = 1 )
            if 'situation' in request.session and 'country_code' in request.session['situation'] and request.session['situation']['country_code']:
                from_country = Country.objects.get( code = request.session['situation']['country_code'] )
            else:
                from_country = Country.objects.get( pk = settings.ID_COUNTRY_BRAZIL )
    
            # Sets Session
            request.session['situation'] = {}
            request.session['situation']['from_country'] = from_country
            request.session['situation']['goal'] = goal
            request.session['situation']['to_country'] = to_country
            try:
                situation = Situation.objects.get(
                    from_country = from_country,
                    to_country = to_country,
                    goal = goal
                )
                request.session['situation']['total_users'] = situation.total_users
            except Situation.DoesNotExist:
                request.session['situation']['total_users'] = 0

        if request.user.is_authenticated():
            news = Notification.get_news_for( request.user )
            request.session[ "news" ] = news
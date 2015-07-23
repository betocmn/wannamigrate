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
from django.utils import translation
from wannamigrate.core.models import Situation, Country, Goal, Notification, Language, UserSituation
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import F
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext as _





##########################
# Locale Midlleware
##########################
class LocaleMiddleware( object ):

    def process_request( self, request ):

        # if language was still not set
        if 'language' not in request.session:

            if request.user.is_authenticated():

                # activates current preferred language set by user
                translation.activate( request.user.preferred_language )
                request.session[translation.LANGUAGE_SESSION_KEY] = request.user.preferred_language

            else:

                # searches for a language subdomain (eg: 'https://pt.wannamigrate.com')
                subdomain = request.get_host().split( '.', 2 )[0]
                if subdomain not in [ 'www', 'dev' ] \
                    and subdomain in settings.COUNTRIES_BY_LANGUAGE \
                    and subdomain != translation.get_language():
                    translation.activate( subdomain )
                    request.session[translation.LANGUAGE_SESSION_KEY] = subdomain

            # Gets language ID from DB and saves in session
            language = Language.objects.get( code = translation.get_language() )
            request.session['language'] = {
                'id': language.id,
                'name': language.name,
                'code': language.code
            }




##########################
# Email Validation Midlleware
##########################
class EmailValidationMiddleware( object ):

    def process_request( self, request ):

        if request.user.is_authenticated():
            if 'email_validated' not in request.session and request.path_info not in [reverse( 'site:edit_account' ),reverse( 'site:logout' ) ]:
                try:
                    validate_email( request.user.email )
                    request.session['email_validated'] = True
                except ValidationError:
                    messages.error( request, _( 'You need a valid email address to use the site!' ) )
                    return HttpResponseRedirect( reverse( 'site:edit_account' ) )





##########################
# Situation Midlleware
##########################
class SituationMiddleware( object ):

    def process_request( self, request ):

        if request.user.is_authenticated():
            if 'email_validated' not in request.session and request.path_info not in [reverse( 'site:edit_account' ),reverse( 'site:logout' ) ]:
                try:
                    validate_email( request.user.email )
                    request.session['email_validated'] = True
                except ValidationError:
                    messages.error( request, _( 'You need a valid email address to use the site!' ) )
                    return HttpResponseRedirect( reverse( 'site:edit_account' ) )

        # Default data
        populate_situation_session = False
        default_situation_id = 35

        # If it's first time access
        if 'situation' not in request.session:
            populate_situation_session = True
            situation = Situation.objects.get( pk = default_situation_id )

        # if user just logged in or signed up, we need to adjust the situation
        elif request.user.is_authenticated() and 'login_or_signup_started' in request.session:
            del request.session['login_or_signup_started']
            user_situation = UserSituation.get_details( request.user.id )
            if not user_situation:
                request.session['conversion_new_signup'] = True # this will be used for marketing conversion pixels
                situation, created = Situation.objects.get_or_create(
                    from_country_id = request.session['situation']['from_country']['id'],
                    to_country_id = request.session['situation']['to_country']['id'],
                    goal_id = request.session['situation']['goal']['id'],
                    defaults = {
                        'total_users': 1,
                        'total_visitors': 0,
                        'from_country_id': request.session['situation']['from_country']['id'],
                        'to_country_id': request.session['situation']['to_country']['id'],
                        'goal_id': request.session['situation']['goal']['id']
                    }
                )
                if not created:
                    situation.total_users = F( 'total_users' ) + 1
                    situation.save()
                user_situation = UserSituation()
                user_situation.user = request.user
                user_situation.situation = situation
                user_situation.save()
                populate_situation_session = True

            else:

                if 'situation_updated' in request.session:
                    del request.session['situation_updated']
                    if user_situation.situation.id != request.session['situation']['id']:
                        user_situation.situation_id = request.session['situation']['id']
                        user_situation.save()
                else:
                    situation = user_situation.situation
                    populate_situation_session = True

        # populate session with situation details
        if populate_situation_session:

            # gets situation details from the DB
            from_country = Country.objects.get( pk = situation.from_country_id )
            to_country = Country.objects.get( pk = situation.to_country_id )
            goal = Goal.objects.get( pk = situation.goal_id )

            # Sets Session
            request.session['situation'] = { 'id': situation.id, 'from_country': {}, 'goal': {}, 'to_country': {} }
            request.session['situation']['from_country']['id'] = from_country.id
            request.session['situation']['from_country']['name'] = from_country.name
            request.session['situation']['from_country']['code'] = from_country.code
            request.session['situation']['goal']['id'] = goal.id
            request.session['situation']['goal']['name'] = goal.name
            request.session['situation']['to_country']['id'] = to_country.id
            request.session['situation']['to_country']['name'] = to_country.name
            request.session['situation']['to_country']['code'] = to_country.code
            request.session['situation']['total_users'] = situation.total_users





##########################
# Notifications Middleware
##########################
class NotificationMiddleware( object ):
    def process_request( self, request ):
        request.session.news_count = 0
        if request.user.is_authenticated():
            request.session.news_count = Notification.get_news_count_for( request.user )






##########################
# Maintainance Midlleware
##########################
class MaintenanceMiddleware( object ):

    def process_request( self, request ):
        from django.shortcuts import render
        return render( request, "site/home/maintenance.html" )






"""
Django settings for wannamigrate_new project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from django.utils.translation import ugettext_lazy as _
import os


#########################################
# GENERAL SYSTEM CONFIGURATIONS
#########################################
# Base directory path
BASE_DIR = os.path.dirname( os.path.dirname( __file__ ) )

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&3je*i!yr=4y3sk&sm7^_@(fhd@^z7re&$y-b-wx(zsm3(6nyk'

# The base URL Conf
ROOT_URLCONF = 'wannamigrate.urls'

# Path of wsgi app
WSGI_APPLICATION = 'wannamigrate.wsgi.application'

# User Model
AUTH_USER_MODEL = 'core.User'

# Login URL
LOGIN_URL = 'admin:login'



#########################################
# INTERNATIONALIZATION AND LOCALIZATION
#########################################
LANGUAGES = (
    ( 'en-us', _( 'English' ) ),
    ( 'pt-BR', _( 'Portuguese (BR)' ) ),
)

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join( BASE_DIR, '../locale' ),
)



#########################################
# STATIC AND TEMPLATE FILES
#########################################
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join( BASE_DIR, '../static' )

# Templates
TEMPLATE_DIRS = (
    os.path.join( BASE_DIR, '../templates' ),
)

# Template Context Processors
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)



#########################################
# EMAIL SETTINGS
#########################################
DEFAULT_FROM_EMAIL = 'Wanna Migrate <contact@wannamigrate.com>'
EMAIL_HOST = 'smtp.wannamigrate.com'
EMAIL_HOST_USER = 'contact@wannamigrate.com'
EMAIL_HOST_PASSWORD = 'ju829sj'
EMAIL_PORT = 587



#########################################
# SOCIAL PLUGIN SETTINGS
#########################################

# Django changed the default session serialization method to JSON instead of Pickle, 
# which doesn't work with object instances. The following line is switching it back to pickle.
# This change is required to python-social-auth work properly.
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Facebook APP Key
SOCIAL_AUTH_FACEBOOK_KEY = "336536879856373"
# Facebook APP Secret
SOCIAL_AUTH_FACEBOOK_SECRET = "4ca87548565ab5d9c40e60bb6309e219"
# Facebook APP Scope
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Linkedin APP Key
SOCIAL_AUTH_LINKEDIN_KEY = "77eu4cz7x6srp6"
# Linkedin APP Secret
SOCIAL_AUTH_LINKEDIN_SECRET = "VOaF1eUDOlHziUTn"
# Linkedin APP Scope
SOCIAL_AUTH_LINKEDIN_SCOPE = [ 'r_emailaddress' ]
SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = ['email-address']
# Arrange to add the fields to UserSocialAuth.extra_data
SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [
    ('id', 'id'),
    ('firstName', 'first_name'),
    ('lastName', 'last_name'),
    ('email', 'email_address'),
]

# Twitter APP Key
SOCIAL_AUTH_TWITTER_KEY = "LIK43CXqkCJjEDKmP4LsqPLD7"
# Twitter APP Secret
SOCIAL_AUTH_TWITTER_SECRET = "BpK70KSeb3RePk6WXoFumG6jMV2sRLY623hzpkHVdXr85eq7sD"

# Google APP Key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "90947248109-nvu6v5d6rvpav60ps1sgrtplt5vlinhp.apps.googleusercontent.com"
# Google APP Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "4I7fFTTrlVfoHLbPNn6lviCK"

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.linkedin.LinkedinOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GooglePlusAuth',
    #'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/site/dashboard/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/site/login-error/'
SOCIAL_AUTH_USER_MODEL = 'core.User'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = [ 'email' ]
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_SLUGIFY_USERNAMES = False
#SOCIAL_AUTH_URL_NAMESPACE = "social"

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)



#########################################
# IMMIGRATION POINTS SETTINGS
#########################################

# Database IDs of questions used on code
ID_QUESTION_FAMILY_OVERSEAS = 1
ID_QUESTION_AGE = 2
ID_QUESTION_ENGLISH = 3
ID_QUESTION_FRENCH = 4
ID_QUESTION_EDUCATION_DEGREE = 5
ID_QUESTION_WORK_OFFER = 6
ID_QUESTION_WORK_EXPERIENCE_OUTSIDE = 7
ID_QUESTION_WORK_EXPERIENCE_INSIDE = 8
ID_QUESTION_OCCUPATION = 9
ID_QUESTION_SKILLED_PARTNER = 10
ID_QUESTION_INVEST = 11
ID_QUESTION_STARTUP_LETTER = 12
ID_QUESTION_US_CITIZEN = 13
ID_QUESTION_STUDY_REGIONAL_AU = 14
ID_QUESTION_PROFESSIONAL_YEAR_AU = 15
ID_QUESTION_LIVE_REGIONAL_AU = 16
ID_QUESTION_COMMUNITY_LANGUAGE_AU = 17

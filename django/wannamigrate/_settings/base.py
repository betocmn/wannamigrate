"""
Django settings for wannamigrate_new project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

##########################
# Imports
##########################
from django.utils.translation import ugettext_lazy as _
import os





#########################################
# GENERAL SYSTEM CONFIGURATIONS
#########################################
# Base directory path
BASE_DIR = os.path.dirname( os.path.dirname( __file__ ) )

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&3je*i!yr=4y3sk&sm7^_@(fhd@^z7re&$y-b-wx(zsm3(6nyk'

# Path of wsgi app
WSGI_APPLICATION = 'wannamigrate.wsgi.application'

# User Model
AUTH_USER_MODEL = 'core.User'

# Login URL
LOGIN_URL = 'site:login'





#########################################
# SSL
#########################################
# secure proxy SSL header and secure cookies
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
os.environ['wsgi.url_scheme'] = 'https'





#########################################
# INTERNATIONALIZATION AND LOCALIZATION
#########################################
LANGUAGES = (
    ( 'en', _( 'English' ) ),
    ( 'pt', 'Português' ),
)

LANGUAGE_CODE = 'en'

# countries that speak Non-english languages supported by our LANGUAGES setting
COUNTRIES_BY_LANGUAGE = {
    'pt': [ 'br', 'pt', 'mz', 'ao', 'gw', 'mo', 'cv', 'st', 'tl' ]
}

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join( BASE_DIR, '..', 'locale' ),
)





#########################################
# PATHS FOR STATIC, UPLOAD and TEMPLATES
#########################################
# Global UPLOAD folder
MEDIA_ROOT = os.path.join( BASE_DIR, '..', 'upload' )
MEDIA_URL = '/upload/'

# User Profile Pictures
UPLOAD_USER_PICTURE_ROOT = os.path.join( BASE_DIR, '..', 'upload', 'user_pictures' )
UPLOAD_USER_PICTURE_FOLDER = 'user_pictures'

# Statis Files paths
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join( BASE_DIR, '..', 'static' )

# Templates
TEMPLATE_DIRS = (
    os.path.join( BASE_DIR, '..', 'templates' ),
)

# The base URL Conf
ROOT_URLCONF = 'wannamigrate.urls'





#########################################
# TEMPLATE SETTINGS
#########################################

# Template Context Processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'wannamigrate.core.context_processors.add_global_template_data',
)





#########################################
# MIDDLEWARES
#########################################
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'wannamigrate.core.middleware.SituationLocaleMiddleware',
)





#########################################
# EMAIL SETTINGS
#########################################

# Default email to send messages to users
DEFAULT_FROM_EMAIL = 'Wanna Migrate <contact@wannamigrate.com>'

# SMTP Config
EMAIL_HOST = 'smtpi.wannamigrate.com'
EMAIL_HOST_USER = 'contact@wannamigrate.com'
EMAIL_HOST_PASSWORD = 'ju829sj'
EMAIL_PORT = 587

# Email to reiceve contact form messages
EMAIL_NOTIFICATION_CONTACT_FORM = 'humberto@wannamigrate.com'
EMAIL_NOTIFICATION_PROVIDER_SIGNUP = 'humberto@wannamigrate.com'
EMAIL_NOTIFICATION_PROVIDER_SIGNUP = 'humberto@wannamigrate.com'
EMAIL_NOTIFICATION_NEW_ORDER = 'humberto@wannamigrate.com'
EMAIL_NOTIFICATION_CONVERSATION_ACTIVITY = 'humberto@wannamigrate.com'





#########################################
# SOCIAL PLUGIN SETTINGS
#########################################

# Django changed the default session serialization method to JSON instead of Pickle, 
# which doesn't work with object instances. The following line is switching it back to pickle.
# This change is required to python-social-auth work properly.
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Facebook APP Key
SOCIAL_AUTH_FACEBOOK_KEY = '336536879856373'
# Facebook APP Secret
SOCIAL_AUTH_FACEBOOK_SECRET = '4ca87548565ab5d9c40e60bb6309e219'
# Facebook APP Scope
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Linkedin APP Key
SOCIAL_AUTH_LINKEDIN_KEY = '77eu4cz7x6srp6'
# Linkedin APP Secret
SOCIAL_AUTH_LINKEDIN_SECRET = 'VOaF1eUDOlHziUTn'
# Linkedin APP Scope
SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress',]
SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = [
    'email-address',
    'picture-urls::(original)',
    'first-name',
    'last-name',
    'email-address',
    'picture-url',
]
SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [
    ('id', 'id'),
    ('firstName', 'first_name'),
    ('lastName', 'last_name'),
    ('emailAddress', 'email_address'),
    ('public-profile-url', 'public_profile_url'),
]

# Twitter APP Key
SOCIAL_AUTH_TWITTER_KEY = 'LIK43CXqkCJjEDKmP4LsqPLD7'
# Twitter APP Secret
SOCIAL_AUTH_TWITTER_SECRET = 'BpK70KSeb3RePk6WXoFumG6jMV2sRLY623hzpkHVdXr85eq7sD'

# Google APP Key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '90947248109-nvu6v5d6rvpav60ps1sgrtplt5vlinhp.apps.googleusercontent.com'
# Google APP Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '4I7fFTTrlVfoHLbPNn6lviCK'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.linkedin.LinkedinOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GooglePlusAuth',
    #'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login'
SOCIAL_AUTH_USER_MODEL = 'core.User'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = [ 'email' ]
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_SLUGIFY_USERNAMES = False
#SOCIAL_AUTH_URL_NAMESPACE = 'social'

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
    'social.pipeline.user.user_details',
    'wannamigrate.core.social_auth_pipelines.save_extra_data',
)





#########################################
# DJANGO APPS REQUIRED
#########################################
# Application definition
DEFAULT_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
)
THIRD_PARTY_APPS = (
    'social.apps.django_app.default',
    'stdimage',
)
LOCAL_APPS = (
    'wannamigrate.core',
    'wannamigrate.admin',
    'wannamigrate.site',
    'wannamigrate.points',
    'wannamigrate.marketplace',
    'wannamigrate.qa',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS





#########################################
# GeoIP SETTINGS (https://docs.djangoproject.com/en/1.7/ref/contrib/gis/geoip/#std:setting-GEOIP_PATH)
#########################################
GEOIP_PATH = os.path.join( BASE_DIR, '..', 'wannamigrate', '_settings', 'geo_ip' )
GEOIP_COUNTRY = 'GeoIP.dat'





#########################################
# IMMIGRATION POINTS SETTINGS
#########################################

# Database IDs for countries with immigration enabled
ID_COUNTRY_BRAZIL = 242
ID_COUNTRY_AUSTRALIA = 117
ID_COUNTRY_NEW_ZEALAND = 131
ID_COUNTRY_CANADA = 204
ID_COUNTRY_UNITED_STATES = 235

# Database IDs for languages that are worth immigration points
ID_LANGUAGE_ENGLISH = 34
ID_LANGUAGE_FRENCH = 42

# Database IDs of questions used on code
ID_QUESTION_FAMILY_OVERSEAS = 1
ID_QUESTION_AGE = 2
ID_QUESTION_ENGLISH = 3
ID_QUESTION_FRENCH = 4
ID_QUESTION_EDUCATION_DEGREE = 5
ID_QUESTION_WORK_OFFER = 6
ID_QUESTION_WORK_EXPERIENCE_OUTSIDE = 7
ID_QUESTION_WORK_EXPERIENCE_INSIDE = 8
ID_QUESTION_SKILLED_PARTNER = 10
ID_QUESTION_INVEST = 11
ID_QUESTION_STARTUP_LETTER = 12
ID_QUESTION_US_CITIZEN = 13
ID_QUESTION_STUDY_REGIONAL_AU = 14
ID_QUESTION_PROFESSIONAL_YEAR_AU = 15
ID_QUESTION_LIVE_REGIONAL_AU = 16
ID_QUESTION_PARTNER_WORKED_STUDIED_CA = 18
ID_QUESTION_PARTNER_ENGLISH = 19
ID_QUESTION_PARTNER_FRENCH = 20
ID_QUESTION_PARTNER_EDUCATION_DEGREE = 21
ID_QUESTION_LANGUAGE_LEVEL_OTHERS = 22
ID_QUESTION_PAST_STUDY_COUNTRY_DESTINATION = 23
ID_QUESTION_WORK_EXPERIENCE_TOTAL = 24

# Map between language levels (IDs for the same language levels as question "General Language Level".
ID_ENGLISH_LEVEL_MAP = {
    912: 93,
    913: 94,
    914: 95,
    915: 96
}
ID_FRENCH_LEVEL_MAP = {
    912: 97,
    913: 98,
    914: 99,
    915: 100
}

# Australian community Language IDS (countries listed in http://www.naati.com.au/PDF/Booklets/NAATI_Recognition_booklet.pdf)
ID_AUSTRALIAN_COMMUNITY_LANGUAGES = [
    4, 5, 6, 8, 163, 164, 165, 166, 19, 20, 167, 26, 28, 29, 168, 169, 32,
    170, 40, 42, 49, 50, 171, 172, 58, 59, 64, 70, 71, 173, 81, 174, 89, 91,
    175, 93, 99, 176, 177, 178, 106, 107, 108, 179, 111, 112, 114, 117, 124,
    126, 128, 129, 180, 137, 181, 140, 142, 182, 145, 149, 150, 153
]

# IDs for user result status
ID_RESULT_STATUS_ALLOWED = 1
ID_RESULT_STATUS_DENIED_POINTS = 2
ID_RESULT_STATUS_DENIED_OCCUPATION = 3
ID_RESULT_STATUS_DENIED_AGE = 4
ID_RESULT_STATUS_DENIED_LANGUAGE = 5
ID_RESULT_STATUS_DENIED_WORK_EXPERIENCE = 6

# Minimum language levels
ID_MINIMUM_ENGLISH_LEVEL = 94
ID_MINIMUM_FRENCH_LEVEL = 98





#######################################
# Questions and Answers constants
#######################################
# The number of questions that should be loaded on each ajax load step.
QA_QUESTIONS_PER_STEP = 10

# IDs for post types
QA_POST_TYPE_ANSWER_ID = 1
QA_POST_TYPE_BLOGPOST_ID = 2
QA_POST_TYPE_COMMENT_ID = 3
QA_POST_TYPE_QUESTION_ID = 4

# IDs for vote types
QA_VOTE_TYPE_UPVOTE_ID = 1
QA_VOTE_TYPE_DOWNVOTE_ID = 2
QA_VOTE_TYPE_REPORT_ID = 3






###########################
# Global constants
###########################
DEFAULT_LISTING_ITEMS_PER_PAGE = 15





#######################################
# Payment Settings
#######################################

# Payment API (Iugu) settings
PAYMENT_API_MODE = 'LIVE' # 'TEST' or 'LIVE'
PAYMENT_API_ACCOUNT_ID = 'd8e362b4-c5d1-4d69-a3f6-ab9dbb4a046d'
PAYMENT_API_KEY_TEST = '8fac43a9239524b3724fb55607acbde3'
PAYMENT_API_KEY_LIVE = 'c98052235240700fc5c07f2cffab443a'
PAYMENT_API_BASE_URL = 'https://api.iugu.com/v1/'

# Database IDs for order statuses
ID_ORDER_STATUS_PENDING = 1
ID_ORDER_STATUS_APPROVED = 2
ID_ORDER_STATUS_DENIED = 3
ID_ORDER_STATUS_CANCELLED = 4
ID_ORDER_STATUS_REFUNDED = 5

# Database IDs for service statuses
ID_SERVICE_STATUS_PENDING = 1
ID_SERVICE_STATUS_STARTED = 2
ID_SERVICE_STATUS_COMPLETED = 3
ID_SERVICE_STATUS_CANCELLED = 4





#######################################
# Messages settings
#######################################
# The number of questions that should be loaded on each ajax load step.
CORE_CONVERSATION_STATUS_INBOX_ID = 1
CORE_CONVERSATION_STATUS_OUTBOX_ID = 2
CORE_CONVERSATION_STATUS_ARCHIVE_ID = 3
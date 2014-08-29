"""
Django settings for wannamigrate_new project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.utils.translation import ugettext_lazy as _
import os
import pymysql
pymysql.install_as_MySQLdb()

# Base directory path
BASE_DIR = os.path.dirname( os.path.dirname( __file__ ) )

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&3je*i!yr=4y3sk&sm7^_@(fhd@^z7re&$y-b-wx(zsm3(6nyk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#DEBUG_TOOLBAR_PATCH_SETTINGS = False

TEMPLATE_DEBUG = True

# Access Restrictions
ALLOWED_HOSTS = []

INTERNAL_IPS = (
    '127.0.0.1'
)

# Application definition
DEFAULT_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
)
THIRD_PARTY_APPS = (
    #'debug_toolbar'
)
LOCAL_APPS = (
    'wannamigrate.core',
    'wannamigrate.admin'
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'wannamigrate.urls'

WSGI_APPLICATION = 'wannamigrate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #'ENGINE': 'mysql.connector.django',
        'NAME': 'wannamigrate',
        'USER': 'wannamigrate',
        'PASSWORD': '4tiq3PAwFjnBsdZ91',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ( 'en-us', _( 'English' ) ),
    ( 'pt-br', _( 'Portuguese (BR)' ) ),
)

LOCALE_PATHS = (
    os.path.join( BASE_DIR, 'locale' ),
)


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join( BASE_DIR, 'static' )

# Templates
TEMPLATE_DIRS = (
    os.path.join( BASE_DIR, 'templates' ),
)

# User Model
AUTH_USER_MODEL = 'core.User'

# Login URL
LOGIN_URL = 'admin:login'

# Email Settings
DEFAULT_FROM_EMAIL = 'Wanna Migrate <contact@wannamigrate.com>'
EMAIL_HOST = 'smtp.wannamigrate.com'
EMAIL_HOST_USER = 'contact@wannamigrate.com'
EMAIL_HOST_PASSWORD = 'ju829sj'
EMAIL_PORT = 587
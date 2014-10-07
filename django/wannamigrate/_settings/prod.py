"""
PRODUCTION SETTINGS
"""

# -*- coding: utf-8 -*-

from wannamigrate._settings.base import *



#########################################
# DEBUG SETTINGS
#########################################
DEBUG = False

TEMPLATE_DEBUG = False


#########################################
# ACCESS RESTRICTIONS
#########################################
ALLOWED_HOSTS = []

INTERNAL_IPS = (
    '127.0.0.1',
)

#########################################
# DATABASES
#########################################
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'wannamigrate',
        'USER': 'wannamigrate',
        'PASSWORD': '4tiq3PAwFjnBsdZ91',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}



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
)
LOCAL_APPS = (
    'wannamigrate.core',
    'wannamigrate.admin',
    'wannamigrate.landing_page',
    'wannamigrate.site'
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
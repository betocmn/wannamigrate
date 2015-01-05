"""
PRODUCTION SETTINGS
"""

# -*- coding: utf-8 -*-

from wannamigrate._settings.base import *


#########################################
# URLs
#########################################
BASE_URL = 'http://www.wannamigrate.com'
BASE_URL_SECURE = 'http://www.wannamigrate.com'
EMAIL_LOGO_URL = 'http://www.wannamigrate.com/static/admin/img/logo.png'


#########################################
# DEBUG SETTINGS
#########################################
DEBUG = False

TEMPLATE_DEBUG = False


#########################################
# ACCESS RESTRICTIONS
#########################################
ALLOWED_HOSTS = [
    "54.148.167.28",
    ".compute.amazonaws.com",
    ".wannamigrate.com"
]

INTERNAL_IPS = (
    '127.0.0.1',
    '191.189.139.194',
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

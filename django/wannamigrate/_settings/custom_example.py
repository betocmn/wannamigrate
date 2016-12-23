# -*- coding: utf-8 -*-
"""
PROD SETTINGS

This settings will overwrite the base settings when in PROD environment
"""

##########################
# Imports
##########################
from wannamigrate._settings.base import *





#########################################
# URLs
#########################################
BASE_URL = 'https://www.wannamigrate.com'
BASE_URL_SECURE = 'https://www.wannamigrate.com'





#########################################
# DEBUG AND ENVIRONMENT SETTINGS
#########################################
IS_PROD = True
DEBUG = False
SQL_DEBUG = False
TEMPLATE_DEBUG = False





#########################################
# ACCESS RESTRICTIONS
#########################################
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "www.wannamigrate.com",
    "wannamigrate.com",
    "pt.wannamigrate.com",
    "54.233.70.76",
    "103.55.92.26"
]

INTERNAL_IPS = (
    "localhost",
    "127.0.0.1",
    "110.174.143.148",
    "103.55.92.26"
)





#########################################
# DATABASES
#########################################
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'wannamigrate',
        'USER': 'wannamigrate',
        'PASSWORD': 'z992ush6dh2y36HAj328aaKW',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

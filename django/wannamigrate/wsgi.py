"""
WSGI config for wannamigrate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

#SSL
os.environ[ 'HTTPS' ] = "on"

# We check if there' a local settings file, if so, we are in dev
BASE_DIR = os.path.dirname( __file__ )
settings_file_path = os.path.join( BASE_DIR, '_settings', 'local.py' )

# check if file exists
if os.path.isfile( settings_file_path ):
    settings_file = 'wannamigrate._settings.local'
else:
    settings_file = 'wannamigrate._settings.prod'

# Set the correct settings file to django
os.environ.setdefault( "DJANGO_SETTINGS_MODULE", settings_file )

# Start django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

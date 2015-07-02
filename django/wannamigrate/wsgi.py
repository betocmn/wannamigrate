"""
WSGI config for wannamigrate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

##########################
# Imports
##########################
import os




##########################
# Project's WSGI Config
##########################

#SSL
os.environ[ 'HTTPS' ] = "on"

# Set the correct settings file to django
os.environ.setdefault( "DJANGO_SETTINGS_MODULE", 'wannamigrate._settings.custom' )

# Start django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

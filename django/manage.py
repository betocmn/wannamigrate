#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    # We check if there' a local settings file, if so, we are in dev
    BASE_DIR = os.path.dirname( __file__ )
    settings_file_path = os.path.join( BASE_DIR, 'wannamigrate', '_settings', 'local.py' )
    if os.path.isfile( settings_file_path ):
        settings_file = 'wannamigrate._settings.local'
    else:
        settings_file = 'wannamigrate._settings.prod'


    # Set Settings file
    os.environ.setdefault( "DJANGO_SETTINGS_MODULE", settings_file )


    # Execute from command line
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

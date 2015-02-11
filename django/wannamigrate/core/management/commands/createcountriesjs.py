"""
This class will get Database content that
needs to be translated and create an html template
file with it.

We do this so that django's translation system recognizes
those strings for later translations.
"""

##########################
# Imports
##########################
from django.core.management.base import BaseCommand, CommandError
from wannamigrate.core.models import Country
from django.core.files import File
from django.conf import settings
import os





##########################
# Classes definitions
##########################
class Command( BaseCommand ):

    args = ''
    help = 'Creates javascript file with map of ids and codes'

    def handle( self, *args, **options ):

        # grab values from the db table and build the content
        file_content = '/* Map of database IDs with country codes to be used by the jquery plugin */\n\n'
        file_content += 'var COUNTRIES_PER_ID = Array();\n\n'
        countries = Country.objects.all()
        for country in countries:
            file_content += "COUNTRIES_PER_ID["+ str( country.id ) +"] = '"+ str( country.code.lower() ) +"';"
            file_content += '\n'

        # creates new file and writes the db content
        file_name = os.path.join( settings.BASE_DIR, '..', 'static', 'site', 'js', 'countries.js' )
        with open( file_name, 'w' ) as f:
            js_file = File( f )
            js_file.write( file_content )

        # Return Success message
        self.stdout.write( 'File(s) successfully created' )
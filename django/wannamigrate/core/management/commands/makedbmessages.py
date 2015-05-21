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
from wannamigrate.core.models import Country, Language, Goal
from wannamigrate.points.models import Answer, Occupation, OccupationCategory
from wannamigrate.qa.models import Topic
from wannamigrate.marketplace.models import ServiceType, ServiceTypeCategory
from django.core.files import File
from django.conf import settings
import os





##########################
# Classes definitions
##########################
class Command( BaseCommand ):

    args = '<table_name table_name ...>'
    help = 'Dumps database table values into templates/db_translations'

    def handle( self, *args, **options ):

        for table_name in args:

            # Instatiates model to be used (based on table name)
            if table_name == 'core_country':
                model = Country
                possible_fields = [ 'name' ]
            elif table_name == 'core_language':
                model = Language
                possible_fields = [ 'name' ]
            elif table_name == 'core_answer':
                model = Answer
                possible_fields = [ 'description' ]
            elif table_name == 'core_goal':
                model = Goal
                possible_fields = [ 'name' ]
            elif table_name == 'marketplace_servicetype':
                model = ServiceType
                possible_fields = [ 'name', 'description' ]
            elif table_name == 'marketplace_servicetypecategory':
                model = ServiceTypeCategory
                possible_fields = [ 'name' ]
            elif table_name == 'points_occupation':
                model = Occupation
                possible_fields = [ 'name' ]
            elif table_name == 'points_occupationcategory':
                model = OccupationCategory
                possible_fields = [ 'name' ]
            elif table_name == 'qa_topic':
                model = Topic
                possible_fields = [ 'name' ]
            else:
                raise CommandError( 'Table does not need translations or do not exist' )

            # grab values from the db table and build the content
            file_content = '{% load i18n %}\n'
            results = model.objects.all()
            for result in results:
                for possible_field in possible_fields:
                    #file_content += getattr( result, possible_field ) + ' '
                    file_content += '{% trans "' + getattr( result, possible_field ) + '" %} '
                file_content += '\n'

            # creates new file and writes the db content
            file_name = os.path.join( settings.BASE_DIR, '..', 'templates', 'db_translations', table_name + '.html' )
            with open( file_name, 'w' ) as f:
                template_file = File( f )
                template_file.write( file_content )

            # Return Success message
            self.stdout.write( 'File(s) successfully created' )
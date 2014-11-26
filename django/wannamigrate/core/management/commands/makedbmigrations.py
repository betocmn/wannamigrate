from django.core.management.base import BaseCommand, CommandError
from wannamigrate.core.models import Question, Answer
from django.core.files import File
from django.conf import settings
import os

class Command( BaseCommand ):

    args = '<>'
    help = 'Dumps database table values into data migration file'

    def handle( self, *args, **options ):


        # Instantiates model to be used (based on table name)


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
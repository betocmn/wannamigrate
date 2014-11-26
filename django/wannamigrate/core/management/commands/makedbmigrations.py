from django.core.management.base import BaseCommand, CommandError
from wannamigrate.core.models import Question, Answer, CountryPoints, OccupationCategory, Occupation
from django.core.files import File
from django.conf import settings
import os

class Command( BaseCommand ):

    args = '<>'
    help = 'Dumps database table values into data migration file'

    def handle( self, *args, **options ):


        # Questions
        questions = Question.objects.all()
        file_content = '#Questions'
        for question in questions:

            file_content += """
    question = Question()
    question.id = %s
    question.description = '%s'
    question.help_text = '%s'
    question.modified_date = '%s'
    question.created_date = '%s'
    question.save()
            """ % ( question.id, question.description, question.help_text, question.modified_date, question.created_date )
            
        
        # Answers
        answers = Answer.objects.all()
        file_content += '\n#Answers'
        for answer in answers:

            file_content += """
    answer = Answer()
    answer.id = %s
    answer.description = '%s'
    answer.question_id = %s
    answer.modified_date = '%s'
    answer.created_date = '%s'
    answer.save()
            """ % ( answer.id, answer.description, answer.question.id, answer.modified_date, answer.created_date )


        # CountryPoints
        country_points_results = CountryPoints.objects.all()
        file_content += '\n#CountryPointss'
        for country_points in country_points_results:

            file_content += """
    country_points = CountryPoints()
    country_points.id = %s
    country_points.points = %s
    country_points.answer_id = %s
    country_points.country_id = %s
    country_points.modified_date = '%s'
    country_points.created_date = '%s'
    country_points.save()
            """ % ( country_points.id, country_points.points, country_points.answer.id, country_points.country.id, country_points.modified_date, country_points.created_date )



        # OccupationCategory
        occupation_category_results = OccupationCategory.objects.all()
        file_content += '\n#OccupationCategory'
        for occupation_category in occupation_category_results:

            file_content += """
    occupation_category = OccupationCategory()
    occupation_category.id = %s
    occupation_category.name = '%s'
    occupation_category.modified_date = '%s'
    occupation_category.created_date = '%s'
    occupation_category.save()
            """ % ( occupation_category.id, occupation_category.name, occupation_category.modified_date, occupation_category.created_date )

        
        # Occupation
        occupation_results = Occupation.objects.all()
        file_content += '\n#Occupation'
        for occupation in occupation_results:

            file_content += """
    occupation = Occupation()
    occupation.id = %s
    occupation.name = '%s'
    occupation.occupation_category_id = %s
    occupation.modified_date = '%s'
    occupation.created_date = '%s'
    occupation.save()
            """ % ( occupation.id, occupation.name, occupation.occupation_category.id, occupation.modified_date, occupation.created_date )

            for country in occupation.countries.all():
                file_content += """
    occupation.countries.add( %s )
            """ % ( country.id )



        # creates new file and writes the db content
        file_name = os.path.join( settings.BASE_DIR, '..', 'templates', 'db_translations', 'temp_questions.html' )
        with open( file_name, 'w' ) as f:
            template_file = File( f )
            template_file.write( file_content )    


        # Return Success message
        self.stdout.write( 'File(s) successfully created' )
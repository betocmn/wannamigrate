# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# USER RESULT STATUS
#######################
def core_question_addition_values( apps, schema_editor ):

    # Get model to use (historical version)
    Question = apps.get_model( "core", "Question" )


    question = Question.objects.get( pk = 1 )
    question.method_name = 'get_family_overseas_points'
    question.type = 'personal'
    question.save()

    question = Question.objects.get( pk = 2 )
    question.method_name = 'get_age_points'
    question.type = 'personal'
    question.save()

    question = Question.objects.get( pk = 3 )
    question.method_name = 'get_english_points'
    question.type = 'language'
    question.save()

    question = Question.objects.get( pk = 4 )
    question.method_name = 'get_french_points'
    question.type = 'language'
    question.save()

    question = Question.objects.get( pk = 5 )
    question.method_name = 'get_education_degree_points'
    question.type = 'education'
    question.save()

    question = Question.objects.get( pk = 6 )
    question.method_name = 'get_work_offer_points'
    question.type = 'work'
    question.save()

    question = Question.objects.get( pk = 7 )
    question.method_name = 'get_work_experience_outside_points'
    question.type = 'work'
    question.save()

    question = Question.objects.get( pk = 8 )
    question.method_name = 'get_work_experience_inside_points'
    question.type = 'work'
    question.save()

    question = Question.objects.get( pk = 24 )
    question.method_name = 'get_work_experience_total_points'
    question.type = 'work'
    question.save()

    question = Question.objects.get( pk = 10 )
    question.method_name = 'get_skilled_partner_points'
    question.type = 'work'
    question.save()

    question = Question.objects.get( pk = 11 )
    question.method_name = 'get_invest_points'
    question.type = 'work'
    question.save()

    question = Question.objects.get( pk = 12 )
    question.method_name = 'get_startup_letter_points'
    question.type = 'work'
    question.save()

    question = Question.objects.get( pk = 13 )
    question.method_name = 'get_us_citizen_points'
    question.type = 'personal'
    question.save()

    question = Question.objects.get( pk = 14 )
    question.method_name = 'get_study_regional_au_points'
    question.type = 'education'
    question.save()

    question = Question.objects.get( pk = 15 )
    question.method_name = 'get_professional_year_au_points'
    question.type = 'education'
    question.save()

    question = Question.objects.get( pk = 16 )
    question.method_name = 'get_live_regional_au_points'
    question.type = 'personal'
    question.save()

    question = Question.objects.get( pk = 18 )
    question.method_name = 'get_partner_worked_studied_ca_points'
    question.type = 'work'
    question.save()

    question = Question.objects.get( pk = 19 )
    question.method_name = 'get_partner_english_points'
    question.type = 'language'
    question.save()

    question = Question.objects.get( pk = 20 )
    question.method_name = 'get_partner_french_points'
    question.type = 'language'
    question.save()

    question = Question.objects.get( pk = 21 )
    question.method_name = 'get_partner_education_degree_points'
    question.type = 'education'
    question.save()

    question = Question.objects.get( pk = 22 )
    question.method_name = 'get_language_level_others_points'
    question.type = 'language'
    question.save()

    question = Question.objects.get( pk = 23 )
    question.method_name = 'get_past_study_country_destination_points'
    question.type = 'education'
    question.save()





#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_auto_20141222_2134'),
    ]

    operations = [
        migrations.RunPython( core_question_addition_values ),
    ]

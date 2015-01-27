# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# USER RESULT STATUS
#######################
def points_user_result_status_values( apps, schema_editor ):

    # Get model to use (historical version)
    UserResultStatus = apps.get_model( "points", "UserResultStatus" )


    user_result_status = UserResultStatus()
    user_result_status.id = 1
    user_result_status.name = 'Allowed (Enough points)'
    user_result_status.save()

    user_result_status = UserResultStatus()
    user_result_status.id = 2
    user_result_status.name = 'Denied (Not enough points)'
    user_result_status.save()

    user_result_status = UserResultStatus()
    user_result_status.id = 3
    user_result_status.name = 'Denied (Occupation not in demand'
    user_result_status.save()

    user_result_status = UserResultStatus()
    user_result_status.id = 4
    user_result_status.name = 'Denied (Age not allowed)'
    user_result_status.save()

    user_result_status = UserResultStatus()
    user_result_status.id = 5
    user_result_status.name = 'Denied (Insufficient language level)'
    user_result_status.save()

    user_result_status = UserResultStatus()
    user_result_status.id = 6
    user_result_status.name = 'Denied (Insufficient work experience)'
    user_result_status.save()

#######################
# USER RESULT STATUS
#######################
def points_question_addition_values( apps, schema_editor ):

    # Get model to use (historical version)
    Question = apps.get_model( "points", "Question" )


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
# QUESTIONS
#######################
def points_add_country_config_values( apps, schema_editor ):

    # Get model to use (historical version)
    Country = apps.get_model( "core", "Country" )
    CountryConfig = apps.get_model( "points", "CountryConfig" )


    # Australia
    country_config = CountryConfig()
    country_config.id = 1
    country_config.country = Country.objects.get( pk = 117 )
    country_config.pass_mark_points = 60
    country_config.max_personal_points = 40
    country_config.max_language_points = 25
    country_config.max_education_points = 30
    country_config.max_work_points = 40
    country_config.max_total_points = 135
    country_config.save()

    # Canada
    country_config = CountryConfig()
    country_config.id = 2
    country_config.country = Country.objects.get( pk = 204 )
    country_config.pass_mark_points = 67
    country_config.max_personal_points = 17
    country_config.max_language_points = 33
    country_config.max_education_points = 30
    country_config.max_work_points = 35
    country_config.max_total_points = 115
    country_config.save()

    # New Zealand
    country_config = CountryConfig()
    country_config.id = 3
    country_config.country = Country.objects.get( pk = 131 )
    country_config.pass_mark_points = 100
    country_config.max_personal_points = 40
    country_config.max_language_points = 0
    country_config.max_education_points = 115
    country_config.max_work_points = 45
    country_config.max_total_points = 200
    country_config.save()

#######################
# QUESTION GROUPS
#######################
def points_add_question_groups_values( apps, schema_editor ):

    # Get model to use (historical version)
    QuestionGroup = apps.get_model( "points", "QuestionGroup" )
    Country = apps.get_model( "core", "Country" )
    Question = apps.get_model( "points", "Question" )

    # Australia
    question_group = QuestionGroup()
    question_group.id = 1
    question_group.country = Country.objects.get( pk = 117 )
    question_group.name = 'Total Experience'
    question_group.max_points = 20
    question_group.save()
    question_group.questions.add( Question.objects.get( pk = 7 ) )
    question_group.questions.add( Question.objects.get( pk = 8 ) )

    # Canada
    question_group = QuestionGroup()
    question_group.id = 2
    question_group.country = Country.objects.get( pk = 204 )
    question_group.name = 'Total Language'
    question_group.max_points = 28
    question_group.save()
    question_group.questions.add( Question.objects.get( pk = 3 ) )
    question_group.questions.add( Question.objects.get( pk = 4 ) )

    question_group = QuestionGroup()
    question_group.id = 3
    question_group.country = Country.objects.get( pk = 204 )
    question_group.name = 'Total Bonus'
    question_group.max_points = 10
    question_group.save()
    question_group.questions.add( Question.objects.get( pk = 1 ) )
    question_group.questions.add( Question.objects.get( pk = 8 ) )
    question_group.questions.add( Question.objects.get( pk = 18 ) )
    question_group.questions.add( Question.objects.get( pk = 19 ) )
    question_group.questions.add( Question.objects.get( pk = 20 ) )
    question_group.questions.add( Question.objects.get( pk = 23 ) )




class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_auto_20150126_2221'),
    ]

    operations = [
        migrations.RunPython( points_user_result_status_values ),
        migrations.RunPython( points_question_addition_values ),
        migrations.RunPython( points_add_country_config_values ),
        migrations.RunPython( points_add_question_groups_values ),

    ]

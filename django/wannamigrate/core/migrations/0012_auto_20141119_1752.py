# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# QUESTIONS
#######################
def core_question_aditional_values( apps, schema_editor ):

    # Get model to use (historical version)
    Question = apps.get_model( "core", "Question" )

    # Insert data
    question = Question()
    question.id = 22
    question.description = 'What is your Language Level (Others)?'
    question.help_text = 'Users can add any other language and this is to store the level of it'
    question.save()



#######################
# ANSWERS
#######################
def core_answer_aditional_values( apps, schema_editor ):

    # Get model to use (historical version)
    Answer = apps.get_model( "core", "Answer" )
    Question = apps.get_model( "core", "Question" )
    AnswerCategory = apps.get_model( "core", "AnswerCategory" )


    answer = Answer()
    answer.id = 912
    answer.question = Question.objects.get( pk = 22 )
    answer.description = 'None'
    answer.save()

    answer = Answer()
    answer.id = 913
    answer.question = Question.objects.get( pk = 22 )
    answer.description = 'Basic Proficiency'
    answer.save()

    answer = Answer()
    answer.id = 914
    answer.question = Question.objects.get( pk = 22 )
    answer.description = 'Moderate Proficiency'
    answer.save()

    answer = Answer()
    answer.id = 915
    answer.question = Question.objects.get( pk = 22 )
    answer.description = 'High Proficiency'
    answer.save()


#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20141111_2137'),
    ]

    operations = [
        migrations.RunPython( core_question_aditional_values ),
        migrations.RunPython( core_answer_aditional_values ),
    ]

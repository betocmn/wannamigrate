# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# QUESTION GROUPS
#######################
def core_add_question_groups_values( apps, schema_editor ):

    # Get model to use (historical version)
    QuestionGroup = apps.get_model( "core", "QuestionGroup" )
    Country = apps.get_model( "core", "Country" )
    Question = apps.get_model( "core", "Question" )

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





#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_auto_20141223_1831'),
    ]

    operations = [
        migrations.RunPython( core_add_question_groups_values ),
    ]

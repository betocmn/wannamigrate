# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# QUESTIONS
#######################
def core_delete_question( apps, schema_editor ):

    # Get model to use (historical version)
    Question = apps.get_model( "core", "Question" )


    question = Question.objects.get( pk = 17 )
    question.delete()

    question = Question.objects.get( pk = 9 )
    question.delete()





#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20141222_2134'),
    ]

    operations = [
        migrations.RunPython( core_delete_question ),
    ]

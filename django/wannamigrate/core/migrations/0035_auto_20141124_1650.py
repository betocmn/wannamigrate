# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# QUESTIONS
#######################
def core_question_new_values( apps, schema_editor ):

    # Get model to use (historical version)
    Question = apps.get_model( "core", "Question" )

    question = Question()
    question.id = 23
    question.description = 'Did you complete any studies in country of destination?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 24
    question.description = 'How many years of experience in a skilled occupation anywhere (totals)?'
    question.help_text = ''
    question.save()



#######################
# ANSWERS
#######################
def core_answer_new_values( apps, schema_editor ):

    # Get model to use (historical version)
    Answer = apps.get_model( "core", "Answer" )
    Question = apps.get_model( "core", "Question" )

    # Insert data
    answer = Answer()
    answer.id = 916
    answer.question = Question.objects.get( pk = 23 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 917
    answer.question = Question.objects.get( pk = 23 )
    answer.description = 'No'
    answer.save()
    
    answer = Answer()
    answer.id = 918
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '1'
    answer.save()

    answer = Answer()
    answer.id = 919
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '2'
    answer.save()

    answer = Answer()
    answer.id = 920
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '3'
    answer.save()

    answer = Answer()
    answer.id = 921
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '4'
    answer.save()

    answer = Answer()
    answer.id = 922
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '5'
    answer.save()

    answer = Answer()
    answer.id = 923
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '6'
    answer.save()

    answer = Answer()
    answer.id = 924
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '7'
    answer.save()

    answer = Answer()
    answer.id = 925
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '8'
    answer.save()

    answer = Answer()
    answer.id = 926
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '9'
    answer.save()

    answer = Answer()
    answer.id = 927
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '10'
    answer.save()

    answer = Answer()
    answer.id = 928
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '11'
    answer.save()

    answer = Answer()
    answer.id = 929
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '12'
    answer.save()

    answer = Answer()
    answer.id = 930
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '13'
    answer.save()

    answer = Answer()
    answer.id = 931
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '14'
    answer.save()

    answer = Answer()
    answer.id = 932
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '15'
    answer.save()

    answer = Answer()
    answer.id = 933
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '16'
    answer.save()

    answer = Answer()
    answer.id = 934
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '17'
    answer.save()

    answer = Answer()
    answer.id = 935
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '18'
    answer.save()

    answer = Answer()
    answer.id = 936
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '19'
    answer.save()

    answer = Answer()
    answer.id = 937
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '20'
    answer.save()

    answer = Answer()
    answer.id = 938
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '21'
    answer.save()

    answer = Answer()
    answer.id = 939
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '22'
    answer.save()

    answer = Answer()
    answer.id = 940
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '23'
    answer.save()

    answer = Answer()
    answer.id = 941
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '24'
    answer.save()

    answer = Answer()
    answer.id = 942
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '25'
    answer.save()

    answer = Answer()
    answer.id = 943
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '26'
    answer.save()

    answer = Answer()
    answer.id = 944
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '27'
    answer.save()

    answer = Answer()
    answer.id = 945
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '28'
    answer.save()

    answer = Answer()
    answer.id = 946
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '29'
    answer.save()

    answer = Answer()
    answer.id = 947
    answer.question = Question.objects.get( pk = 24 )
    answer.description = '30'
    answer.save()


#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_userstats_updating_now'),
    ]

    operations = [
         migrations.RunPython( core_question_new_values ),
         migrations.RunPython( core_answer_new_values ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.db import connection


#######################
# ACTIONS
#######################
def rename_question_tables( apps, schema_editor ):

    cursor = connection.cursor()

    cursor.execute( "RENAME TABLE points_question TO points_question_old" )
    cursor.execute( "RENAME TABLE points_questiongroup TO points_questiongroup_old" )
    cursor.execute( "RENAME TABLE points_questiongroup_questions TO points_questiongroup_questions_old" )

    cursor.execute( "RENAME TABLE core_question TO points_question" )
    cursor.execute( "RENAME TABLE core_questiongroup TO points_questiongroup" )
    cursor.execute( "RENAME TABLE core_questiongroup_questions TO points_questiongroup_questions" )

    cursor.execute( "RENAME TABLE points_question_old TO core_question" )
    cursor.execute( "RENAME TABLE points_questiongroup_old TO core_questiongroup" )
    cursor.execute( "RENAME TABLE points_questiongroup_questions_old TO core_questiongroup_questions" )


#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('points', '0004_question_questiongroup'),
    ]

    operations = [
        migrations.RunPython( rename_question_tables ),
    ]

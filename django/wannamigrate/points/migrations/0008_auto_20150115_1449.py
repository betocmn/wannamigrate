# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.db import connection


#######################
# ACTIONS
#######################
def rename_answer_tables( apps, schema_editor ):

    cursor = connection.cursor()

    cursor.execute( "RENAME TABLE points_answer TO points_answer_old" )
    cursor.execute( "RENAME TABLE points_countryconfig TO points_countryconfig_old" )
    cursor.execute( "RENAME TABLE points_countrypoints TO points_countrypoints_old" )

    cursor.execute( "RENAME TABLE core_answer TO points_answer" )
    cursor.execute( "RENAME TABLE core_countryconfig TO points_countryconfig" )
    cursor.execute( "RENAME TABLE core_countrypoints TO points_countrypoints" )

    cursor.execute( "RENAME TABLE points_answer_old TO core_answer" )
    cursor.execute( "RENAME TABLE points_countryconfig_old TO core_countryconfig" )
    cursor.execute( "RENAME TABLE points_countrypoints_old TO core_countrypoints" )


#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('points', '0007_auto_20150115_1449'),
    ]

    operations = [
        migrations.RunPython( rename_answer_tables ),
    ]

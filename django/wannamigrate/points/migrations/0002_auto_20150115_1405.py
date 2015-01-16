# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.db import connection


#######################
# ACTIONS
#######################
def rename_occupation_tables( apps, schema_editor ):

    cursor = connection.cursor()

    cursor.execute( "RENAME TABLE points_occupationcategory TO points_occupationcategory_old" )
    cursor.execute( "RENAME TABLE points_occupation TO points_occupation_old" )
    cursor.execute( "RENAME TABLE points_occupation_countries TO points_occupation_countries_old" )

    cursor.execute( "RENAME TABLE core_occupationcategory TO points_occupationcategory" )
    cursor.execute( "RENAME TABLE core_occupation TO points_occupation" )
    cursor.execute( "RENAME TABLE core_occupation_countries TO points_occupation_countries" )

    cursor.execute( "RENAME TABLE points_occupationcategory_old TO core_occupationcategory" )
    cursor.execute( "RENAME TABLE points_occupation_old TO core_occupation" )
    cursor.execute( "RENAME TABLE points_occupation_countries_old TO core_occupation_countries" )


#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.RunPython( rename_occupation_tables ),
    ]

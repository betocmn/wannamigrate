# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.db import connection


#######################
# ACTIONS
#######################
def rename_user_result_tables( apps, schema_editor ):

    cursor = connection.cursor()

    cursor.execute( "RENAME TABLE points_userresultstatus TO points_userresultstatus_old" )
    cursor.execute( "RENAME TABLE points_userresult TO points_userresult_old" )

    cursor.execute( "RENAME TABLE core_userresultstatus TO points_userresultstatus" )
    cursor.execute( "RENAME TABLE core_userresult TO points_userresult" )

    cursor.execute( "RENAME TABLE points_userresultstatus_old TO core_userresultstatus" )
    cursor.execute( "RENAME TABLE points_userresult_old TO core_userresult" )


#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('points', '0010_auto_20150115_1506'),
    ]

    operations = [
        migrations.RunPython( rename_user_result_tables ),
    ]

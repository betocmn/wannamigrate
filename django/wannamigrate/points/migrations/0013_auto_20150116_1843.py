# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


from django.db import connection


#######################
# ACTIONS
#######################
def recalcuate_user_points( apps, schema_editor ):

    cursor = connection.cursor()

    cursor.execute( "UPDATE core_userstats SET updating_now = 1" )


#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('points', '0012_auto_20150115_1512'),
    ]

    operations = [
        migrations.RunPython( recalcuate_user_points ),
    ]

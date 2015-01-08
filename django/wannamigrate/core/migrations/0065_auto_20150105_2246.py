# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from datetime import datetime

#######################
# USER RESULT STATUS
#######################
def core_user_result_status_edited_values( apps, schema_editor ):

    # Get model to use (historical version)
    UserResultStatus = apps.get_model( "core", "UserResultStatus" )


    UserResultStatus.objects.update_or_create(
        pk = 3, defaults = { 'name': 'Denied (Occupation not in demand)' }
    )

    UserResultStatus.objects.update_or_create(
        pk = 4, defaults = { 'name': 'Denied (Age not allowed)' }
    )

    UserResultStatus.objects.update_or_create(
        pk = 5, defaults = { 'name': 'Denied (Insufficient language level)' }
    )

    user_result_status = UserResultStatus()
    user_result_status.id = 6
    user_result_status.name = 'Denied (Insufficient work experience)'
    user_result_status.save()


#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0064_auto_20141223_1855'),
    ]

    operations = [
        migrations.RunPython( core_user_result_status_edited_values ),
    ]

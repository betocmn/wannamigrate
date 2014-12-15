# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# USER RESULT STATUS
#######################
def core_user_result_status_values( apps, schema_editor ):

    # Get model to use (historical version)
    UserResultStatus = apps.get_model( "core", "UserResultStatus" )


    user_result_status = UserResultStatus()
    user_result_status.id = 1
    user_result_status.name = 'Allowed (Enough points)'
    user_result_status.save()

    user_result_status = UserResultStatus()
    user_result_status.id = 2
    user_result_status.name = 'Denied (Not enough points)'
    user_result_status.save()

    user_result_status = UserResultStatus()
    user_result_status.id = 3
    user_result_status.name = 'Denied (Enough points but occupation not in demand)'
    user_result_status.save()

    user_result_status = UserResultStatus()
    user_result_status.id = 4
    user_result_status.name = 'Denied (Enough points but age not allowed)'
    user_result_status.save()

    user_result_status = UserResultStatus()
    user_result_status.id = 5
    user_result_status.name = 'Denied (Enough points but insufficient language level)'
    user_result_status.save()



#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_userresultstatus'),
    ]

    operations = [
         migrations.RunPython( core_user_result_status_values ),
    ]

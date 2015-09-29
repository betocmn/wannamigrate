# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

#######################
# ACTIONS
#######################
def update_situations( apps, schema_editor ):

    # Get model to use (historical version)
    Situation = apps.get_model( "core", "Situation" )
    UserSituation = apps.get_model( "core", "UserSituation" )
    Goal = apps.get_model( "core", "Goal" )

    # Get all situation where goal is not live/work or study
    situations = Situation.objects.filter( goal_id__gt = 2 )
    if situations:
        for situation in situations:
            user_situations = UserSituation.objects.filter( situation_id = situation.id )
            if user_situations:
                for user_situation in user_situations:
                    user_situation.situation_id = 36
                    user_situation.save()

    # Deactivates goals not used anymore
    goal = Goal.objects.get( pk = 3 )
    goal.is_active = False
    goal.save()

    goal = Goal.objects.get( pk = 4 )
    goal.is_active = False
    goal.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20150721_1419'),
    ]

    operations = [
        migrations.RunPython( update_situations ),
    ]

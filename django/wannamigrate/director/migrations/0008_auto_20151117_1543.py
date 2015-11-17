# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

#######################
# ACTIONS
#######################
def fix_situation_mission( apps, schema_editor ):

    # Get model to use (historical version)
    SituationsMissions = apps.get_model( "director", "SituationsMissions" )
    Mission = apps.get_model( "director", "Mission" )

    # Gets goal_id and to_country_id and update situations_missions
    situatios_missions = SituationsMissions.objects.all()
    inserted = {}
    delete_ids = []
    for situation_mission in situatios_missions:
        situation = situation_mission.situation
        if situation.to_country_id in inserted \
                and situation.goal_id in inserted[situation.to_country_id] \
                and situation_mission.mission_id in inserted[situation.to_country_id][situation.goal_id]:
            delete_ids.append( situation_mission.id )
            continue
        inserted[situation.to_country_id] = {}
        inserted[situation.to_country_id][situation.goal_id] = {}
        inserted[situation.to_country_id][situation.goal_id][situation_mission.mission_id] = True
        mission = Mission.objects.get(pk=situation_mission.mission_id)
        mission.to_country_id = situation.to_country_id
        mission.goal_id = situation.goal_id
        mission.order = situation_mission.order
        mission.save()

    # Remove duplicates
    SituationsMissions.objects.filter( id__in = delete_ids ).delete()



class Migration(migrations.Migration):

    dependencies = [
        ('director', '0007_auto_20151117_1542'),
    ]

    operations = [
        migrations.RunPython( fix_situation_mission ),
    ]

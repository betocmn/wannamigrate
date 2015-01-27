# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations




#######################
# ACTIONS
#######################
def core_goals_values( apps, schema_editor ):

    # Get model to use (historical version)
    Goal = apps.get_model( "core", "Goal" )

    # Insert data
    goal = Goal()
    goal.id = 1
    goal.name = 'live and work permanently'
    goal.is_active = True
    goal.save()

    goal = Goal()
    goal.id = 2
    goal.name = 'live and work temporarily'
    goal.is_active = True
    goal.save()

    goal = Goal()
    goal.id = 3
    goal.name = 'study foreign language'
    goal.is_active = True
    goal.save()

    goal = Goal()
    goal.id = 4
    goal.name = 'study professional related course'
    goal.is_active = True
    goal.save()

    goal = Goal()
    goal.id = 5
    goal.name = 'be an exchange student'
    goal.is_active = True
    goal.save()

    goal = Goal()
    goal.id = 6
    goal.name = 'invest or create a business in'
    goal.is_active = True
    goal.save()

    goal = Goal()
    goal.id = 7
    goal.name = 'travel and be a visitor in'
    goal.is_active = False
    goal.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150126_2211'),
    ]

    operations = [
        migrations.RunPython( core_goals_values ),
    ]

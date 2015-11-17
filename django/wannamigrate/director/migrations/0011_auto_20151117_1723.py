# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid

#######################
# ACTIONS
#######################
def fix_objective_hashes( apps, schema_editor ):

    # Get model to use (historical version)
    Objective = apps.get_model( "director", "Objective" )

    objectives = Objective.objects.filter( hash = '' )
    for objective in objectives:
        objective.hash = uuid.uuid1().hex
        objective.save()

class Migration(migrations.Migration):

    dependencies = [
        ('director', '0010_auto_20151117_1611'),
    ]

    operations = [
        migrations.RunPython( fix_objective_hashes ),
    ]

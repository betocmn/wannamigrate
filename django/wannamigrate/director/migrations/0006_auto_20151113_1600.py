# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def update_data( apps, schema_editor ):

    # Get model to use (historical version)
    Objective = apps.get_model( "director", "Objective" )

    # Fixes some information
    lock_objectives_ids = [ 4,41,7,25,44,62 ]
    Objective.objects.filter( id__in = lock_objectives_ids ).update( is_public = False )

class Migration(migrations.Migration):

    dependencies = [
        ('director', '0005_auto_20151113_1517'),
    ]

    operations = [
        migrations.RunPython( update_data ),
    ]

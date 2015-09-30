# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations




def unlock_objectives( apps, schema_editor ):

    Objective = apps.get_model( "director", "Objective" )

    unlock_objectives_ids = [ 1, 3, 40, 21, 38, 58 ]
    Objective.objects.filter( id__in = unlock_objectives_ids ).update( is_public = True )



class Migration(migrations.Migration):

    dependencies = [
        ('director', '0003_objective_is_public'),
    ]

    operations = [
        migrations.RunPython( unlock_objectives )
    ]

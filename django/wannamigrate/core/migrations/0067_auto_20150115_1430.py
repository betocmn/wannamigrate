# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_auto_20150115_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupation',
            name='countries',
        ),
        migrations.RemoveField(
            model_name='occupation',
            name='occupation_category',
        ),
        migrations.DeleteModel(
            name='Occupation',
        ),
        migrations.DeleteModel(
            name='OccupationCategory',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20141120_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereducation',
            name='regional_australia_study',
            field=models.NullBooleanField(verbose_name='studied in regional part of australia', default=None, choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]

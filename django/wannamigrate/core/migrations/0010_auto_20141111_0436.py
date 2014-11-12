# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20141111_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonal',
            name='australian_regional_immigration',
            field=models.NullBooleanField(verbose_name='willing to move to regional australia?', default=None, choices=[(False, 'No'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=1, null=True, default=None, verbose_name='gender'),
        ),
    ]

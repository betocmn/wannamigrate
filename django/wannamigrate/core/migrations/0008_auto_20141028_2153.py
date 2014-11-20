# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20141024_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonal',
            name='gender',
            field=models.CharField(max_length=1, verbose_name='gender', default=None, choices=[('F', 'Female'), ('M', 'Male')], null=True),
        ),
    ]

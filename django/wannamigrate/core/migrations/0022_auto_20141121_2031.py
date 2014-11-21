# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20141121_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwork',
            name='partner_occupation_months',
            field=models.PositiveSmallIntegerField(verbose_name='Experience', null=True, blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='userworkexperience',
            name='months',
            field=models.PositiveSmallIntegerField(verbose_name='Duration of Employment'),
        ),
    ]

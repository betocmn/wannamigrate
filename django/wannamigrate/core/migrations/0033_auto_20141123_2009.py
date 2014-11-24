# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_userstats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstats',
            name='percentage_education',
            field=models.IntegerField(blank=True, verbose_name='percentage education', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userstats',
            name='percentage_language',
            field=models.IntegerField(blank=True, verbose_name='percentage language', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userstats',
            name='percentage_personal',
            field=models.IntegerField(blank=True, verbose_name='percentage personal', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userstats',
            name='percentage_work',
            field=models.IntegerField(blank=True, verbose_name='percentage work', default=0, null=True),
        ),
    ]

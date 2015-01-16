# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_auto_20150115_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='countryconfig',
            name='country',
        ),
        migrations.DeleteModel(
            name='CountryConfig',
        ),
        migrations.AlterUniqueTogether(
            name='countrypoints',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='countrypoints',
            name='answer',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.RemoveField(
            model_name='countrypoints',
            name='country',
        ),
        migrations.DeleteModel(
            name='CountryPoints',
        ),
    ]

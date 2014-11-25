# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_remove_occupation_countries'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='countryoccupation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='countryoccupation',
            name='country',
        ),
        migrations.RemoveField(
            model_name='countryoccupation',
            name='occupation',
        ),
        migrations.DeleteModel(
            name='CountryOccupation',
        ),
    ]

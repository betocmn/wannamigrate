# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20141125_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupation',
            name='countries',
            field=models.ManyToManyField(to='core.Country', through='core.CountryOccupation'),
            preserve_default=True,
        ),
    ]

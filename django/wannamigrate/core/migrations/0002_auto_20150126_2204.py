# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='points',
            field=models.ManyToManyField(to='core.Country', through='points.CountryPoints'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='results',
            field=models.ManyToManyField(to='core.Country', through='points.UserResult'),
            preserve_default=True,
        ),
    ]

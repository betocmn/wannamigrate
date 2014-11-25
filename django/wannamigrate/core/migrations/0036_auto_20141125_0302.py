# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20141124_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlanguage',
            name='australian_community_language',
        ),
        migrations.AddField(
            model_name='country',
            name='points',
            field=models.ManyToManyField(through='core.CountryPoints', to='core.Answer'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='countrypoints',
            unique_together=set([('answer', 'country')]),
        ),
    ]

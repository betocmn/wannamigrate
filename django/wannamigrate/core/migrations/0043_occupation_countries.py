# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20141125_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupation',
            name='countries',
            field=models.ManyToManyField(to='core.Country'),
            preserve_default=True,
        ),
    ]

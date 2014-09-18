# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20140916_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='immigration_enabled',
            field=models.BooleanField(default=False, verbose_name='immigration enabled?'),
            preserve_default=True,
        ),
    ]

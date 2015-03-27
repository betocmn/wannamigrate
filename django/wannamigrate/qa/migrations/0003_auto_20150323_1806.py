# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20150226_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='answers_count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='followers_count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]

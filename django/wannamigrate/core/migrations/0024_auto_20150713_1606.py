# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20150710_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='followers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
            preserve_default=True,
        ),
    ]

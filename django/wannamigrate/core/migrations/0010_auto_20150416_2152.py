# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150416_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstats',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='user_stats'),
            preserve_default=True,
        ),
    ]

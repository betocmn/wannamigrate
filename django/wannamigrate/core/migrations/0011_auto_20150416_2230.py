# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150416_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstats',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=True,
        ),
    ]

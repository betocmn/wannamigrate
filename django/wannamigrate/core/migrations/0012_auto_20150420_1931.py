# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150416_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstats',
            name='user',
            field=models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL, related_name='userstats'),
            preserve_default=True,
        ),
    ]

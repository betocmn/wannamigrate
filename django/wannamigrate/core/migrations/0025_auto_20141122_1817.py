# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_userwork_work_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereducation',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]

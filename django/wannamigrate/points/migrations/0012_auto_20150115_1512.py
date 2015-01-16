# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0011_auto_20150115_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresult',
            name='country',
            field=models.ForeignKey(verbose_name='country', to='core.Country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresult',
            name='user',
            field=models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresult',
            name='user_result_status',
            field=models.ForeignKey(verbose_name='result status', to='points.UserResultStatus'),
            preserve_default=True,
        ),
    ]

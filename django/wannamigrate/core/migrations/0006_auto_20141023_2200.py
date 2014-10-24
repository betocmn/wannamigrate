# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20141023_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonal',
            name='avatar',
            field=stdimage.models.StdImageField(blank=True, verbose_name='avatar', null=True, upload_to='/wanna/django/wannamigrate/../upload/user'),
        ),
    ]

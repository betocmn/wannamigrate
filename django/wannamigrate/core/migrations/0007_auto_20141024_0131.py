# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20141023_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonal',
            name='avatar',
            field=stdimage.models.StdImageField(blank=True, upload_to='user_pictures', verbose_name='avatar', null=True),
        ),
    ]

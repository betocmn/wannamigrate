# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_goal_usergoal'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
            preserve_default=True,
        ),
    ]

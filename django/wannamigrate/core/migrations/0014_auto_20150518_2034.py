# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150506_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstats',
            name='total_favorite_blogposts',
            field=models.IntegerField(blank=True, verbose_name='total favorite blogposts', null=True, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_favorite_questions',
            field=models.IntegerField(blank=True, verbose_name='total favorite questions', null=True, default=0),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150420_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstats',
            name='total_posts_following',
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_blogposts_following',
            field=models.IntegerField(default=0, verbose_name='total blogposts following', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_questions_following',
            field=models.IntegerField(default=0, verbose_name='total questions following', blank=True, null=True),
            preserve_default=True,
        ),
    ]

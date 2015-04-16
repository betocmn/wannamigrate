# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150224_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstats',
            name='total_posts_following',
            field=models.IntegerField(verbose_name='total posts following', blank=True, default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_topics_following',
            field=models.IntegerField(verbose_name='total topics following', blank=True, default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_users_followers',
            field=models.IntegerField(verbose_name='total users followers', blank=True, default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_users_following',
            field=models.IntegerField(verbose_name='total users following', blank=True, default=0, null=True),
            preserve_default=True,
        ),
    ]

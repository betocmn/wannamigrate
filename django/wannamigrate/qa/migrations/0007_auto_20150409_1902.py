# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0006_auto_20150407_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upvotes_count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(null=True, related_name='answers', to='qa.Post'),
            preserve_default=True,
        ),
    ]

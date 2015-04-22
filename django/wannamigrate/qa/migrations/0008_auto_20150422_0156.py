# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0007_auto_20150409_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upvotes_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

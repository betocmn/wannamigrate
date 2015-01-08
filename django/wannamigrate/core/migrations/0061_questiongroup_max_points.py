# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_questiongroup_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiongroup',
            name='max_points',
            field=models.IntegerField(default=0, verbose_name='max points allowed'),
            preserve_default=True,
        ),
    ]

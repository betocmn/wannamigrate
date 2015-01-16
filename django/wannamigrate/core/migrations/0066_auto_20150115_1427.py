# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_auto_20150105_2246'),
        ('points', '0002_auto_20150115_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwork',
            name='occupation',
            field=models.ForeignKey(to='points.Occupation', null=True, blank=True, verbose_name='occupation'),
            preserve_default=True,
        ),
    ]

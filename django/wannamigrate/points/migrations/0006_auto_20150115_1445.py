# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0005_auto_20150115_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiongroup',
            name='country',
            field=models.ForeignKey(to='core.Country', verbose_name='country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questiongroup',
            name='questions',
            field=models.ManyToManyField(to='points.Question'),
            preserve_default=True,
        ),
    ]

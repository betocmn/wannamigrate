# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_auto_20150115_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupation',
            name='countries',
            field=models.ManyToManyField(to='core.Country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='occupation',
            name='occupation_category',
            field=models.ForeignKey(verbose_name='category', to='points.OccupationCategory'),
            preserve_default=True,
        ),
    ]

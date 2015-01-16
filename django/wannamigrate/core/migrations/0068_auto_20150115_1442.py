# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_auto_20150115_1430'),
        ('points', '0005_auto_20150115_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name='question', to='points.Question'),
            preserve_default=True,
        ),
    ]

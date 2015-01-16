# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_auto_20150115_1501'),
        ('points', '0011_auto_20150115_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='results',
            field=models.ManyToManyField(through='points.UserResult', to='core.Country'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150126_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='name',
            field=models.CharField(max_length=60, verbose_name='name'),
            preserve_default=True,
        ),
    ]

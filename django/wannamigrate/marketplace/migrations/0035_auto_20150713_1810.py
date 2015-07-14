# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0034_auto_20150713_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providerservicetype',
            name='price',
            field=models.DecimalField(max_digits=7, verbose_name='price', decimal_places=2),
            preserve_default=True,
        ),
    ]

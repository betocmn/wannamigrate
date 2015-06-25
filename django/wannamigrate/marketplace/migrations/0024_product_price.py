# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0023_auto_20150624_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=6, default=19.0, decimal_places=2, verbose_name='price'),
            preserve_default=True,
        ),
    ]

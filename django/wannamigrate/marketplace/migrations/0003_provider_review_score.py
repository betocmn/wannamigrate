# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20150204_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='review_score',
            field=models.DecimalField(max_digits=5, decimal_places=2, verbose_name='discount', default=0),
            preserve_default=True,
        ),
    ]

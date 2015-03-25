# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0007_servicetype_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider_servicetypes',
            name='price',
            field=models.DecimalField(decimal_places=2, verbose_name='price', max_digits=5, default=100),
            preserve_default=False,
        ),
    ]

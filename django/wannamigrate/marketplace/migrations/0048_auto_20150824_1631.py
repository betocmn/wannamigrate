# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0047_auto_20150821_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='expiry_date',
            field=models.DateField(blank=True, default=None, verbose_name='expiry date', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='start_date',
            field=models.DateField(blank=True, default=None, verbose_name='start date', null=True),
            preserve_default=True,
        ),
    ]

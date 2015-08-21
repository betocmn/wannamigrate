# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20150721_1419'),
        ('marketplace', '0042_auto_20150806_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.ForeignKey(verbose_name='country', to='core.Country', default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='expiry_months',
            field=models.SmallIntegerField(null=True, verbose_name='expiry months', blank=True, default=None),
            preserve_default=True,
        ),
    ]

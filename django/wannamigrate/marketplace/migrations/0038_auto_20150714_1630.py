# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0037_auto_20150714_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocode',
            name='product',
            field=models.ForeignKey(to='marketplace.Product', verbose_name='product', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='promocode',
            name='service',
            field=models.ForeignKey(to='marketplace.Service', verbose_name='service', null=True, blank=True),
            preserve_default=True,
        ),
    ]

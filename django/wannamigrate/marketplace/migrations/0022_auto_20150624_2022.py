# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0021_auto_20150624_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, to='marketplace.Product', blank=True, verbose_name='product'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.ForeignKey(null=True, to='marketplace.Service', blank=True, verbose_name='service'),
            preserve_default=True,
        ),
    ]

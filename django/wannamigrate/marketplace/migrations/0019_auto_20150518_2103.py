# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0018_auto_20150515_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.DecimalField(verbose_name='discount', decimal_places=2, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='fees',
            field=models.DecimalField(verbose_name='fees', decimal_places=2, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='gross_total',
            field=models.DecimalField(verbose_name='gross total', decimal_places=2, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='net_total',
            field=models.DecimalField(verbose_name='net total', decimal_places=2, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='promocode',
            name='discount',
            field=models.DecimalField(verbose_name='discount', decimal_places=2, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='providerservicetype',
            name='price',
            field=models.DecimalField(verbose_name='price', decimal_places=2, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='service_price',
            field=models.DecimalField(verbose_name='service price', decimal_places=2, max_digits=6),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0027_auto_20150630_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(verbose_name='payment type', default=1, to='marketplace.PaymentType'),
            preserve_default=False,
        ),
    ]

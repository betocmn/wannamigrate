# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0029_auto_20150630_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='boleto_url',
            field=models.CharField(verbose_name='boleto url', null=True, max_length=200, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0017_auto_20150515_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(verbose_name='description', max_length=100, default='Testando'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.CharField(verbose_name='description', max_length=100, default='Testando'),
            preserve_default=False,
        ),
    ]

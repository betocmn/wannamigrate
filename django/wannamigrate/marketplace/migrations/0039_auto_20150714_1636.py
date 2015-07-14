# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0038_auto_20150714_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promocode',
            name='service',
        ),
        migrations.AddField(
            model_name='promocode',
            name='service_type',
            field=models.ForeignKey(null=True, blank=True, verbose_name='service type', to='marketplace.ServiceType'),
            preserve_default=True,
        ),
    ]

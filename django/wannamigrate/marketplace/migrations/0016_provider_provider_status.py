# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0015_auto_20150414_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='provider_status',
            field=models.ForeignKey(default=2, verbose_name='status', to='marketplace.ProviderStatus'),
            preserve_default=False,
        ),
    ]

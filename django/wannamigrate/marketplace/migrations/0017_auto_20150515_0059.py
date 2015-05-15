# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0016_provider_provider_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderhistory',
            name='message',
        ),
        migrations.RemoveField(
            model_name='orderhistory',
            name='payment_code',
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='full_api_response',
            field=models.TextField(null=True, blank=True, verbose_name='full API response'),
            preserve_default=True,
        ),
    ]

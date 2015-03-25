# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0006_servicetype_service_type_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
            preserve_default=True,
        ),
    ]

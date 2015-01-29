# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150127_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='preferred_timezone',
            field=models.CharField(max_length=100, blank=True, verbose_name='Timezone', null=True),
            preserve_default=True,
        ),
    ]

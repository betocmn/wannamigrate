# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0002_auto_20150928_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='objective',
            name='is_public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

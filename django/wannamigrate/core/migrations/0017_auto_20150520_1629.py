# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationstatus_user',
            name='has_updates',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='preferred_language',
            field=models.CharField(default='en', choices=[('en', 'English'), ('pt', 'Português')], verbose_name='Preferred Language', max_length=6),
            preserve_default=True,
        ),
    ]

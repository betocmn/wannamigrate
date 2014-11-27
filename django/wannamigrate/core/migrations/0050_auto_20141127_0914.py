# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_auto_20141126_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='preferred_language',
            field=models.CharField(choices=[('en', 'English'), ('pt-br', 'Portuguese (BR)')], verbose_name='Language', default='en', max_length=6),
            preserve_default=True,
        ),
    ]

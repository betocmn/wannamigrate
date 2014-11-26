# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_auto_20141126_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='language',
            new_name='preferred_language',
        ),
    ]

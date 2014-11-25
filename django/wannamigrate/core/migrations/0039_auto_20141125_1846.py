# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20141125_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occupation',
            old_name='description',
            new_name='name',
        ),
    ]

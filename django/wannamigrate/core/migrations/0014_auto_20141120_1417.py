# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20141120_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonal',
            name='family_overseas',
            field=models.NullBooleanField(default=None, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Any family members who are citizens in other countries?'),
        ),
    ]

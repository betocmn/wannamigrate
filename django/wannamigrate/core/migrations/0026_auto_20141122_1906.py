# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20141122_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwork',
            name='partner_occupation_answer',
        ),
        migrations.RemoveField(
            model_name='userwork',
            name='partner_occupation_months',
        ),
        migrations.AddField(
            model_name='userwork',
            name='partner_skills',
            field=models.NullBooleanField(default=None, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you have a partner with proved skills?'),
            preserve_default=True,
        ),
    ]

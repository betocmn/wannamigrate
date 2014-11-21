# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20141121_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwork',
            name='work_offer',
            field=models.NullBooleanField(verbose_name='Do you have a work offer overseas', default=None, choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
    ]

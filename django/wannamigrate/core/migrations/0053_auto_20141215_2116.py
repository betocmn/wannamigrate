# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20141207_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereducation',
            name='regional_australia_study',
            field=models.NullBooleanField(verbose_name='Did you complete any studies in a regional part of Australia', choices=[(True, 'Yes'), (False, 'No')], default=None),
            preserve_default=True,
        ),
    ]

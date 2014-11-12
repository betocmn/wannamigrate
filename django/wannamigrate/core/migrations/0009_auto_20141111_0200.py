# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20141028_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonal',
            name='australian_regional_immigration',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], verbose_name='willing to move to regional australia?', default=None),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='country',
            field=models.ForeignKey(to='core.Country', blank=True, null=True, verbose_name='country of residence'),
        ),
    ]

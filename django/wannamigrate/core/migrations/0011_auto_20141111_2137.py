# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20141111_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpersonal',
            name='family_overseas',
            field=models.NullBooleanField(default=None, verbose_name='Any family member who are citizens in other countries?', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='australian_regional_immigration',
            field=models.NullBooleanField(default=None, verbose_name='Would you be willing to live in Regional Australia?', choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20141121_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwork',
            name='canadian_startup_letter',
            field=models.NullBooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, verbose_name='do you have a startup recommendation letter approved by canada'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='willing_to_invest',
            field=models.NullBooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, verbose_name='are you willing to invest money on the country of destination'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20141121_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwork',
            name='partner_occupation_months',
            field=models.IntegerField(verbose_name='Experience', blank=True, null=True, default=None),
        ),
    ]

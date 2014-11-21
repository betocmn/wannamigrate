# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20141121_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwork',
            name='partner_occupation_months',
            field=models.IntegerField(blank=True, verbose_name='Experience', null=True, default=None),
        ),
    ]

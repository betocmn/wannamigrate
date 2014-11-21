# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20141121_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwork',
            name='partner_occupation_months',
            field=models.IntegerField(null=True, verbose_name='Experience', default=0, blank=True),
        ),
    ]

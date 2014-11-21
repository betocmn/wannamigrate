# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20141121_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwork',
            name='partner_occupation_months',
            field=models.IntegerField(verbose_name='Experience', default=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userworkexperience',
            name='months',
            field=models.IntegerField(verbose_name='Duration of Employment'),
        ),
    ]

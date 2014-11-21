# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20141120_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userworkexperience',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='userworkexperience',
            name='start_date',
        ),
        migrations.AddField(
            model_name='userworkexperience',
            name='months',
            field=models.IntegerField(verbose_name='Months of Employment', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usereducationhistory',
            name='school',
            field=models.CharField(max_length=100, verbose_name='school/university'),
        ),
    ]

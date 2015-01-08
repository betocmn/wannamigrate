# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_auto_20141222_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='method_name',
            field=models.CharField(max_length=60, verbose_name='method name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(max_length=15, verbose_name='type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresult',
            name='user_result_status',
            field=models.ForeignKey(to='core.UserResultStatus', verbose_name='result status'),
            preserve_default=True,
        ),
    ]

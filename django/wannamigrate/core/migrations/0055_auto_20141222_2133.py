# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_auto_20141215_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='method_name',
            field=models.CharField(default='get_points', verbose_name='method name', max_length=60),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(default='personal', verbose_name='type', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userresult',
            name='user_result_status',
            field=models.ForeignKey(verbose_name='result status', default=2, to='core.UserResultStatus'),
            preserve_default=True,
        ),
    ]

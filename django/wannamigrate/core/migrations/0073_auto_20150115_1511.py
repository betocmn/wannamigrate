# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_auto_20150115_1510'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userresult',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='userresult',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userresult',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userresult',
            name='user_result_status',
        ),
        migrations.DeleteModel(
            name='UserResult',
        ),
        migrations.DeleteModel(
            name='UserResultStatus',
        ),
    ]

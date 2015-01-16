# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_auto_20150115_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questiongroup',
            name='country',
        ),
        migrations.RemoveField(
            model_name='questiongroup',
            name='questions',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='QuestionGroup',
        ),
    ]

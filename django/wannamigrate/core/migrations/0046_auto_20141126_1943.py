# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_remove_answer_answer_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answercategory',
            name='question',
        ),
        migrations.DeleteModel(
            name='AnswerCategory',
        ),
    ]

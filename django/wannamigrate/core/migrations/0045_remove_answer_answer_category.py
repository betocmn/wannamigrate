# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_user_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_category',
        ),
    ]

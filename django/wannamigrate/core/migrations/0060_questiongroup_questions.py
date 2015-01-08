# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_questiongroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiongroup',
            name='questions',
            field=models.ManyToManyField(to='core.Question'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0007_auto_20150522_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topictranslation',
            name='slug',
            field=models.SlugField(max_length=100),
            preserve_default=True,
        ),
    ]

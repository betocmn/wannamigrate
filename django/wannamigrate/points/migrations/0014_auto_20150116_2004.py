# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0013_auto_20150116_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.IntegerField(verbose_name='question'),
            preserve_default=True,
        ),
    ]

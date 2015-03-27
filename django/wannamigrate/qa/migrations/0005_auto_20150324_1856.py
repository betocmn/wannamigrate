# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0004_auto_20150324_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='related_countries',
            field=models.ManyToManyField(to='core.Country', related_name='related_topics'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='related_goals',
            field=models.ManyToManyField(to='core.Goal', related_name='related_topics'),
            preserve_default=True,
        ),
    ]

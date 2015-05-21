# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20150520_1629'),
        ('qa', '0003_auto_20150515_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='related_countries',
        ),
        migrations.AddField(
            model_name='topic',
            name='country',
            field=models.ForeignKey(null=True, to='core.Country', blank=True, related_name='topic'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='related_goals',
            field=models.ManyToManyField(to='core.Goal', blank=True, null=True, related_name='related_topics'),
            preserve_default=True,
        ),
    ]

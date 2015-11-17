# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20150929_1308'),
        ('director', '0006_auto_20151113_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='goal',
            field=models.ForeignKey(verbose_name='goal', to='core.Goal', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mission',
            name='order',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mission',
            name='to_country',
            field=models.ForeignKey(verbose_name='to country', to='core.Country', default=117),
            preserve_default=False,
        ),
    ]

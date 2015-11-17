# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0008_auto_20151117_1543'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='situationsmissions',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='situationsmissions',
            name='mission',
        ),
        migrations.RemoveField(
            model_name='situationsmissions',
            name='situation',
        ),
        migrations.RemoveField(
            model_name='mission',
            name='situations',
        ),
        migrations.DeleteModel(
            name='SituationsMissions',
        ),
    ]

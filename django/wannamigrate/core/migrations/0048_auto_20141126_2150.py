# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20141126_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwork',
            name='occupation_answer',
        ),
        migrations.AddField(
            model_name='userwork',
            name='occupation',
            field=models.ForeignKey(blank=True, to='core.Occupation', null=True, verbose_name='occupation'),
            preserve_default=True,
        ),
    ]

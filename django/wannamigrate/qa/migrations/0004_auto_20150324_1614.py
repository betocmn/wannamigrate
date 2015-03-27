# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150224_1800'),
        ('qa', '0003_auto_20150323_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='related_countries',
            field=models.ManyToManyField(to='core.Country', related_name='related_countries'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='topic',
            name='related_goals',
            field=models.ManyToManyField(to='core.Goal', related_name='related_goals'),
            preserve_default=True,
        ),
    ]

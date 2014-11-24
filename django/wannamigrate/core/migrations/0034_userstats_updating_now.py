# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20141123_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstats',
            name='updating_now',
            field=models.BooleanField(verbose_name='updating now', default=False),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_occupation_countries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupation',
            name='countries',
        ),
    ]

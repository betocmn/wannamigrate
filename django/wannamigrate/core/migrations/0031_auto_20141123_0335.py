# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20141123_0252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='country_results',
            new_name='results',
        ),
    ]

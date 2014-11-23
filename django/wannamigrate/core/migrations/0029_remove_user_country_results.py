# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_user_country_results'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='country_results',
        ),
    ]

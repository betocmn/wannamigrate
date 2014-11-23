# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20141122_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country_results',
            field=models.ManyToManyField(through='core.UserResult', to='core.Country'),
            preserve_default=True,
        ),
    ]

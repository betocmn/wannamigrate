# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0012_auto_20150407_2103'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='providercountry',
            unique_together=set([('country', 'provider')]),
        ),
        migrations.AlterUniqueTogether(
            name='providerlanguage',
            unique_together=set([('language', 'provider')]),
        ),
    ]

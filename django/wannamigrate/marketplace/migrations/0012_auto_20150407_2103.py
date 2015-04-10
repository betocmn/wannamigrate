# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0011_auto_20150407_1837'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='providercountry',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='providerlanguage',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='providerservicetype',
            unique_together=set([]),
        ),
    ]

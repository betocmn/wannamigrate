# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_auto_20141128_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonal',
            name='country',
            field=models.ForeignKey(blank=True, verbose_name='country of citizenship', null=True, to='core.Country'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_auto_20150226_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='service_type_category',
            field=models.ForeignKey(default=1, to='marketplace.ServiceTypeCategory', verbose_name='category'),
            preserve_default=False,
        ),
    ]

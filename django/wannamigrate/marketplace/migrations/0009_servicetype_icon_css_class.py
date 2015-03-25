# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0008_provider_servicetypes_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='icon_css_class',
            field=models.CharField(max_length=30, verbose_name='name', default='review'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20150608_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_userloginhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpersonal',
            name='avatar',
            field=models.CharField(verbose_name='avatar', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]

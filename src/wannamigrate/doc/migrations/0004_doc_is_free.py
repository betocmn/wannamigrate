# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-08 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0003_auto_20170701_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='is_free',
            field=models.BooleanField(default=True, verbose_name='is free'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-26 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_enabled',
            field=models.BooleanField(default=True, verbose_name='is enabled'),
        ),
    ]
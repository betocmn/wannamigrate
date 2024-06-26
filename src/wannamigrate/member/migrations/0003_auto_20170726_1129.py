# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-26 01:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170726_1115'),
        ('member', '0002_member_quiz_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Stage', verbose_name='stage'),
        ),
        migrations.AddField(
            model_name='member',
            name='visa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Visa', verbose_name='visa'),
        ),
    ]

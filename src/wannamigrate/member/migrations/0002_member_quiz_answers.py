# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-03 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20170402_0109'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='quiz_answers',
            field=models.ManyToManyField(to='quiz.QuizAnswer'),
        ),
    ]

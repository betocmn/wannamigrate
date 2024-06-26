# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-01 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import stdimage.models
import wannamigrate.core.util


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='photo',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=wannamigrate.core.util.CustomUploadToAutoSlugClassNameDir('description'), verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='quizanswer',
            name='points',
            field=models.PositiveSmallIntegerField(verbose_name='points'),
        ),
    ]

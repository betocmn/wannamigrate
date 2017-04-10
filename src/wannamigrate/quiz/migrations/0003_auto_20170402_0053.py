# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-01 13:53
from __future__ import unicode_literals

from django.db import migrations
import stdimage.models
import stdimage.utils


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20170402_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='photo',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=stdimage.utils.UploadToClassNameDirUUID(), verbose_name='photo'),
        ),
    ]

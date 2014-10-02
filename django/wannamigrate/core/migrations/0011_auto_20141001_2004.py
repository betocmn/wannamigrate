# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_country_immigration_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', null=True, max_length=255, verbose_name='username'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=255, verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='language_level_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Answer', verbose_name='language level'),
        ),
    ]

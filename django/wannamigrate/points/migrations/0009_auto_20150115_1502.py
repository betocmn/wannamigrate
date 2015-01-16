# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0008_auto_20150115_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='points.Question', verbose_name='question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='countryconfig',
            name='country',
            field=models.OneToOneField(to='core.Country', verbose_name='country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='countrypoints',
            name='answer',
            field=models.ForeignKey(to='points.Answer', verbose_name='answer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='countrypoints',
            name='country',
            field=models.ForeignKey(to='core.Country', verbose_name='country'),
            preserve_default=True,
        ),
    ]

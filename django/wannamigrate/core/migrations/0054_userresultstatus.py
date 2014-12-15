# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_auto_20141215_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResultStatus',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

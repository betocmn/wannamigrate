# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20141207_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResultStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='regional_australia_study',
            field=models.NullBooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, verbose_name='Did you complete any studies in a regional part of Australia'),
            preserve_default=True,
        ),
    ]

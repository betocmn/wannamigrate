# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_questiongroup_max_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('pass_mark_points', models.IntegerField(verbose_name='pass mark points', default=0)),
                ('max_personal_points', models.IntegerField(verbose_name='max personal points', default=0)),
                ('max_language_points', models.IntegerField(verbose_name='max language points', default=0)),
                ('max_education_points', models.IntegerField(verbose_name='max education points', default=0)),
                ('max_work_points', models.IntegerField(verbose_name='max education points', default=0)),
                ('max_total_points', models.IntegerField(verbose_name='max total points', default=0)),
                ('country', models.OneToOneField(verbose_name='country', to='core.Country')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

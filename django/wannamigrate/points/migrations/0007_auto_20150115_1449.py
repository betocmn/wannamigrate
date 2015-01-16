# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_auto_20150115_1443'),
        ('points', '0006_auto_20150115_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('description', models.CharField(max_length=255, verbose_name='Answer')),
                ('question', models.ForeignKey(to='points.Question', verbose_name='question', related_name='question_new')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CountryConfig',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('pass_mark_points', models.IntegerField(default=0, verbose_name='pass mark points')),
                ('max_personal_points', models.IntegerField(default=0, verbose_name='max personal points')),
                ('max_language_points', models.IntegerField(default=0, verbose_name='max language points')),
                ('max_education_points', models.IntegerField(default=0, verbose_name='max education points')),
                ('max_work_points', models.IntegerField(default=0, verbose_name='max education points')),
                ('max_total_points', models.IntegerField(default=0, verbose_name='max total points')),
                ('country', models.OneToOneField(to='core.Country', verbose_name='country', related_name='country_new_1')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CountryPoints',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('points', models.IntegerField(verbose_name='points')),
                ('answer', models.ForeignKey(to='points.Answer', verbose_name='answer', related_name='answer_new')),
                ('country', models.ForeignKey(to='core.Country', verbose_name='country', related_name='country_new_2')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='countrypoints',
            unique_together=set([('answer', 'country')]),
        ),
    ]

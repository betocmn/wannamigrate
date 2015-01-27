# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('description', models.CharField(max_length=255, verbose_name='Answer')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CountryConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('pass_mark_points', models.IntegerField(default=0, verbose_name='pass mark points')),
                ('max_personal_points', models.IntegerField(default=0, verbose_name='max personal points')),
                ('max_language_points', models.IntegerField(default=0, verbose_name='max language points')),
                ('max_education_points', models.IntegerField(default=0, verbose_name='max education points')),
                ('max_work_points', models.IntegerField(default=0, verbose_name='max education points')),
                ('max_total_points', models.IntegerField(default=0, verbose_name='max total points')),
                ('country', models.OneToOneField(to='core.Country', verbose_name='country')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CountryPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('points', models.IntegerField(verbose_name='points')),
                ('answer', models.ForeignKey(to='points.Answer', verbose_name='answer')),
                ('country', models.ForeignKey(to='core.Country', verbose_name='country')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=180, verbose_name='Name')),
                ('countries', models.ManyToManyField(to='core.Country')),
            ],
            options={
                'permissions': (('admin_add_occupation', 'ADMIN: Can add occupation'), ('admin_change_occupation', 'ADMIN: Can change occupation'), ('admin_delete_occupation', 'ADMIN: Can delete occupation'), ('admin_view_occupation', 'ADMIN: Can view occupations')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OccupationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('description', models.CharField(max_length=255, verbose_name='question')),
                ('help_text', models.TextField(null=True, verbose_name='help text', blank=True)),
                ('method_name', models.CharField(max_length=60, verbose_name='method name')),
                ('type', models.CharField(max_length=15, verbose_name='type')),
            ],
            options={
                'permissions': (('admin_add_immigration_rule', 'ADMIN: Can add immigration rule'), ('admin_change_immigration_rule', 'ADMIN: Can change immigration rule'), ('admin_delete_immigration_rule', 'ADMIN: Can delete immigration rule'), ('admin_view_immigration_rule', 'ADMIN: Can view immigration rules')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.TextField(verbose_name='name')),
                ('max_points', models.IntegerField(default=0, verbose_name='max points allowed')),
                ('country', models.ForeignKey(to='core.Country', verbose_name='country')),
                ('questions', models.ManyToManyField(to='points.Question')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('score_total', models.IntegerField(verbose_name='total score')),
                ('score_personal', models.IntegerField(verbose_name='score personal')),
                ('score_language', models.IntegerField(verbose_name='score language')),
                ('score_education', models.IntegerField(verbose_name='score education')),
                ('score_work', models.IntegerField(verbose_name='score work')),
                ('country', models.ForeignKey(to='core.Country', verbose_name='country')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserResultStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userresult',
            name='user_result_status',
            field=models.ForeignKey(to='points.UserResultStatus', verbose_name='result status'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='userresult',
            unique_together=set([('user', 'country')]),
        ),
        migrations.AddField(
            model_name='occupation',
            name='occupation_category',
            field=models.ForeignKey(to='points.OccupationCategory', verbose_name='category'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='countrypoints',
            unique_together=set([('answer', 'country')]),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='points.Question', verbose_name='question'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_auto_20150115_1501'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('points', '0009_auto_20150115_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('score_total', models.IntegerField(verbose_name='total score')),
                ('score_personal', models.IntegerField(verbose_name='score personal')),
                ('score_language', models.IntegerField(verbose_name='score language')),
                ('score_education', models.IntegerField(verbose_name='score education')),
                ('score_work', models.IntegerField(verbose_name='score work')),
                ('country', models.ForeignKey(to='core.Country', verbose_name='country', related_name='country_new_3')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='user_new')),
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
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
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
            field=models.ForeignKey(to='points.UserResultStatus', verbose_name='result status', related_name='user_result_status_new'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='userresult',
            unique_together=set([('user', 'country')]),
        ),
    ]

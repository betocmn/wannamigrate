# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
                ('body', models.TextField(blank=True, default='')),
                ('is_anonymous', models.BooleanField(default=False)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('last_activity_date', models.DateTimeField(null=True)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='following_posts')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, to='qa.Post')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
                ('body', models.TextField(blank=True, default='')),
                ('written_date', models.DateTimeField()),
                ('original_post', models.ForeignKey(to='qa.Post')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=255)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='following_topics')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('post', models.ForeignKey(to='qa.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_type',
            field=models.ForeignKey(to='qa.VoteType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(to='qa.PostType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='readers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='reading_list'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='related_topics',
            field=models.ManyToManyField(to='qa.Topic', related_name='related_posts'),
            preserve_default=True,
        ),
    ]

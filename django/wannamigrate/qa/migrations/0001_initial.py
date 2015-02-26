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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('title', models.CharField(default='', blank=True, max_length=255)),
                ('body', models.TextField(default='', blank=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('last_activity_date', models.DateTimeField(null=True)),
                ('followers', models.ManyToManyField(related_name='following_posts', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, to='qa.Post')),
            ],
            options={
                'permissions': (('admin_add_post', '[ADMIN] Can add post'), ('admin_edit_post', '[ADMIN] Can edit post'), ('admin_delete_post', '[ADMIN] Can delete post'), ('admin_view_post', '[ADMIN] Can view post'), ('admin_list_post', '[ADMIN] Can list posts')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostHistory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('title', models.CharField(default='', blank=True, max_length=255)),
                ('body', models.TextField(default='', blank=True)),
                ('written_date', models.DateTimeField()),
                ('original_post', models.ForeignKey(to='qa.Post')),
            ],
            options={
                'permissions': (('admin_add_post_history', '[ADMIN] Can add post history'), ('admin_edit_post_history', '[ADMIN] Can edit post history'), ('admin_delete_post_history', '[ADMIN] Can delete post history'), ('admin_view_post_history', '[ADMIN] Can view post history'), ('admin_list_post_history', '[ADMIN] Can list post history')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('followers', models.ManyToManyField(related_name='following_topics', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('admin_add_topic', '[ADMIN] Can add topic'), ('admin_edit_topic', '[ADMIN] Can edit topic'), ('admin_delete_topic', '[ADMIN] Can delete topic'), ('admin_view_topic', '[ADMIN] Can view topic'), ('admin_list_topic', '[ADMIN] Can list topic')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('post', models.ForeignKey(to='qa.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('admin_add_vote', '[ADMIN] Can add vote'), ('admin_edit_vote', '[ADMIN] Can edit vote'), ('admin_delete_vote', '[ADMIN] Can delete vote'), ('admin_view_vote', '[ADMIN] Can view vote'), ('admin_list_vote', '[ADMIN] Can list vote')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'default_permissions': [],
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
            field=models.ManyToManyField(related_name='reading_list', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='related_topics',
            field=models.ManyToManyField(related_name='related_posts', to='qa.Topic'),
            preserve_default=True,
        ),
    ]

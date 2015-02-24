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
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('title', models.CharField(max_length=255, blank=True, default='')),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
>>>>>>> ef2dd8818d5c30f7754dcd1ccbc8e149f96884bc
                ('body', models.TextField(blank=True, default='')),
                ('is_anonymous', models.BooleanField(default=False)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('last_activity_date', models.DateTimeField(null=True)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='following_posts')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, to='qa.Post')),
            ],
            options={
<<<<<<< HEAD
                'default_permissions': [],
                'permissions': (('admin_add_post', '[ADMIN] Can add post'), ('admin_edit_post', '[ADMIN] Can edit post'), ('admin_delete_post', '[ADMIN] Can delete post'), ('admin_view_post', '[ADMIN] Can view post'), ('admin_list_post', '[ADMIN] Can list posts')),
=======
                'abstract': False,
>>>>>>> ef2dd8818d5c30f7754dcd1ccbc8e149f96884bc
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostHistory',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('title', models.CharField(max_length=255, blank=True, default='')),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
>>>>>>> ef2dd8818d5c30f7754dcd1ccbc8e149f96884bc
                ('body', models.TextField(blank=True, default='')),
                ('written_date', models.DateTimeField()),
                ('original_post', models.ForeignKey(to='qa.Post')),
            ],
            options={
<<<<<<< HEAD
                'default_permissions': [],
                'permissions': (('admin_add_post_history', '[ADMIN] Can add post history'), ('admin_edit_post_history', '[ADMIN] Can edit post history'), ('admin_delete_post_history', '[ADMIN] Can delete post history'), ('admin_view_post_history', '[ADMIN] Can view post history'), ('admin_list_post_history', '[ADMIN] Can list post history')),
=======
                'abstract': False,
>>>>>>> ef2dd8818d5c30f7754dcd1ccbc8e149f96884bc
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'default_permissions': [],
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
>>>>>>> ef2dd8818d5c30f7754dcd1ccbc8e149f96884bc
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
>>>>>>> ef2dd8818d5c30f7754dcd1ccbc8e149f96884bc
                ('name', models.CharField(max_length=255)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='following_topics')),
            ],
            options={
<<<<<<< HEAD
                'default_permissions': [],
                'permissions': (('admin_add_topic', '[ADMIN] Can add topic'), ('admin_edit_topic', '[ADMIN] Can edit topic'), ('admin_delete_topic', '[ADMIN] Can delete topic'), ('admin_view_topic', '[ADMIN] Can view topic'), ('admin_list_topic', '[ADMIN] Can list topic')),
=======
                'abstract': False,
>>>>>>> ef2dd8818d5c30f7754dcd1ccbc8e149f96884bc
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
>>>>>>> ef2dd8818d5c30f7754dcd1ccbc8e149f96884bc
                ('post', models.ForeignKey(to='qa.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
<<<<<<< HEAD
                'default_permissions': [],
                'permissions': (('admin_add_vote', '[ADMIN] Can add vote'), ('admin_edit_vote', '[ADMIN] Can edit vote'), ('admin_delete_vote', '[ADMIN] Can delete vote'), ('admin_view_vote', '[ADMIN] Can view vote'), ('admin_list_vote', '[ADMIN] Can list vote')),
=======
                'abstract': False,
>>>>>>> ef2dd8818d5c30f7754dcd1ccbc8e149f96884bc
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteType',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'default_permissions': [],
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
>>>>>>> ef2dd8818d5c30f7754dcd1ccbc8e149f96884bc
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

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0013_auto_20150506_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('total_upvotes', models.PositiveIntegerField(default=0)),
                ('total_downvotes', models.PositiveIntegerField(default=0)),
                ('total_reports', models.PositiveIntegerField(default=0)),
                ('total_comments', models.PositiveIntegerField(default=0)),
                ('body', models.TextField(default='')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('admin_add_answer', '[ADMIN] Can add answer'), ('admin_edit_answer', '[ADMIN] Can edit answer'), ('admin_delete_answer', '[ADMIN] Can delete answer'), ('admin_view_answer', '[ADMIN] Can view answer'), ('admin_list_answer', '[ADMIN] Can list answer')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('total_followers', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('body', models.TextField(default='')),
                ('last_activity_date', models.DateTimeField()),
                ('total_views', models.PositiveIntegerField(default=0)),
                ('total_upvotes', models.PositiveIntegerField(default=0)),
                ('total_downvotes', models.PositiveIntegerField(default=0)),
                ('total_reports', models.PositiveIntegerField(default=0)),
                ('total_comments', models.PositiveIntegerField(default=0)),
                ('followers', models.ManyToManyField(related_name='following_blogpost', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('admin_add_blogpost', '[ADMIN] Can add blogpost'), ('admin_edit_blogpost', '[ADMIN] Can edit blogpost'), ('admin_delete_blogpost', '[ADMIN] Can delete blogpost'), ('admin_view_blogpost', '[ADMIN] Can view blogpost'), ('admin_list_blogpost', '[ADMIN] Can list blogpost')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('total_upvotes', models.PositiveIntegerField(default=0)),
                ('total_downvotes', models.PositiveIntegerField(default=0)),
                ('total_reports', models.PositiveIntegerField(default=0)),
                ('total_comments', models.PositiveIntegerField(default=0)),
                ('body', models.TextField(default='')),
                ('object_id', models.PositiveIntegerField(default=0)),
                ('content_type', models.ForeignKey(default=None, to='contenttypes.ContentType')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('admin_add_comment', '[ADMIN] Can add comment'), ('admin_edit_comment', '[ADMIN] Can edit comment'), ('admin_delete_comment', '[ADMIN] Can delete comment'), ('admin_view_comment', '[ADMIN] Can view comment'), ('admin_list_comment', '[ADMIN] Can list comment')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('total_followers', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('body', models.TextField(default='')),
                ('last_activity_date', models.DateTimeField()),
                ('total_views', models.PositiveIntegerField(default=0)),
                ('total_upvotes', models.PositiveIntegerField(default=0)),
                ('total_downvotes', models.PositiveIntegerField(default=0)),
                ('total_reports', models.PositiveIntegerField(default=0)),
                ('total_comments', models.PositiveIntegerField(default=0)),
                ('total_answers', models.PositiveIntegerField(default=0)),
                ('followers', models.ManyToManyField(related_name='following_question', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('admin_add_question', '[ADMIN] Can add question'), ('admin_edit_question', '[ADMIN] Can edit question'), ('admin_delete_question', '[ADMIN] Can delete question'), ('admin_view_question', '[ADMIN] Can view question'), ('admin_list_question', '[ADMIN] Can list question')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('followers', models.ManyToManyField(related_name='following_topics', to=settings.AUTH_USER_MODEL)),
                ('related_countries', models.ManyToManyField(related_name='related_topics', to='core.Country')),
                ('related_goals', models.ManyToManyField(related_name='related_topics', to='core.Goal')),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('object_id', models.PositiveIntegerField(default=0)),
                ('content_type', models.ForeignKey(default=None, to='contenttypes.ContentType')),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
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
            model_name='question',
            name='related_topics',
            field=models.ManyToManyField(related_name='related_question', to='qa.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='related_topics',
            field=models.ManyToManyField(related_name='related_blogpost', to='qa.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', to='qa.Question'),
            preserve_default=True,
        ),
    ]

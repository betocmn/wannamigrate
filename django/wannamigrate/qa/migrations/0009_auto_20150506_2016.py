# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
        ('qa', '0008_auto_20150422_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('total_followers', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('body', models.TextField(default='')),
                ('last_activity_date', models.DateTimeField()),
                ('total_views', models.PositiveIntegerField(default=0)),
                ('total_upvotes', models.PositiveIntegerField(default=0)),
                ('total_downvotes', models.PositiveIntegerField(default=0)),
                ('total_reports', models.PositiveIntegerField(default=0)),
                ('total_comments', models.PositiveIntegerField(default=0)),
                ('followers', models.ManyToManyField(related_name='following_blogpost', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('related_topics', models.ManyToManyField(related_name='related_blogpost', to='qa.Topic')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('total_upvotes', models.PositiveIntegerField(default=0)),
                ('total_downvotes', models.PositiveIntegerField(default=0)),
                ('total_reports', models.PositiveIntegerField(default=0)),
                ('total_comments', models.PositiveIntegerField(default=0)),
                ('body', models.TextField(default='')),
                ('object_id', models.PositiveIntegerField(default=0)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', default=None)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('total_followers', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
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
                ('related_topics', models.ManyToManyField(related_name='related_question', to='qa.Topic')),
            ],
            options={
                'permissions': (('admin_add_question', '[ADMIN] Can add question'), ('admin_edit_question', '[ADMIN] Can edit question'), ('admin_delete_question', '[ADMIN] Can delete question'), ('admin_view_question', '[ADMIN] Can view question'), ('admin_list_question', '[ADMIN] Can list question')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='post',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='post',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='readers',
        ),
        migrations.RemoveField(
            model_name='post',
            name='related_topics',
        ),
        migrations.RemoveField(
            model_name='posthistory',
            name='original_post',
        ),
        migrations.DeleteModel(
            name='PostHistory',
        ),
        migrations.DeleteModel(
            name='PostType',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', to='qa.Question'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='vote',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='vote',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vote',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]

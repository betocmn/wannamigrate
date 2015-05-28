# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0010_auto_20150524_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(default='')),
                ('parent_created_date', models.DateTimeField()),
                ('parent', models.ForeignKey(related_name='edition_history', to='qa.BlogPost')),
            ],
            options={
                'permissions': (('admin_add_blogpost_history', '[ADMIN] Can add blogpost history'), ('admin_edit_blogpost_history', '[ADMIN] Can edit blogpost history'), ('admin_delete_blogpost_history', '[ADMIN] Can delete blogpost history'), ('admin_view_blogpost_history', '[ADMIN] Can view blogpost history'), ('admin_list_blogpost_history', '[ADMIN] Can list blogpost history')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(default='')),
                ('parent_created_date', models.DateTimeField()),
                ('parent', models.ForeignKey(related_name='edition_history', to='qa.Question')),
            ],
            options={
                'permissions': (('admin_add_question_history', '[ADMIN] Can add question history'), ('admin_edit_question_history', '[ADMIN] Can edit question history'), ('admin_delete_question_history', '[ADMIN] Can delete question history'), ('admin_view_question_history', '[ADMIN] Can view question history'), ('admin_list_question_history', '[ADMIN] Can list question history')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

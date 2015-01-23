# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_auto_20150122_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('content', models.TextField(verbose_name='comment')),
                ('is_read', models.BooleanField(default=False, verbose_name='is read')),
                ('from_user', models.ForeignKey(verbose_name='from user', to=settings.AUTH_USER_MODEL, related_name='message_from_user')),
                ('to_user', models.ForeignKey(verbose_name='to user', to=settings.AUTH_USER_MODEL, related_name='message_to_user')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

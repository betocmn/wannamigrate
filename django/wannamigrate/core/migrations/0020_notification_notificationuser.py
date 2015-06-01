# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150522_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('message', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'default_permissions': [],
                'permissions': (('admin_add_notification', 'ADMIN: Can add notification'), ('admin_change_notification', 'ADMIN: Can change notification'), ('admin_delete_notification', 'ADMIN: Can delete notification'), ('admin_view_notification', 'ADMIN: Can view notification')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotificationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('is_read', models.BooleanField(default=False)),
                ('notification', models.ForeignKey(related_name='notifications_users', to='core.Notification')),
                ('user', models.ForeignKey(related_name='notifications_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
                'permissions': (('admin_add_notification_user', 'ADMIN: Can add notification user'), ('admin_change_notification_user', 'ADMIN: Can change notification user'), ('admin_delete_notification_user', 'ADMIN: Can delete notification user'), ('admin_view_notification_user', 'ADMIN: Can view notification user')),
            },
            bases=(models.Model,),
        ),
    ]

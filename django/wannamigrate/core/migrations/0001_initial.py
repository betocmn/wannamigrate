# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='e-mail')),
                ('name', models.CharField(max_length=120, verbose_name='name', null=True, default='')),
                ('is_active', models.BooleanField(verbose_name='is active', default=True)),
                ('is_admin', models.BooleanField(verbose_name='is admin', default=False)),
                ('preferred_language', models.CharField(max_length=6, verbose_name='Language', choices=[('en', 'English'), ('pt-br', 'Portuguese (BR)')], default='en')),
                ('groups', models.ManyToManyField(related_name='user_set', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_query_name='user', blank=True, to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', verbose_name='user permissions', help_text='Specific permissions for this user.', related_query_name='user', blank=True, to='auth.Permission')),
            ],
            options={
                'default_permissions': [],
                'permissions': (('admin_add_user', 'ADMIN: Can add user'), ('admin_change_user', 'ADMIN: Can change user'), ('admin_delete_user', 'ADMIN: Can delete user'), ('admin_view_user', 'ADMIN: Can view users'), ('admin_add_admin_user', 'ADMIN: Can add admin user'), ('admin_change_admin_user', 'ADMIN: Can change admin user'), ('admin_delete_admin_user', 'ADMIN: Can delete admin user'), ('admin_view_admin_user', 'ADMIN: Can view admin users')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('code', models.CharField(max_length=2, verbose_name='code')),
                ('immigration_enabled', models.BooleanField(verbose_name='immigration enabled', default=False)),
                ('continent', models.ForeignKey(verbose_name='continent', to='core.Continent')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

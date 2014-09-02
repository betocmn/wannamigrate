# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'e-mail')),
                ('name', models.CharField(default=b'', max_length=120, null=True, verbose_name=b'name')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'is active?')),
                ('is_admin', models.BooleanField(default=False, verbose_name=b'is admin?')),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='groups', blank=True)),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', verbose_name='user permissions', blank=True)),
            ],
            options={
                'default_permissions': [],
                'permissions': ((b'admin_add_user', b'ADMIN: Can add user'), (b'admin_change_user', b'ADMIN: Can change user'), (b'admin_delete_user', b'ADMIN: Can delete user'), (b'admin_view_user', b'ADMIN: Can view users'), (b'admin_add_admin_user', b'ADMIN: Can add admin user'), (b'admin_change_admin_user', b'ADMIN: Can change admin user'), (b'admin_delete_admin_user', b'ADMIN: Can delete admin user'), (b'admin_view_admin_user', b'ADMIN: Can view admin users')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'name')),
                ('continent', models.CharField(max_length=30, verbose_name=b'continent')),
                ('code', models.CharField(max_length=2, verbose_name=b'code')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=15, verbose_name=b'name')),
                ('code', models.CharField(max_length=5, verbose_name=b'code')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255, verbose_name=b'description')),
                ('help_text', models.TextField(null=True, verbose_name=b'help text', blank=True)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPersonal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('birth_date', models.DateField(verbose_name=b'birth date')),
                ('gender', models.CharField(max_length=1, choices=[(b'F', b'Femanle'), (b'M', b'Male')])),
                ('country', models.ForeignKey(to='core.Country')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

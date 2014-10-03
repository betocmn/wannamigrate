# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='e-mail')),
                ('name', models.CharField(max_length=120, default='', null=True, verbose_name='name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is admin?')),
                ('groups', models.ManyToManyField(verbose_name='groups', related_query_name='user', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_name='user_set', blank=True)),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_query_name='user', to='auth.Permission', help_text='Specific permissions for this user.', related_name='user_set', blank=True)),
            ],
            options={
                'default_permissions': [],
                'permissions': (('admin_add_user', 'ADMIN: Can add user'), ('admin_change_user', 'ADMIN: Can change user'), ('admin_delete_user', 'ADMIN: Can delete user'), ('admin_view_user', 'ADMIN: Can view users'), ('admin_add_admin_user', 'ADMIN: Can add admin user'), ('admin_change_admin_user', 'ADMIN: Can change admin user'), ('admin_delete_admin_user', 'ADMIN: Can delete admin user'), ('admin_view_admin_user', 'ADMIN: Can view admin users')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('description', models.CharField(max_length=255, verbose_name='Answer')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnswerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('code', models.CharField(max_length=2, verbose_name='code')),
                ('immigration_enabled', models.BooleanField(default=False, verbose_name='immigration enabled?')),
                ('continent', models.ForeignKey(verbose_name='continent', to='core.Continent')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CountryPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('points', models.IntegerField(verbose_name='points')),
                ('answer', models.ForeignKey(verbose_name='answer', to='core.Answer')),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=25, verbose_name='name')),
                ('code', models.CharField(max_length=6, verbose_name='code')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('description', models.CharField(max_length=255, verbose_name='question')),
                ('help_text', models.TextField(null=True, verbose_name='help text', blank=True)),
            ],
            options={
                'default_permissions': [],
                'permissions': (('admin_add_immigration_rule', 'ADMIN: Can add immigration rule'), ('admin_change_immigration_rule', 'ADMIN: Can change immigration rule'), ('admin_delete_immigration_rule', 'ADMIN: Can delete immigration rule'), ('admin_view_immigration_rule', 'ADMIN: Can view immigration rules')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('school', models.CharField(max_length=100, verbose_name='school')),
                ('year_start', models.CharField(max_length=4, verbose_name='start year')),
                ('year_end', models.CharField(max_length=4, verbose_name='end year')),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
                ('education_field_answer', models.ForeignKey(verbose_name='education field', to='core.Answer', related_name='education_field')),
                ('education_level_answer', models.ForeignKey(verbose_name='education level', to='core.Answer', related_name='education_level')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('language', models.ForeignKey(verbose_name='language', to='core.Language')),
                ('language_level_answer', models.ForeignKey(verbose_name='language level', on_delete=django.db.models.deletion.PROTECT, to='core.Answer')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('birth_date', models.DateField(verbose_name='birth date')),
                ('gender', models.CharField(max_length=1, choices=[('F', 'Femanle'), ('M', 'Male')], verbose_name='gender')),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('score', models.IntegerField(verbose_name='score')),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserWork',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('company', models.CharField(max_length=100, verbose_name='company')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
                ('occupation_answer', models.ForeignKey(verbose_name='occupation', to='core.Answer')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answercategory',
            name='question',
            field=models.ForeignKey(verbose_name='question', to='core.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_category',
            field=models.ForeignKey(null=True, verbose_name='category', to='core.AnswerCategory', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name='question', to='core.Question'),
            preserve_default=True,
        ),
    ]

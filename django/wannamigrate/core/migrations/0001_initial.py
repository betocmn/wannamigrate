# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('email', models.EmailField(max_length=255, verbose_name='e-mail', unique=True)),
                ('name', models.CharField(default='', max_length=120, verbose_name='name', null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is admin?')),
                ('groups', models.ManyToManyField(blank=True, verbose_name='groups', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, verbose_name='user permissions', related_name='user_set', help_text='Specific permissions for this user.', related_query_name='user', to='auth.Permission')),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('description', models.CharField(max_length=255, verbose_name='question')),
                ('help_text', models.TextField(blank=True, verbose_name='help text', null=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('regional_australia_study', models.BooleanField(default=False, verbose_name='studied in regional australia?')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserEducationHistory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('school', models.CharField(max_length=100, verbose_name='school')),
                ('year_start', models.CharField(max_length=4, verbose_name='start year')),
                ('year_end', models.CharField(max_length=4, verbose_name='end year')),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
                ('education_level_answer', models.ForeignKey(verbose_name='education level', related_name='education_level', to='core.Answer')),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('australian_community_language', models.BooleanField(default=False, verbose_name='credentialled community language in australia?')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLanguageProficiency',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('language', models.ForeignKey(verbose_name='language', to='core.Language')),
                ('language_level_answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='language level', to='core.Answer')),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('birth_date', models.DateField(verbose_name='birth date')),
                ('gender', models.CharField(max_length=1, verbose_name='gender', choices=[('F', 'Female'), ('M', 'Male')])),
                ('australian_regional_immigration', models.BooleanField(default=False, verbose_name='willing to move to regional australia?')),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPersonalFamily',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('partner_skills', models.BooleanField(default=False, verbose_name='partner skills?')),
                ('willing_to_invest', models.BooleanField(default=False, verbose_name='willing to invest?')),
                ('canadian_startup_letter', models.BooleanField(default=False, verbose_name='startup letter from canada?')),
                ('australian_professional_year', models.BooleanField(default=False, verbose_name='professional year course in australia?')),
                ('occupation_answer', models.ForeignKey(verbose_name='occupation', to='core.Answer')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserWorkExperience',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
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
        migrations.CreateModel(
            name='UserWorkOffer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
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
            field=models.ForeignKey(blank=True, verbose_name='category', to='core.AnswerCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name='question', to='core.Question'),
            preserve_default=True,
        ),
    ]

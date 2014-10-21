# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion
import django.utils.timezone


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
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('email', models.EmailField(max_length=255, verbose_name='e-mail', unique=True)),
                ('name', models.CharField(verbose_name='name', null=True, max_length=120, default='')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is admin?')),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='groups', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_name='user_set')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', verbose_name='user permissions', related_query_name='user', help_text='Specific permissions for this user.', blank=True, related_name='user_set')),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('regional_australia_study', models.BooleanField(default=False, verbose_name='studied in regional australia?')),
                ('partner_education_level_answer', models.ForeignKey(null=True, verbose_name='partner education level', to='core.Answer', related_name='partner_education_level_answer')),
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
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('school', models.CharField(max_length=100, verbose_name='school')),
                ('year_start', models.CharField(max_length=4, verbose_name='start year')),
                ('year_end', models.CharField(max_length=4, verbose_name='end year')),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('australian_community_language', models.BooleanField(default=False, verbose_name='credentialled community language in australia?')),
                ('partner_english_level_answer', models.ForeignKey(null=True, verbose_name='partner english level', to='core.Answer', related_name='partner_english_level_answer', on_delete=django.db.models.deletion.PROTECT)),
                ('partner_french_level_answer', models.ForeignKey(null=True, verbose_name='partner french level', to='core.Answer', related_name='partner_french_level_answer', on_delete=django.db.models.deletion.PROTECT)),
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
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('language', models.ForeignKey(verbose_name='language', to='core.Language')),
                ('language_level_answer', models.ForeignKey(verbose_name='language level', to='core.Answer', on_delete=django.db.models.deletion.PROTECT)),
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
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('birth_date', models.DateField(verbose_name='birth date')),
                ('gender', models.CharField(max_length=1, verbose_name='gender', choices=[('F', 'Female'), ('M', 'Male')])),
                ('australian_regional_immigration', models.BooleanField(default=False, verbose_name='willing to move to regional australia?')),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user')),
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
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
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
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('score_total', models.IntegerField(verbose_name='total score')),
                ('score_personal', models.IntegerField(verbose_name='score personal')),
                ('score_language', models.IntegerField(verbose_name='score language')),
                ('score_education', models.IntegerField(verbose_name='score education')),
                ('score_work', models.IntegerField(verbose_name='score work')),
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
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('partner_skills', models.BooleanField(default=False, verbose_name='partner skills?')),
                ('willing_to_invest', models.BooleanField(default=False, verbose_name='willing to invest?')),
                ('canadian_startup_letter', models.BooleanField(default=False, verbose_name='startup letter from canada?')),
                ('australian_professional_year', models.BooleanField(default=False, verbose_name='professional year course in australia?')),
                ('canadian_partner_work_study_experience', models.BooleanField(default=False, verbose_name='has partner worked or studied in canada?')),
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
        migrations.CreateModel(
            name='UserWorkOffer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
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

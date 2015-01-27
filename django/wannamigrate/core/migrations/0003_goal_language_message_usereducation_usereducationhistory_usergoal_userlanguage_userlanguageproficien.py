# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import stdimage.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
        ('core', '0002_auto_20150126_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=100)),
                ('is_active', models.BooleanField(verbose_name='is active', default=True)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=25)),
                ('code', models.CharField(verbose_name='code', max_length=6)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('content', models.TextField(verbose_name='comment')),
                ('is_read', models.BooleanField(verbose_name='is read', default=False)),
                ('from_user', models.ForeignKey(verbose_name='from user', related_name='message_from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(verbose_name='to user', related_name='message_to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('regional_australia_study', models.NullBooleanField(verbose_name='Did you complete any studies in a regional part of Australia', choices=[(True, 'Yes'), (False, 'No')], default=None)),
                ('partner_education_level_answer', models.ForeignKey(verbose_name='partner/spouse education level', related_name='partner_education_level_answer', null=True, to='points.Answer', blank=True)),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserEducationHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('school', models.CharField(verbose_name='school/university', max_length=100)),
                ('year_start', models.CharField(verbose_name='start year', max_length=4)),
                ('year_end', models.CharField(verbose_name='end year', max_length=4)),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
                ('education_level_answer', models.ForeignKey(verbose_name='education level', related_name='education_level', to='points.Answer')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserGoal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('from_country', models.ForeignKey(verbose_name='from country', related_name='from_country', to='core.Country')),
                ('goal', models.ForeignKey(verbose_name='goal', to='core.Goal')),
                ('to_country', models.ForeignKey(verbose_name='to country', related_name='to_country', to='core.Country')),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLanguage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('partner_english_level_answer', models.ForeignKey(verbose_name='partner/spouse english level', related_name='partner_english_level_answer', null=True, to='points.Answer', blank=True, on_delete=django.db.models.deletion.PROTECT)),
                ('partner_french_level_answer', models.ForeignKey(verbose_name='partner/spouse french level', related_name='partner_french_level_answer', null=True, to='points.Answer', blank=True, on_delete=django.db.models.deletion.PROTECT)),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLanguageProficiency',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('language', models.ForeignKey(verbose_name='language', to='core.Language')),
                ('language_level_answer', models.ForeignKey(verbose_name='language level', on_delete=django.db.models.deletion.PROTECT, to='points.Answer')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLoginHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('is_logout', models.BooleanField(verbose_name='is logout', default=False)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('avatar', stdimage.models.StdImageField(verbose_name='avatar', upload_to='user_pictures', null=True, blank=True)),
                ('birth_date', models.DateField(verbose_name='birth date', null=True, blank=True)),
                ('gender', models.CharField(verbose_name='gender', choices=[('F', 'Female'), ('M', 'Male')], null=True, blank=True, max_length=1, default=None)),
                ('australian_regional_immigration', models.NullBooleanField(verbose_name='Would you be willing to live in Regional Australia', choices=[(True, 'Yes'), (False, 'No')], default=None)),
                ('family_overseas', models.NullBooleanField(verbose_name='Any family members who are citizens in other countries', choices=[(True, 'Yes'), (False, 'No')], default=None)),
                ('country', models.ForeignKey(verbose_name='country of citizenship', null=True, to='core.Country', blank=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
            name='UserStats',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('percentage_personal', models.IntegerField(verbose_name='percentage personal', default=0, null=True, blank=True)),
                ('percentage_language', models.IntegerField(verbose_name='percentage language', default=0, null=True, blank=True)),
                ('percentage_education', models.IntegerField(verbose_name='percentage education', default=0, null=True, blank=True)),
                ('percentage_work', models.IntegerField(verbose_name='percentage work', default=0, null=True, blank=True)),
                ('updating_now', models.BooleanField(verbose_name='updating now', default=False)),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserWork',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('partner_skills', models.NullBooleanField(verbose_name='Do you have a partner/spouse with proved skills', choices=[(True, 'Yes'), (False, 'No')], default=None)),
                ('willing_to_invest', models.NullBooleanField(verbose_name='are you willing to invest money on the country of destination', choices=[(True, 'Yes'), (False, 'No')], default=None)),
                ('canadian_startup_letter', models.NullBooleanField(verbose_name='do you have a startup recommendation letter approved by canada', choices=[(True, 'Yes'), (False, 'No')], default=None)),
                ('australian_professional_year', models.NullBooleanField(verbose_name='Did you complete a Professional Year Course in Australia', choices=[(True, 'Yes'), (False, 'No')], default=None)),
                ('canadian_partner_work_study_experience', models.NullBooleanField(verbose_name='If you have a partner/spouse, has he/she worked or studied in Canada', choices=[(True, 'Yes'), (False, 'No')], default=None)),
                ('work_offer', models.NullBooleanField(verbose_name='Do you have a work offer overseas', choices=[(True, 'Yes'), (False, 'No')], default=None)),
                ('occupation', models.ForeignKey(verbose_name='occupation', null=True, to='points.Occupation', blank=True)),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserWorkExperience',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('company', models.CharField(verbose_name='company', max_length=100)),
                ('months', models.PositiveSmallIntegerField(verbose_name='Duration of Employment')),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
    ]

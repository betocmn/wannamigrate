# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_countrypoints'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('admin_add_user', 'ADMIN: Can add user'), ('admin_change_user', 'ADMIN: Can change user'), ('admin_delete_user', 'ADMIN: Can delete user'), ('admin_view_user', 'ADMIN: Can view users'), ('admin_add_admin_user', 'ADMIN: Can add admin user'), ('admin_change_admin_user', 'ADMIN: Can change admin user'), ('admin_delete_admin_user', 'ADMIN: Can delete admin user'), ('admin_view_admin_user', 'ADMIN: Can view admin users')), 'default_permissions': []},
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='description',
            field=models.CharField(max_length=255, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='core.Question', verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=2, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.CharField(max_length=30, verbose_name='continent'),
        ),
        migrations.AlterField(
            model_name='country',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='country',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='countrypoints',
            name='answer',
            field=models.ForeignKey(to='core.Answer', verbose_name='answer'),
        ),
        migrations.AlterField(
            model_name='countrypoints',
            name='country',
            field=models.ForeignKey(to='core.Country', verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='countrypoints',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='countrypoints',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='countrypoints',
            name='points',
            field=models.IntegerField(verbose_name='points'),
        ),
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=5, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='language',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='language',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=15, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=255, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='question',
            name='help_text',
            field=models.TextField(null=True, blank=True, verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='question',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', related_name='user_set', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(verbose_name='is active?', default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(verbose_name='is admin?', default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(null=True, max_length=120, verbose_name='name', default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_query_name='user', help_text='Specific permissions for this user.', to='auth.Permission', related_name='user_set', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='country',
            field=models.ForeignKey(to='core.Country', verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='education_field_answer',
            field=models.ForeignKey(to='core.Answer', related_name='education_field', verbose_name='education field'),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='education_level_answer',
            field=models.ForeignKey(to='core.Answer', related_name='education_level', verbose_name='education level'),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='school',
            field=models.CharField(max_length=100, verbose_name='school'),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='year_end',
            field=models.CharField(max_length=4, verbose_name='end year'),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='year_start',
            field=models.CharField(max_length=4, verbose_name='start year'),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='language',
            field=models.ForeignKey(to='core.Language', verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='language_level_answer',
            field=models.ForeignKey(to='core.Answer', verbose_name='language level'),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='birth_date',
            field=models.DateField(verbose_name='birth date'),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='country',
            field=models.ForeignKey(to='core.Country', verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='gender',
            field=models.CharField(choices=[('F', 'Femanle'), ('M', 'Male')], max_length=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='country',
            field=models.ForeignKey(to='core.Country', verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='score',
            field=models.IntegerField(verbose_name='score'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='company',
            field=models.CharField(max_length=100, verbose_name='company'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='country',
            field=models.ForeignKey(to='core.Country', verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='end_date',
            field=models.DateField(verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='occupation_answer',
            field=models.ForeignKey(to='core.Answer', verbose_name='occupation'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='start_date',
            field=models.DateField(verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]

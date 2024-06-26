# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-01 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wannamigrate.core.util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_auto_20170330_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('file', models.FileField(upload_to=wannamigrate.core.util.CustomUploadToAutoSlugClassNameDir('name'))),
                ('sort_order', models.PositiveSmallIntegerField(default=1, verbose_name='sort order')),
                ('doc_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Doc', verbose_name='doc')),
            ],
            options={
                'permissions': (('admin_add_doc', 'ADMIN: Can add doc'), ('admin_change_doc', 'ADMIN: Can change doc'), ('admin_delete_doc', 'ADMIN: Can delete doc'), ('admin_view_doc', 'ADMIN: Can view docs')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='DocGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('sort_order', models.PositiveSmallIntegerField(default=1, verbose_name='sort order')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Country', verbose_name='country')),
            ],
            options={
                'permissions': (('admin_add_doc_group', 'ADMIN: Can add doc_group'), ('admin_change_doc_group', 'ADMIN: Can change doc_group'), ('admin_delete_doc_group', 'ADMIN: Can delete doc_group'), ('admin_view_doc_group', 'ADMIN: Can view doc_groups')),
                'default_permissions': [],
            },
        ),
    ]

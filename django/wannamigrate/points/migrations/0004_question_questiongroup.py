# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_auto_20150115_1430'),
        ('points', '0003_auto_20150115_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('description', models.CharField(verbose_name='question', max_length=255)),
                ('help_text', models.TextField(verbose_name='help text', null=True, blank=True)),
                ('method_name', models.CharField(verbose_name='method name', max_length=60)),
                ('type', models.CharField(verbose_name='type', max_length=15)),
            ],
            options={
                'default_permissions': [],
                'permissions': (('admin_add_immigration_rule', 'ADMIN: Can add immigration rule'), ('admin_change_immigration_rule', 'ADMIN: Can change immigration rule'), ('admin_delete_immigration_rule', 'ADMIN: Can delete immigration rule'), ('admin_view_immigration_rule', 'ADMIN: Can view immigration rules')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.TextField(verbose_name='name')),
                ('max_points', models.IntegerField(verbose_name='max points allowed', default=0)),
                ('country', models.ForeignKey(to='core.Country', related_name='country_new', verbose_name='country')),
                ('questions', models.ManyToManyField(to='points.Question', db_constraint='questions_new')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

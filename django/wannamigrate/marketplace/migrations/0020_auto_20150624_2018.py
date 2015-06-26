# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0019_auto_20150518_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(verbose_name='name', max_length=120)),
                ('description', models.TextField(verbose_name='description')),
                ('is_active', models.BooleanField(verbose_name='is active', default=True)),
                ('icon_css_class', models.CharField(verbose_name='name', max_length=30)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(verbose_name='name', max_length=40)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(to='marketplace.ProductCategory', verbose_name='category'),
            preserve_default=True,
        ),
    ]

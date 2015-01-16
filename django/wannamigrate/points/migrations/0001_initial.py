# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_auto_20150105_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=180)),
                ('countries', models.ManyToManyField(to='core.Country', related_name='new_countries')),
            ],
            options={
                'permissions': (('admin_add_occupation', 'ADMIN: Can add occupation'), ('admin_change_occupation', 'ADMIN: Can change occupation'), ('admin_delete_occupation', 'ADMIN: Can delete occupation'), ('admin_view_occupation', 'ADMIN: Can view occupations')),
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OccupationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='occupation',
            name='occupation_category',
            field=models.ForeignKey(related_name='new_occupation_category', to='points.OccupationCategory', verbose_name='category'),
            preserve_default=True,
        ),
    ]

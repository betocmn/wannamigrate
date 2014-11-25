# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20141125_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryOccupation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('description', models.CharField(verbose_name='Name', max_length=180)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OccupationCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
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
            field=models.ForeignKey(verbose_name='category', to='core.OccupationCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='countryoccupation',
            name='occupation',
            field=models.ForeignKey(verbose_name='occupation', to='core.Occupation'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='countryoccupation',
            unique_together=set([('occupation', 'country')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150224_1800'),
        ('marketplace', '0010_auto_20150407_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderCountry',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('country', models.ForeignKey(verbose_name='country', to='core.Country')),
                ('provider', models.ForeignKey(verbose_name='provider', to='marketplace.Provider')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProviderLanguage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('language', models.ForeignKey(verbose_name='language', to='core.Language')),
                ('provider', models.ForeignKey(verbose_name='provider', to='marketplace.Provider')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProviderServiceType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('price', models.DecimalField(max_digits=5, verbose_name='price', decimal_places=2)),
                ('is_top', models.BooleanField(verbose_name='is top service', default=False)),
                ('provider', models.ForeignKey(verbose_name='provider', to='marketplace.Provider')),
                ('service_type', models.ForeignKey(verbose_name='service type', to='marketplace.ServiceType')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='providerservicetype',
            unique_together=set([('service_type', 'provider')]),
        ),
        migrations.AlterUniqueTogether(
            name='providerlanguage',
            unique_together=set([('language', 'provider')]),
        ),
        migrations.AlterUniqueTogether(
            name='providercountry',
            unique_together=set([('country', 'provider')]),
        ),
        migrations.AddField(
            model_name='provider',
            name='countries',
            field=models.ManyToManyField(to='core.Country', through='marketplace.ProviderCountry', related_name='countries'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='languages',
            field=models.ManyToManyField(to='core.Language', through='marketplace.ProviderLanguage', related_name='languages'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='service_types',
            field=models.ManyToManyField(to='marketplace.ServiceType', through='marketplace.ProviderServiceType', related_name='service_types'),
            preserve_default=True,
        ),
    ]

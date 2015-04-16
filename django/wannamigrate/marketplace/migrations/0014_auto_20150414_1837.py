# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0013_auto_20150408_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=45)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='provider',
            name='regulator',
            field=models.ForeignKey(null=True, verbose_name='regulator', to='marketplace.Regulator', blank=True),
            preserve_default=True,
        ),
    ]

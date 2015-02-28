# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_provider_review_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceTypeCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(verbose_name='name', max_length=40)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

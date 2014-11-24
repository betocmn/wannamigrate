# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20141123_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('percentage_personal', models.IntegerField(verbose_name='percentage personal')),
                ('percentage_language', models.IntegerField(verbose_name='percentage language')),
                ('percentage_education', models.IntegerField(verbose_name='percentage education')),
                ('percentage_work', models.IntegerField(verbose_name='percentage work')),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20150520_1629'),
        ('qa', '0004_auto_20150521_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('language', models.ForeignKey(related_name='topics_translations', to='core.Language')),
                ('topic', models.ForeignKey(related_name='translations', to='qa.Topic')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

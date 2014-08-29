# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_userlanguage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('school', models.CharField(max_length=100)),
                ('year_start', models.CharField(max_length=4)),
                ('year_end', models.CharField(max_length=4)),
                ('country', models.ForeignKey(to='core.Country')),
                ('education_field_answer', models.ForeignKey(to='core.Answer')),
                ('education_level_answer', models.ForeignKey(to='core.Answer')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

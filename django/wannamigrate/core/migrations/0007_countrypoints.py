# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_userresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryPoints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('points', models.IntegerField()),
                ('answer', models.ForeignKey(to='core.Answer')),
                ('country', models.ForeignKey(to='core.Country')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
    ]

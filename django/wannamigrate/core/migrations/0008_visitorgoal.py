# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_preferred_timezone'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorGoal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('from_country', models.ForeignKey(verbose_name='from country', to='core.Country', related_name='visitor_from_country')),
                ('goal', models.ForeignKey(verbose_name='goal', to='core.Goal')),
                ('to_country', models.ForeignKey(verbose_name='to country', to='core.Country', related_name='visitor_to_country')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

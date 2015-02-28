# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_preferred_timezone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('total_users', models.IntegerField(default=1, verbose_name='total users')),
                ('total_visitors', models.IntegerField(default=1, verbose_name='total visitors')),
                ('from_country', models.ForeignKey(verbose_name='from country', to='core.Country', related_name='visitor_from_country')),
                ('goal', models.ForeignKey(verbose_name='goal', to='core.Goal')),
                ('to_country', models.ForeignKey(verbose_name='to country', to='core.Country', related_name='visitor_to_country')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSituation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('situation', models.ForeignKey(verbose_name='situation', to='core.Situation')),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='usergoal',
            name='from_country',
        ),
        migrations.RemoveField(
            model_name='usergoal',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='usergoal',
            name='to_country',
        ),
        migrations.RemoveField(
            model_name='usergoal',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserGoal',
        ),
    ]

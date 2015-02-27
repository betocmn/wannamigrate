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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('total_users', models.IntegerField(default=1, verbose_name='total users')),
                ('total_visitors', models.IntegerField(default=1, verbose_name='total visitors')),
                ('from_country', models.ForeignKey(to='core.Country', verbose_name='from country', related_name='visitor_from_country')),
                ('goal', models.ForeignKey(to='core.Goal', verbose_name='goal')),
                ('to_country', models.ForeignKey(to='core.Country', verbose_name='to country', related_name='visitor_to_country')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSituation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('situation', models.ForeignKey(to='core.Situation', verbose_name='situation')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user')),
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
        migrations.AddField(
            model_name='userstats',
            name='total_answers',
            field=models.IntegerField(verbose_name='total answers', blank=True, default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_contracts',
            field=models.IntegerField(verbose_name='total contracts', blank=True, default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_profile_views',
            field=models.IntegerField(verbose_name='total profile views', blank=True, default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_questions',
            field=models.IntegerField(verbose_name='total questions', blank=True, default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_reviews',
            field=models.IntegerField(verbose_name='total reviews', blank=True, default=0, null=True),
            preserve_default=True,
        ),
    ]

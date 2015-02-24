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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('total_users', models.IntegerField(verbose_name='total users', default=1)),
                ('total_visitors', models.IntegerField(verbose_name='total visitors', default=1)),
                ('from_country', models.ForeignKey(verbose_name='from country', related_name='visitor_from_country', to='core.Country')),
                ('goal', models.ForeignKey(verbose_name='goal', to='core.Goal')),
                ('to_country', models.ForeignKey(verbose_name='to country', related_name='visitor_to_country', to='core.Country')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSituation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
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
        migrations.AddField(
            model_name='userstats',
            name='total_answers',
            field=models.IntegerField(verbose_name='total answers', default=0, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_contracts',
            field=models.IntegerField(verbose_name='total contracts', default=0, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_profile_views',
            field=models.IntegerField(verbose_name='total profile views', default=0, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_questions',
            field=models.IntegerField(verbose_name='total questions', default=0, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstats',
            name='total_reviews',
            field=models.IntegerField(verbose_name='total reviews', default=0, blank=True, null=True),
            preserve_default=True,
        ),
    ]

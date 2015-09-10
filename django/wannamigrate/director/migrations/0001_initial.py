# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20150721_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MissionsObjectives',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('optional', models.BooleanField(default=False)),
                ('mission', models.ForeignKey(to='director.Mission')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('content_url', models.TextField()),
                ('content_progress_url', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SituationsMissions',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('mission', models.ForeignKey(to='director.Mission')),
                ('situation', models.ForeignKey(to='core.Situation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='situationsmissions',
            unique_together=set([('situation', 'mission'), ('situation', 'order')]),
        ),
        migrations.AddField(
            model_name='missionsobjectives',
            name='objective',
            field=models.ForeignKey(to='director.Objective'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='missionsobjectives',
            unique_together=set([('mission', 'order'), ('mission', 'objective')]),
        ),
        migrations.AddField(
            model_name='mission',
            name='objectives',
            field=models.ManyToManyField(related_name='missions', through='director.MissionsObjectives', to='director.Objective'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='situations',
            field=models.ManyToManyField(related_name='missions', through='director.SituationsMissions', to='core.Situation'),
            preserve_default=True,
        ),
    ]

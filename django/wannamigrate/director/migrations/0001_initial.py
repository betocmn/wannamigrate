# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0026_auto_20150721_1419'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('question', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormContentChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('text', models.CharField(max_length=200)),
                ('progress_amount', models.IntegerField()),
                ('form', models.ForeignKey(to='director.FormContent', related_name='choices')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormContentUserChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('choice', models.ForeignKey(to='director.FormContentChoice')),
                ('form', models.ForeignKey(to='director.FormContent')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GenericContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('layout', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GenericContainerContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('order', models.IntegerField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_module', models.CharField(max_length=200)),
                ('container', models.ForeignKey(to='director.GenericContainer', related_name='contents')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HtmlContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('html', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HtmlContentUserProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('progress', models.IntegerField()),
                ('html', models.ForeignKey(to='director.HtmlContent')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IframeContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('url', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IframeContentUserProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('progress', models.IntegerField()),
                ('iframe', models.ForeignKey(to='director.IframeContent')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_module', models.CharField(max_length=200)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RedirectContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('url', models.CharField(max_length=300)),
                ('progress_url', models.CharField(max_length=300)),
                ('blank', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SituationsMissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
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
            unique_together=set([('mission', 'objective'), ('mission', 'order')]),
        ),
        migrations.AddField(
            model_name='mission',
            name='objectives',
            field=models.ManyToManyField(to='director.Objective', related_name='missions', through='director.MissionsObjectives'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='situations',
            field=models.ManyToManyField(to='core.Situation', related_name='missions', through='director.SituationsMissions'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='iframecontentuserprogress',
            unique_together=set([('iframe', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='htmlcontentuserprogress',
            unique_together=set([('html', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='formcontentuserchoice',
            unique_together=set([('user', 'form')]),
        ),
    ]

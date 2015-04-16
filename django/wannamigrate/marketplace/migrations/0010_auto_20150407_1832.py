# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketplace', '0009_servicetype_icon_css_class'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='provider_servicetypes',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='provider_servicetypes',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='provider_servicetypes',
            name='service_type',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='countries',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='service_types',
        ),
        migrations.DeleteModel(
            name='Provider_ServiceTypes',
        ),
        migrations.RemoveField(
            model_name='service',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='service',
            name='to_user',
        ),
        migrations.AddField(
            model_name='service',
            name='provider',
            field=models.ForeignKey(default='1', verbose_name='service provider', to='marketplace.Provider'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='user',
            field=models.ForeignKey(default='1', verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='provider',
            name='display_name',
            field=models.CharField(max_length=80, verbose_name='professional display name'),
            preserve_default=True,
        ),
    ]

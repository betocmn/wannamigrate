# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_remove_user_country_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country_results',
            field=models.ManyToManyField(through='core.UserResult', to='core.Country'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='userresult',
            unique_together=set([('user', 'country')]),
        ),
    ]

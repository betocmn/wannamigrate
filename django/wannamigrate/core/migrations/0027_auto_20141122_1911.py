# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20141122_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='immigration_enabled',
            field=models.BooleanField(default=False, verbose_name='immigration enabled'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='is admin'),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='australian_community_language',
            field=models.BooleanField(default=False, verbose_name='credentialled community language in australia'),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='australian_regional_immigration',
            field=models.NullBooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, verbose_name='Would you be willing to live in Regional Australia'),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='family_overseas',
            field=models.NullBooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, verbose_name='Any family members who are citizens in other countries'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='partner_skills',
            field=models.NullBooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, verbose_name='Do you have a partner with proved skills'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_userpersonal_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereducation',
            name='partner_education_level_answer',
            field=models.ForeignKey(related_name='partner_education_level_answer', null=True, to='core.Answer', verbose_name='partner education level', blank=True),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='partner_english_level_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='partner_english_level_answer', null=True, to='core.Answer', verbose_name='partner english level', blank=True),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='partner_french_level_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='partner_french_level_answer', null=True, to='core.Answer', verbose_name='partner french level', blank=True),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='birth date', blank=True),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='country',
            field=models.ForeignKey(null=True, to='core.Country', verbose_name='country', blank=True),
        ),
        migrations.AlterField(
            model_name='userpersonal',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], verbose_name='gender', max_length=1, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='occupation_answer',
            field=models.ForeignKey(null=True, to='core.Answer', verbose_name='occupation', blank=True),
        ),
    ]

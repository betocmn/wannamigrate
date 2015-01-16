# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_auto_20150115_1443'),
        ('points', '0008_auto_20150115_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='points',
            field=models.ManyToManyField(through='points.CountryPoints', to='core.Country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='partner_education_level_answer',
            field=models.ForeignKey(null=True, blank=True, related_name='partner_education_level_answer', verbose_name='partner/spouse education level', to='points.Answer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usereducationhistory',
            name='education_level_answer',
            field=models.ForeignKey(related_name='education_level', verbose_name='education level', to='points.Answer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='partner_english_level_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, related_name='partner_english_level_answer', verbose_name='partner/spouse english level', to='points.Answer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='partner_french_level_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, related_name='partner_french_level_answer', verbose_name='partner/spouse french level', to='points.Answer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlanguageproficiency',
            name='language_level_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='points.Answer', verbose_name='language level'),
            preserve_default=True,
        ),
    ]

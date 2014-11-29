# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20141127_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereducation',
            name='partner_education_level_answer',
            field=models.ForeignKey(null=True, related_name='partner_education_level_answer', verbose_name='partner/spouse education level', to='core.Answer', blank=True),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='regional_australia_study',
            field=models.NullBooleanField(verbose_name='Did you complete any studies in a regional part of australia', default=None, choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='partner_english_level_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='partner_english_level_answer', verbose_name='partner/spouse english level', to='core.Answer', blank=True),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='partner_french_level_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='partner_french_level_answer', verbose_name='partner/spouse french level', to='core.Answer', blank=True),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='canadian_partner_work_study_experience',
            field=models.NullBooleanField(verbose_name='If you have a partner/spouse, has he/she worked or studied in Canada', default=None, choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='partner_skills',
            field=models.NullBooleanField(verbose_name='Do you have a partner/spouse with proved skills', default=None, choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]

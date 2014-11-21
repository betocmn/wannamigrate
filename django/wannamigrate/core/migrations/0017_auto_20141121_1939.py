# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20141121_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwork',
            name='partner_skills',
        ),
        migrations.RemoveField(
            model_name='userworkexperience',
            name='occupation_answer',
        ),
        migrations.AddField(
            model_name='userwork',
            name='partner_occupation_answer',
            field=models.ForeignKey(related_name='partner_occupation_answer', null=True, blank=True, to='core.Answer', verbose_name='partner occupation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userwork',
            name='australian_professional_year',
            field=models.NullBooleanField(default=None, verbose_name='Did you complete a Professional Year Course in Australia', choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='canadian_partner_work_study_experience',
            field=models.NullBooleanField(default=None, verbose_name='If you have a partner, has he/she worked or studied in Canada', choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='canadian_startup_letter',
            field=models.NullBooleanField(default=None, verbose_name='do you have a startup letter from canada', choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='occupation_answer',
            field=models.ForeignKey(related_name='occupation_answer', null=True, blank=True, to='core.Answer', verbose_name='occupation'),
        ),
        migrations.AlterField(
            model_name='userwork',
            name='willing_to_invest',
            field=models.NullBooleanField(default=None, verbose_name='are you willing to invest money', choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]

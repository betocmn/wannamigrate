# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150522_0547'),
        ('qa', '0009_auto_20150522_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='language',
            field=models.ForeignKey(related_name='related_blogpost', to='core.Language', default=107),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='language',
            field=models.ForeignKey(related_name='related_question', to='core.Language', default=107),
            preserve_default=False,
        ),
    ]

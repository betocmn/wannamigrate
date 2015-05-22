# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_topictranslation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topictranslation',
            options={'permissions': (('admin_add_topic_translation', '[ADMIN] Can add topic translation'), ('admin_edit_topic_translation', '[ADMIN] Can edit topic translation'), ('admin_delete_topic_translation', '[ADMIN] Can delete topic translation'), ('admin_view_topic_translation', '[ADMIN] Can view topic translation'), ('admin_list_topic_translation', '[ADMIN] Can list topic translation')), 'default_permissions': []},
        ),
    ]

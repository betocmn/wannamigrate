# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20150209_1916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('qa_admin_add_post', '[ADMIN] Can add post'), ('qa_admin_edit_post', '[ADMIN] Can edit post'), ('qa_admin_delete_post', '[ADMIN] Can delete post'), ('qa_admin_view_post', '[ADMIN] Can view post'), ('qa_admin_list_post', '[ADMIN] Can list posts')), 'default_permissions': []},
        ),
        migrations.AlterModelOptions(
            name='posthistory',
            options={'permissions': (('qa_admin_add_post_history', '[ADMIN] Can add post history'), ('qa_admin_edit_post_history', '[ADMIN] Can edit post history'), ('qa_admin_delete_post_history', '[ADMIN] Can delete post history'), ('qa_admin_view_post_history', '[ADMIN] Can view post history'), ('qa_admin_list_post_history', '[ADMIN] Can list post history')), 'default_permissions': []},
        ),
        migrations.AlterModelOptions(
            name='posttype',
            options={'default_permissions': []},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'permissions': (('qa_admin_add_topic', '[ADMIN] Can add topic'), ('qa_admin_edit_topic', '[ADMIN] Can edit topic'), ('qa_admin_delete_topic', '[ADMIN] Can delete topic'), ('qa_admin_view_topic', '[ADMIN] Can view topic'), ('qa_admin_list_topic', '[ADMIN] Can list topic')), 'default_permissions': []},
        ),
        migrations.AlterModelOptions(
            name='vote',
            options={'permissions': (('qa_admin_add_vote', '[ADMIN] Can add vote'), ('qa_admin_edit_vote', '[ADMIN] Can edit vote'), ('qa_admin_delete_vote', '[ADMIN] Can delete vote'), ('qa_admin_view_vote', '[ADMIN] Can view vote'), ('qa_admin_list_vote', '[ADMIN] Can list vote')), 'default_permissions': []},
        ),
        migrations.AlterModelOptions(
            name='votetype',
            options={'default_permissions': []},
        ),
    ]

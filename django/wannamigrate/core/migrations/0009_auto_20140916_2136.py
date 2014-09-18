# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20140828_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'permissions': (('admin_add_immigration_rule', 'ADMIN: Can add immigration rule'), ('admin_change_immigration_rule', 'ADMIN: Can change immigration rule'), ('admin_delete_immigration_rule', 'ADMIN: Can delete immigration rule'), ('admin_view_immigration_rule', 'ADMIN: Can view immigration rules')), 'default_permissions': []},
        ),
    ]

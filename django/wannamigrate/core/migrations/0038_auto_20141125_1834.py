# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20141125_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occupation',
            options={'default_permissions': [], 'permissions': (('admin_add_occupation', 'ADMIN: Can add occupation'), ('admin_change_occupation', 'ADMIN: Can change occupation'), ('admin_delete_occupation', 'ADMIN: Can delete occupation'), ('admin_view_occupation', 'ADMIN: Can view occupations'))},
        ),
    ]

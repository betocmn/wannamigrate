# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import os
from django.conf import settings




#########################
# Migration functions
#########################
def fix_broken_user_personal_pictures( apps, schema_editor ):
    """
        Fixes broken links from avatars on UserPersonal model.
        :param: apps A reference to the apps.
        :param: schema_editor A reference to the schema_editor.
    """
    # Gets the models
    User = apps.get_model( "core", "User" )
    UserPersonal = apps.get_model( "core", "UserPersonal" )

    data = UserPersonal.objects.all()

    for d in data:
        if d.avatar == '' or not os.path.isfile( "{0}{1}".format( "/wanna/django", d.avatar.url ) ):
            d.avatar = None
        d.save()





class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20150716_2021'),
    ]

    operations = [
        migrations.RunPython( fix_broken_user_personal_pictures ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_new_service_types_for_subscription( apps, schema_editor ):

    # Get model to use (historical version)
    ServiceType = apps.get_model( "marketplace", "ServiceType" )

    # Insert Order Status
    service_type = ServiceType()
    service_type.id = 32
    service_type.name = 'Immi-Box Subscription 1 Year'
    service_type.description = '1 year access to the Immi Box - Immigration Tools.'
    service_type.service_type_category_id = 1
    service_type.is_active = True
    service_type.icon_css_class = 'document'
    service_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0040_auto_20150723_1300'),
    ]

    operations = [
        migrations.RunPython( add_new_service_types_for_subscription ),
    ]

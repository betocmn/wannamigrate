# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

#######################
# ACTIONS
#######################
def add_new_service_price( apps, schema_editor ):

    # Get model to use (historical version)
    ProviderServiceType = apps.get_model( "marketplace", "ProviderServiceType" )

    # Insert Order Status
    provider_service_type = ProviderServiceType()
    provider_service_type.price = 49.00
    provider_service_type.is_top = False
    provider_service_type.provider_id = 13
    provider_service_type.service_type_id = 22
    provider_service_type.save()



class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0031_auto_20150702_2059'),
    ]

    operations = [
        migrations.RunPython( add_new_service_price ),
    ]

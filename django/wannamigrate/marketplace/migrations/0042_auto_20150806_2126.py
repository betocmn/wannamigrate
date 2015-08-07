# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations



#######################
# ACTIONS
#######################
def add_price_for_subscription_plan( apps, schema_editor ):

    # Get model to use (historical version)
    ProviderServiceType = apps.get_model( "marketplace", "ProviderServiceType" )

    # Insert Order Status
    provider_service_type = ProviderServiceType()
    provider_service_type.price = 89.00
    provider_service_type.is_top = False
    provider_service_type.provider_id = 13
    provider_service_type.service_type_id = 32
    provider_service_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0041_auto_20150806_2111'),
    ]

    operations = [
        migrations.RunPython( add_price_for_subscription_plan ),
    ]

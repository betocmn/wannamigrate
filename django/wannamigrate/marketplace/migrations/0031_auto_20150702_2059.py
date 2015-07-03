# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_new_service( apps, schema_editor ):

    # Get model to use (historical version)
    ServiceType = apps.get_model( "marketplace", "ServiceType" )

    # Insert Order Status
    service_type = ServiceType()
    service_type.id = 22
    service_type.name = 'Package - International CV'
    service_type.description = 'You will receive an international CV in english, cover letter and help to build your Linkedin Profile.'
    service_type.service_type_category_id = 4
    service_type.is_active = False
    service_type.icon_css_class = 'headhunting'
    service_type.save()

class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0030_order_boleto_url'),
    ]

    operations = [
        migrations.RunPython( add_new_service ),
    ]

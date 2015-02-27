# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_initial_service_type_categories( apps, schema_editor ):

    # Get model to use (historical version)
    ServiceTypeCategory = apps.get_model( "marketplace", "ServiceTypeCategory" )

    # Insert Order Status
    service_type_category = ServiceTypeCategory()
    service_type_category.id = 1
    service_type_category.name = 'Immigration Consultancy'
    service_type_category.save()

    service_type_category = ServiceTypeCategory()
    service_type_category.id = 2
    service_type_category.name = 'Translation'
    service_type_category.save()

    service_type_category = ServiceTypeCategory()
    service_type_category.id = 3
    service_type_category.name = 'Exchange Student Programs'
    service_type_category.save()

    service_type_category = ServiceTypeCategory()
    service_type_category.id = 4
    service_type_category.name = 'Headhunting'
    service_type_category.save()

    service_type_category = ServiceTypeCategory()
    service_type_category.id = 5
    service_type_category.name = 'Real State'
    service_type_category.save()

    service_type_category = ServiceTypeCategory()
    service_type_category.id = 6
    service_type_category.name = 'Travel Services'
    service_type_category.save()



class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_servicetypecategory'),
    ]

    operations = [
        migrations.RunPython( add_initial_service_type_categories ),
    ]

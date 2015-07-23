# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_new_service_types_for_coaching_services( apps, schema_editor ):

    # Get model to use (historical version)
    ServiceType = apps.get_model( "marketplace", "ServiceType" )

    # Insert Order Status
    service_type = ServiceType()
    service_type.id = 29
    service_type.name = 'Cultural Training'
    service_type.description = 'The goal is to prepare you and your family for the cultural changes you will face while moving to a new country.'
    service_type.service_type_category_id = 1
    service_type.is_active = True
    service_type.icon_css_class = 'exchange'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 30
    service_type.name = 'Career Coaching'
    service_type.description = 'Career assessment in the country of destination, including skype meetings, strategic planning, market evaluation, creation of CV, cover letter, LinkedIn and Portfolio.'
    service_type.service_type_category_id = 4
    service_type.is_active = True
    service_type.icon_css_class = 'headhunting'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 31
    service_type.name = 'Relocation Assessment'
    service_type.description = 'Get help to prepare your relocation plan. You will be assisted in aspects such as renting a house, buying furniture, buying a car and enrolling in school.'
    service_type.service_type_category_id = 6
    service_type.is_active = True
    service_type.icon_css_class = 'housing'
    service_type.save()



class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0039_auto_20150714_1636'),
    ]

    operations = [
        migrations.RunPython( add_new_service_types_for_coaching_services ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_new_service_types( apps, schema_editor ):

    # Get model to use (historical version)
    ServiceType = apps.get_model( "marketplace", "ServiceType" )

    # Insert Order Status
    service_type = ServiceType()
    service_type.id = 25
    service_type.name = 'Study Abroad - Australia I'
    service_type.description = 'Study English abroad in Melbourne, Australia. School: Impact English College. The package includes 24 weeks of english classes, with 20 hours per week, enrollment fees, health insurance for 28 weeks, course material, 4 weeks of accommodation in a family house, individual room, breakfast, dinner, accommodation reservation fee, EdukBrasil fee and visa assessment.'
    service_type.service_type_category_id = 3
    service_type.is_active = True
    service_type.icon_css_class = 'exchange'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 26
    service_type.name = 'Study Abroad - New Zealand I'
    service_type.description = 'Study English abroad in Auckland or Wellington, New Zealand. School: New Zealand Language Centres. The package includes 24 weeks of english classes, with 25 hours per week, enrollment fees, 4 weeks of accommodation in a family house, individual room, breakfast, dinner, accommodation reservation fee, EdukBrasil fee and visa assessment.'
    service_type.service_type_category_id = 3
    service_type.is_active = True
    service_type.icon_css_class = 'exchange'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 27
    service_type.name = 'Study Abroad - Ireland I'
    service_type.description = 'Study English abroad in Dublin, Ireland. School: CES – Centre of English Studies. The package includes 25 weeks of english classes, with 20 hours per week, enrollment fees, 2 weeks of student accommodation, double room, accommodation reservation fee, EdukBrasil fee and public health insurance.'
    service_type.service_type_category_id = 3
    service_type.is_active = True
    service_type.icon_css_class = 'exchange'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 28
    service_type.name = 'Study Abroad - Canada I'
    service_type.description = 'Study English abroad in Toronto or Vancouver, Canada. School: ILAC. The package includes 24 weeks of english classes, with 30 lessons per week, enrollment fees, 4 weeks of accommodation in a family house, individual room, breakfast, lunch, dinner, accommodation reservation fee, EdukBrasil fee and visa assessment.'
    service_type.service_type_category_id = 3
    service_type.is_active = True
    service_type.icon_css_class = 'exchange'
    service_type.save()







class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0033_auto_20150703_1909'),
    ]

    operations = [
        migrations.RunPython( add_new_service_types ),
    ]

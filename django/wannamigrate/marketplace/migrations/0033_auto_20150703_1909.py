# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_new_services( apps, schema_editor ):

    # Get model to use (historical version)
    ServiceType = apps.get_model( "marketplace", "ServiceType" )
    ProviderServiceType = apps.get_model( "marketplace", "ProviderServiceType" )

    # Inserts
    service_type = ServiceType()
    service_type.id = 23
    service_type.name = 'IELTS Express Online Course'
    service_type.description = 'IELTS Express is a fast online preparation course for the IELTS test. Our easy to use, step by step course covers all four IELTS modules. With over 100 activities and approximately 200 study pages, IELTS Express will boost your confidence and help improve your IELTS score.'
    service_type.service_type_category_id = 7
    service_type.is_active = False
    service_type.icon_css_class = 'language'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 24
    service_type.name = 'IELTS Master Online Course'
    service_type.description = 'IELTS Master is a comprehensive online preparation course for the IELTS test. You get 3 months access to our easy to use, step by step course. With four practice tests, recording tools to practice your speaking and online tutors, IELTS Master will boost your confidence and help improve your IELTS score.'
    service_type.service_type_category_id = 7
    service_type.is_active = False
    service_type.icon_css_class = 'language'
    service_type.save()

    # Insert Order Status
    provider_service_type = ProviderServiceType()
    provider_service_type.price = 135.00
    provider_service_type.is_top = False
    provider_service_type.provider_id = 13
    provider_service_type.service_type_id = 23
    provider_service_type.save()

    provider_service_type = ProviderServiceType()
    provider_service_type.price = 250.00
    provider_service_type.is_top = False
    provider_service_type.provider_id = 13
    provider_service_type.service_type_id = 24
    provider_service_type.save()

class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0032_auto_20150702_2104'),
    ]

    operations = [
        migrations.RunPython( add_new_services ),
    ]

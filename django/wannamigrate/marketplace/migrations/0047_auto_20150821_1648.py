# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_consulting_data( apps, schema_editor ):

    # Get model to use (historical version)
    Provider = apps.get_model( "marketplace", "Provider" )
    ServiceType = apps.get_model( "marketplace", "ServiceType" )
    ProviderServiceType = apps.get_model( "marketplace", "ProviderServiceType" )

    # Insert categories
    provider = Provider()
    provider.id = 30
    provider.user_id = 26
    provider.review_score = 5
    provider.provider_status_id = 2
    provider.display_name = 'Humberto Moreira'
    provider.headline = 'CEO - Wanna Migrate'
    provider.description = 'Humberto possui 10 anos de experiência na área de TI e imigração, tendo morado e trabalhado no Chile, Austrália, Estados Unidos e Inglaterra.'
    provider.save()

    # Insert Order Status
    service_type = ServiceType()
    service_type.id = 33
    service_type.name = 'In-Person Individual Evaluation'
    service_type.description = 'In-person individual (or couple) meeting to do your immigration evaluation to Canada and Australia with 1 hour of duration, final report and immigration guides as e-books.'
    service_type.service_type_category_id = 1
    service_type.is_active = True
    service_type.icon_css_class = 'document'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 34
    service_type.name = 'In-Person Group Evaluation'
    service_type.description = 'In-person group meeting to do your immigration evaluation to Canada and Australia with 1 hour of duration, final report and immigration guides as e-books.'
    service_type.service_type_category_id = 1
    service_type.is_active = True
    service_type.icon_css_class = 'document'
    service_type.save()

    provider_service_type = ProviderServiceType()
    provider_service_type.price = 60.00
    provider_service_type.is_top = True
    provider_service_type.provider_id = 30
    provider_service_type.service_type_id = 34
    provider_service_type.save()

    provider_service_type = ProviderServiceType()
    provider_service_type.price = 150.00
    provider_service_type.is_top = True
    provider_service_type.provider_id = 30
    provider_service_type.service_type_id = 33
    provider_service_type.save()

class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0046_auto_20150819_1105'),
    ]

    operations = [
        migrations.RunPython( add_consulting_data ),
    ]


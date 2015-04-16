# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_initial_provider_status( apps, schema_editor ):

    # Get model to use (historical version)
    ProviderStatus = apps.get_model( "marketplace", "ProviderStatus" )

    # Insert Order Status
    provider_status = ProviderStatus()
    provider_status.id = 1
    provider_status.name = 'Pending Approval'
    provider_status.save()

    provider_status = ProviderStatus()
    provider_status.id = 2
    provider_status.name = 'Active'
    provider_status.save()

    provider_status = ProviderStatus()
    provider_status.id = 3
    provider_status.name = 'Suspended'
    provider_status.save()

    provider_status = ProviderStatus()
    provider_status.id = 4
    provider_status.name = 'Inactive'
    provider_status.save()


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0014_auto_20150414_1837'),
    ]

    operations = [
        migrations.RunPython( add_initial_provider_status ),
    ]

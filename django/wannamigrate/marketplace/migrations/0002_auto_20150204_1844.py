# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_initial_values( apps, schema_editor ):

    # Get model to use (historical version)
    OrderStatus = apps.get_model( "marketplace", "OrderStatus" )
    ServiceStatus = apps.get_model( "marketplace", "ServiceStatus" )
    ServiceType = apps.get_model( "marketplace", "ServiceType" )

    # Insert Order Status
    order_status = OrderStatus()
    order_status.id = 1
    order_status.name = 'Awaiting Payment'
    order_status.save()

    order_status = OrderStatus()
    order_status.id = 2
    order_status.name = 'Payment Approved'
    order_status.save()

    order_status = OrderStatus()
    order_status.id = 3
    order_status.name = 'Payment Denied'
    order_status.save()

    order_status = OrderStatus()
    order_status.id = 4
    order_status.name = 'Cancelled'
    order_status.save()

    order_status = OrderStatus()
    order_status.id = 5
    order_status.name = 'Refunded'
    order_status.save()
    
    
    # Insert Service Status
    service_status = ServiceStatus()
    service_status.id = 1
    service_status.name = 'Awaiting Payment'
    service_status.save()

    service_status = ServiceStatus()
    service_status.id = 2
    service_status.name = 'Started'
    service_status.save()

    service_status = ServiceStatus()
    service_status.id = 3
    service_status.name = 'Completed'
    service_status.save()

    service_status = ServiceStatus()
    service_status.id = 4
    service_status.name = 'Cancelled'
    service_status.save()


    # Insert Service Type
    service_type = ServiceType()
    service_type.id = 1
    service_type.name = 'Skype Consulting 30 Minutes'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 2
    service_type.name = 'Skype Consulting 60 Minutes'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 3
    service_type.name = 'Skype Consulting 90 Minutes'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 4
    service_type.name = 'Initial Assessment'
    service_type.save()

    service_type = ServiceType()
    service_type.id = 5
    service_type.name = 'File Review'
    service_type.save()



class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.RunPython( add_initial_values ),
    ]

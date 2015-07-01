# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def update_order_payment_types( apps, schema_editor ):

    # Get model to use (historical version)
    Order = apps.get_model( "marketplace", "Order" )

    # Insert Order Status
    orders = Order.objects.filter( external_code__in = [ '7C0B7BC23F884213B37A9AD8121FD773', '587516A450054A40B70DFFED52C44431', 'A4152016F5444870839D6CE93826500C' ] )
    for order in orders:
        order.payment_type_id = 2
        order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0028_order_payment_type'),
    ]

    operations = [
        migrations.RunPython( update_order_payment_types ),
    ]

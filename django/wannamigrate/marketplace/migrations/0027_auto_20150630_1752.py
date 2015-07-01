# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_initial_payment_types( apps, schema_editor ):

    # Get model to use (historical version)
    PaymentType = apps.get_model( "marketplace", "PaymentType" )

    # Insert Order Status
    payment_type = PaymentType()
    payment_type.id = 1
    payment_type.name = 'Credit-Card'
    payment_type.save()

    payment_type = PaymentType()
    payment_type.id = 2
    payment_type.name = 'Boleto'
    payment_type.save()

class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0026_paymenttype'),
    ]

    operations = [
        migrations.RunPython( add_initial_payment_types ),
    ]

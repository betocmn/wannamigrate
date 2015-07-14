# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_promo_code( apps, schema_editor ):

    # Get model to use (historical version)
    PromoCode = apps.get_model( "marketplace", "PromoCode" )

    # Insert Order Status
    promo_code = PromoCode()
    promo_code.id = 1
    promo_code.name = 'PROMO-50-XLEW'
    promo_code.discount = 50
    promo_code.expiry_date = '2015-07-17'
    promo_code.save()




class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0036_auto_20150713_1811'),
    ]

    operations = [
        migrations.RunPython( add_promo_code ),
    ]

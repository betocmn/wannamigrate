# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

#######################
# ACTIONS
#######################
def add_initial_products( apps, schema_editor ):

    # Get model to use (historical version)
    Product = apps.get_model( "marketplace", "Product" )

    # Insert Order Status
    product = Product()
    product.id = 1
    product.name = 'Guide - How to Move to Canada'
    product.description = 'A complete step-by-step guide about immigrating to Canada.'
    product.is_active = True
    product.icon_css_class = 'document'
    product.product_category_id = 1
    product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0022_auto_20150624_2022'),
    ]

    operations = [
        migrations.RunPython( add_initial_products ),
    ]

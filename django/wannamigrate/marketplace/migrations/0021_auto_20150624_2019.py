# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

#######################
# ACTIONS
#######################
def add_initial_product_categories( apps, schema_editor ):

    # Get model to use (historical version)
    ProductCategory = apps.get_model( "marketplace", "ProductCategory" )

    # Insert Order Status
    product_category = ProductCategory()
    product_category.id = 1
    product_category.name = 'E-Books'
    product_category.save()


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0020_auto_20150624_2018'),
    ]

    operations = [
        migrations.RunPython( add_initial_product_categories ),
    ]

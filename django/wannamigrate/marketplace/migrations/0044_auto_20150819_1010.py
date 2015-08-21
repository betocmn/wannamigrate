# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

#######################
# ACTIONS
#######################
def add_product_categories_and_items( apps, schema_editor ):

    # Get model to use (historical version)
    ProductCategory = apps.get_model( "marketplace", "ProductCategory" )
    Product = apps.get_model( "marketplace", "Product" )

    # Insert categories
    product_category = ProductCategory()
    product_category.id = 2
    product_category.name = 'Simple Subscription'
    product_category.save()

    product_category = ProductCategory()
    product_category.id = 3
    product_category.name = 'Support Subscription'
    product_category.save()

    # Insert new products
    product = Product()
    product.id = 2
    product.name = 'Subscription 1 Year - Australia'
    product.description = '1 year of full-access to the Immi Box - Immigration tools - for Australia'
    product.is_active = True
    product.icon_css_class = 'document'
    product.product_category_id = 2
    product.price = 80.00
    product.country_id = 117
    product.expiry_months = 12
    product.save()

    product = Product()
    product.id = 3
    product.name = 'Subscription 1 Year - Canada'
    product.description = '1 year of full-access to the Immi Box - Immigration tools - for Canada'
    product.is_active = True
    product.icon_css_class = 'document'
    product.product_category_id = 2
    product.price = 80.00
    product.country_id = 204
    product.expiry_months = 12
    product.save()

    product = Product()
    product.id = 4
    product.name = 'Subscription 1 Year - Australia (With Support)'
    product.description = '1 year of full-access to the Immi Box - Immigration tools - for Australia, including email support'
    product.is_active = True
    product.icon_css_class = 'document'
    product.product_category_id = 3
    product.price = 150.00
    product.country_id = 117
    product.expiry_months = 12
    product.save()

    product = Product()
    product.id = 5
    product.name = 'Subscription 1 Year - Canada (With Support)'
    product.description = '1 year of full-access to the Immi Box - Immigration tools - for Canada, including email support'
    product.is_active = True
    product.icon_css_class = 'document'
    product.product_category_id = 3
    product.price = 150.00
    product.country_id = 204
    product.expiry_months = 12
    product.save()



class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0043_auto_20150819_1009'),
    ]

    operations = [
        migrations.RunPython( add_product_categories_and_items ),
    ]

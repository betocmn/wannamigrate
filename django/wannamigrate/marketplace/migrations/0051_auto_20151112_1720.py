# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.db import connection


#######################
# ACTIONS
#######################
def update_products( apps, schema_editor ):

    # Get model to use (historical version)
    Product = apps.get_model( "marketplace", "Product" )
    ProductCategory = apps.get_model( "marketplace", "ProductCategory" )

    # Updates all old subscriptions to the 12 months one
    cursor = connection.cursor()
    cursor.execute( 'UPDATE marketplace_subscription SET product_id = 2 WHERE product_id IN(2,3,4,5)' )
    cursor.execute( 'UPDATE marketplace_order SET product_id = 2 WHERE product_id IN(2,3,4,5)' )

    # Updates products
    product = Product.objects.get(pk=2)
    product.name = 'Subscription 1 Year (disabled)'
    product.description = '1 year subscription + unlimited email support + skype interview'
    product.is_active = False
    product.icon_css_class = 'document'
    product.product_category_id = 2
    product.price = 260.00
    product.country_id = None
    product.expiry_months = 12
    product.save()

    product = Product.objects.get(pk=3)
    product.name = 'PRO Package'
    product.description = 'Skype interview + Resumé creation + English evaluation + 3 months email support'
    product.is_active = True
    product.icon_css_class = 'document'
    product.product_category_id = 2
    product.price = 175.00
    product.country_id = None
    product.expiry_months = 3
    product.save()

    # deletes unused data
    Product.objects.filter(pk=4).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0050_auto_20151103_1734'),
    ]

    operations = [
        migrations.RunPython( update_products ),
    ]

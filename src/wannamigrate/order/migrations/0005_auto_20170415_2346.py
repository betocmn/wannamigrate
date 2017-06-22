# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-15 13:46
from __future__ import unicode_literals

from django.db import migrations


def add_initial_products(apps, schema_editor):

    # Get model to use (historical version)
    Product = apps.get_model("order", "Product")

    # Insert Records
    product = Product()
    product.id = 1
    product.name = '1-Year Unlimited Access'
    product.price = 15.00
    product.save()


def add_initial_subscription_status(apps, schema_editor):

    # Get model to use (historical version)
    SubscriptionStatus = apps.get_model("order", "SubscriptionStatus")

    # Insert Records
    subscription_status = SubscriptionStatus()
    subscription_status.id = 1
    subscription_status.name = 'Never activated'
    subscription_status.save()

    subscription_status = SubscriptionStatus()
    subscription_status.id = 2
    subscription_status.name = 'Active'
    subscription_status.save()

    subscription_status = SubscriptionStatus()
    subscription_status.id = 3
    subscription_status.name = 'Expired'
    subscription_status.save()

    subscription_status = SubscriptionStatus()
    subscription_status.id = 4
    subscription_status.name = 'Cancelled'
    subscription_status.save()


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20170415_2341'),
    ]

    operations = [
        migrations.RunPython(add_initial_products),
        migrations.RunPython(add_initial_subscription_status),
    ]
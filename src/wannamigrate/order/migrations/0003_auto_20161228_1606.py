# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 05:06
from __future__ import unicode_literals

from django.db import migrations


def order_initial_values(apps, schema_editor):

    # Get model to use (historical version)
    OrderStatus = apps.get_model("order", "OrderStatus")
    PaymentType = apps.get_model("order", "PaymentType")

    # Order Status
    order_status = OrderStatus()
    order_status.name = 'awaiting payment'
    order_status.save()

    order_status = OrderStatus()
    order_status.name = 'authorised & waiting charge'
    order_status.save()

    order_status = OrderStatus()
    order_status.name = 'charged & succeeded'
    order_status.save()

    order_status = OrderStatus()
    order_status.name = 'billing failed'
    order_status.save()

    order_status = OrderStatus()
    order_status.name = 'refunded'
    order_status.save()

    # Payment Types
    payment_type = PaymentType()
    payment_type.name = 'Stripe Cards'
    payment_type.save()

    payment_type = PaymentType()
    payment_type.name = 'Paypal Cards'
    payment_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_member'),
    ]

    operations = [
        migrations.RunPython(order_initial_values),
    ]
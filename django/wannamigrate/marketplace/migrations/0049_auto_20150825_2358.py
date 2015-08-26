# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

#######################
# ACTIONS
#######################
def add_pre_sales_subscriptions( apps, schema_editor ):

    # Get model to use (historical version)
    Subscription = apps.get_model( "marketplace", "Subscription" )

    users = [6928,341,317,10103,11390,5715,10106,6721,8916,5031,9478,850,758,10444,8154,5375,4414,7941,12044,10389,12278,10425,7190]
    for user in users:

        # Insert subscription
        subscription = Subscription()
        subscription.user_id = user
        subscription.start_date = '2015-08-26'
        subscription.expiry_date = '2016-08-30'
        subscription.subscription_status_id = 2
        subscription.product_id = 4
        subscription.save()

        subscription = Subscription()
        subscription.user_id = user
        subscription.start_date = '2015-08-26'
        subscription.expiry_date = '2016-08-30'
        subscription.subscription_status_id = 2
        subscription.product_id = 5
        subscription.save()


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0048_auto_20150824_1631'),
    ]

    operations = [
        migrations.RunPython( add_pre_sales_subscriptions ),
    ]

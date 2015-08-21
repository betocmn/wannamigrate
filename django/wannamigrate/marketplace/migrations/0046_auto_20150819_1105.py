# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def add_subscription_status( apps, schema_editor ):

    # Get model to use (historical version)
    SubscriptionStatus = apps.get_model( "marketplace", "SubscriptionStatus" )

    # Insert categories
    subscription_status = SubscriptionStatus()
    subscription_status.id = 1
    subscription_status.name = 'Awaiting Payment'
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
        ('marketplace', '0045_auto_20150819_1105'),
    ]

    operations = [
        migrations.RunPython( add_subscription_status ),
    ]

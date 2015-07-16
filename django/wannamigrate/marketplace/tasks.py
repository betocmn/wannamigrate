"""
Tasks for marketplace app, including celery tasks

"""

##########################
# Imports
##########################
from __future__ import absolute_import
from celery import shared_task
from wannamigrate.core.mailer import Mailer




##########################
# Celery Tasks
##########################
@shared_task
def send_order_confirmation_user( user, order, provider ):
    return Mailer.send_order_confirmation_user( user, order, provider )
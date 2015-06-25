#################
# Imports
#################
from __future__ import absolute_import
from celery import shared_task
from wannamigrate.core.models import Notification





@shared_task
def add_notification( message, url, users ):
    return Notification.add( message, url, users )


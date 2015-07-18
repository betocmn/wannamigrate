#################
# Imports
#################
from __future__ import absolute_import
from celery import shared_task
from wannamigrate.core.models import Notification
from wannamigrate.core.mailer import Mailer
from django.utils import translation





##########################
# Celery Tasks
##########################
@shared_task
def add_notification( message_translation, message_no_translation, url, users ):
    return Notification.add( message_translation, message_no_translation, url, users )


@shared_task
def send_welcome_email( user ):
    return Mailer.send_welcome_email( user )
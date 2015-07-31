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
def add_notification( compressed_message, url, users, send_email = False ):
    return Notification.add( compressed_message, url, users, send_email )


@shared_task
def send_welcome_email( user, type = 'user' ):

    # sets user language
    preferred_language = user.preferred_language
    if not preferred_language:
        preferred_language = 'en'
    translation.activate( preferred_language )

    # sends email
    return Mailer.send_welcome_email( user, type )
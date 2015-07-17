"""
Tasks for marketplace app, including celery tasks

"""

##########################
# Imports
##########################
from __future__ import absolute_import
from celery import shared_task
from wannamigrate.core.mailer import Mailer
from django.utils import translation





##########################
# Celery Tasks
##########################
@shared_task
def send_order_confirmation_user( user, order, provider ):

    # sets user language
    preferred_language = user.preferred_language
    if not preferred_language:
        preferred_language = 'en'
    translation.activate( preferred_language )

    # sends email
    return Mailer.send_order_confirmation_user( user, order, provider )


@shared_task
def send_order_confirmation_provider( user, order, provider ):

    # sets user language
    preferred_language = user.preferred_language
    if not preferred_language:
        preferred_language = 'en'
    translation.activate( preferred_language )

    # sends email
    return Mailer.send_order_confirmation_provider( user, order, provider )


@shared_task
def send_order_download_link( user, order ):

    # sets user language
    preferred_language = user.preferred_language
    if not preferred_language:
        preferred_language = 'en'
    translation.activate( preferred_language )

    # sends email
    return Mailer.send_order_download_link( user, order )
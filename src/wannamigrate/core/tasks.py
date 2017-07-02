"""
General tasks with the option to run in the background with Celery
"""

##########################
# Imports
##########################
import json
from django.conf import settings
from celery import shared_task
from wannamigrate.core.tracking_processor import TrackingProcessor
from wannamigrate.core.alert_processor import AlertProcessor


##########################
# Function Definitions
##########################
@shared_task
def create_alert(title, message, mode='tech', **kwargs):
    """
    Create a tech or admin alert. This will send notifications to the
    related staff members (it could be via email, slack, sms, etc)

    :param title: str
    :param message: str
    :param mode: 'tech' or 'admin'
    :return: Boolean
    """
    return AlertProcessor.create(title, message, mode, **kwargs)


@shared_task
def track_event(member, event, data={}, **kwargs):
    """
    Record the actions our users perform

    :param member: User Object
    :param event: string
    :param data: dict
    :return: None
    """
    return TrackingProcessor.add(member, event, data)


@shared_task
def track_user(member):
    """
    Identifies the current user.

    :param member: Member Object
    :return: None
    """
    return TrackingProcessor.identify(member)

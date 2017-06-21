"""
Class responsible to process shipping operations.

It uses a 3rd party service through an API.

API Used: https://www.shippit.com/api (username: shippit, password: shippit_api_docs)
"""

##########################
# Imports
##########################
import requests
import json
from django.conf import settings


##########################
# Class definitions
##########################
class AlertProcessor(object):
    """
    Class responsible to create system alerts and notify admins/devs
    """

    @staticmethod
    def create(title, message, mode='tech', **kwargs):
        """
        Sends the HTTP request with the data to Slack

        :param title: str
        :param message: str
        :param mode: 'tech' or 'admin'
        :return: Boolean
        """

        text = ">%s \n ```%s```" % (title, message)
        url = settings.ALERT_TECH_SLACK_URL if mode == 'tech' else settings.ALERT_ADMIN_SLACK_URL
        return requests.post(url, data=json.dumps({'text': text}))

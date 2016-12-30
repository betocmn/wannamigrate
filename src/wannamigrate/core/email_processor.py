"""
Class responsible to process all transactional emails

It uses a 3rd party service through an API.

API Used: https://sendgrid.com
"""

##########################
# Imports
##########################
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Substitution, Mail
import urllib.request as urllib
from django.conf import settings


##########################
# Class definitions
##########################
class EmailProcessor(object):
    """
    Class responsible to prepare the data and communicate with the 3rd party API
    """

    @staticmethod
    def send(email, tracking_event, data={}):
        """
        Record the actions our users perform

        :param email: String
        :param tracking_event: String
        :param data: dictionary
        :return: None
        """

        # If in DEV, only works for staff emails
        if not settings.IS_PROD and '@wannamigrate.com' not in email:
            return False

        # Checks if there's a transactional email for this tracking event
        email_template_id = EmailProcessor.get_template(tracking_event, data)
        if not email_template_id:
            return False

        # Sets up email base via Sendgrid's Python library
        sg = sendgrid.SendGridAPIClient(apikey=settings.SEND_GRID_KEY)
        from_email = Email(settings.EMAIL_DEFAULT_FROM_ADDRESS, settings.EMAIL_DEFAULT_FROM_NAME)
        to_email = Email(email)
        content = Content("text/html", "Replace This")
        subject = "Replace This"
        mail = Mail(from_email, subject, to_email, content)

        # Perform template substitutions
        for key, value in data.items():
            if key and value:
                mail.personalizations[0].add_substitution(Substitution(
                    "-%s-" % key, "%s" % value
                ))

        # Sets the template
        mail.set_template_id(email_template_id)

        # Sends email
        error_msg = None
        try:
            response = sg.client.mail.send.post(request_body=mail.get())
            if response.status_code != 202:
                error_msg = "Request Failed!" \
                            "\nStatus: %s \nResponse Body: %s\n Response Headers: %s" % (
                                response.status_code, response.body, response.headers
                            )
        except urllib.HTTPError as e:
            error_msg = e.read()

        # If there's an error, alert devs right away
        if error_msg:
            pass
            """
            AlertProcessor.create(
                "Emails Processor Failed",
                "%s" % error_msg
            )
            """

    @staticmethod
    def get_template(tracking_event, data={}):
        """
        Mapping between tracking events and send grid transactional templates.

        If none is find, no need to send out transactional emails for this event.

        :param tracking_event: String
        :param data: dictionary
        :return: None
        """

        # First we try to identify a direct link between the tracking event and email to be sent
        template_id = None
        mapping = {
            settings.TRACKING_EVENT_SENT_SUPPORT_MESSAGE:
                settings.EMAIL_TEMPLATE_CONTACT_FORM,
        }
        if tracking_event in mapping:
            template_id = mapping[tracking_event]

        return template_id

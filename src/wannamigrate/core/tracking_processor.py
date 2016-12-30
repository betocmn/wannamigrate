"""
Class responsible to process all tracking

It uses a 3rd party service through an API.

API Used: https://segment.com/docs/
"""

##########################
# Imports
##########################
import analytics
from django.conf import settings
from django.core.urlresolvers import reverse
from wannamigrate.core.util import date_to_string
from wannamigrate.core.email_processor import EmailProcessor


##########################
# Class definitions
##########################
class TrackingProcessor(object):
    """
    Class responsible to prepare the data and communicate with the 3rd party API
    """

    @staticmethod
    def add(member, event, data={}, order=None, password_reset_url=None):
        """
        Record the actions our users perform

        :param member: Object
        :param event: string
        :param data: dict
        :param order: Object
        :param password_reset_url: String
        :param to_contact: String
        :return: None
        """

        # Initial settings
        user = member.user

        # If in DEV, only works for staff emails
        if not settings.IS_PROD and '@wannamigrate.com' not in user.email:
            return False

        # Sets up Segment Python Library
        analytics.write_key = settings.SEGMENT_KEY
        if not settings.IS_PROD:
            analytics.debug = True

        # Reinforces user identity
        data['email'] = user.email
        data['member_id'] = member.id
        data['member_first_name'] = user.first_name
        data['member_last_name'] = user.last_name
        data['member_birth_date'] = "%s" % member.birth_date
        data['member_gender'] = member.gender
        data['member_mobile_number'] = member.mobile_number
        data['member_referral_code'] = member.referral_code
        data['member_registration_date'] = date_to_string(user.created_date)
        data['member_login_url'] = "%s%s" % (settings.BASE_URL_SECURE, reverse('member:login'))

        # If sending a reset password link
        if password_reset_url:
            data['password_reset_url'] = password_reset_url

        # Sends Segment Tracking Event
        analytics.track(user.id, event, data, integrations={
            'All': True,
            'Facebook Pixel': False
        })

        # Sends out transactional emails (if any)
        EmailProcessor.send(user.email, event, data)

    @staticmethod
    def identify(member):
        """
        Identifies the current user.

        :param member: Member Object
        :return: None
        """

        # Initial settings
        user = member.user

        # If in DEV, only works for staff emails
        if not settings.IS_PROD and '@wannamigrate.com' not in user.email:
            return False

        # Sets up Segment Python Library
        analytics.write_key = settings.SEGMENT_KEY
        if not settings.IS_PROD:
            analytics.debug = True

        # Sends Identity Data
        first_name = user.first_name if user.first_name else ''
        last_name = user.first_name if user.last_name else ''
        full_name = '%s %s' % (user.first_name, user.last_name) if user.first_name else ''
        analytics.identify(user.id, {
            'email': user.email,

            # Segment required
            'id': user.id,
            'firstName': first_name,
            'lastName': last_name,
            'name': full_name,
            'created': date_to_string(user.created_date),

            # Our params
            'member_id': member.id,
            'member_first_name': first_name,
            'member_last_name': last_name,
            'member_birth_date': "%s" % member.birth_date,
            'member_gender': member.gender,
            'member_mobile_number': member.mobile_number,
            'member_referral_code': member.referral_code,
            'member_registration_date': date_to_string(user.created_date)
        })

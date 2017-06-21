"""
With signal you can pretty much setup state actions before
or after some action occurs.

Django includes a “signal dispatcher” which helps allow
decoupled applications get notified when actions occur elsewhere in the framework

Read more on: https://docs.djangoproject.com/en/1.9/topics/signals/
"""

##########################
# Imports
##########################
import random
from django.db.models.signals import post_save
from wannamigrate.member.models import Member


def member_post_save(sender, instance, created, raw, using, update_fields, **kwargs):
    """
    Post-Save for Member.
    Generates referral code on the format:

    {RANDOM_KEYWORD}{MEMBER_ID}

    And welcome code on the format:
    {EMAIL_USERNAME}{RANDOM 2 DIGITS}

    :param sender:
    :param instance:
    :param created:
    :param raw:
    :param using:
    :param update_fields:
    :param kwargs:
    :return:
    """
    if not instance.referral_code:

        # Get a random word from the list below
        possible_words = [
            'TRIP', 'COUNTRY', 'IMMI', 'MIGRATION', 'WANNA', 'PASSPORT', 'MOVE', 'PLANE',
            'TRAIN', 'LIFE', 'NEW', 'EXPAT', 'FUTURE', 'VISA'
        ]
        secure_random = random.SystemRandom()
        keyword = secure_random.choice(possible_words)

        # Generates referral code
        referral_code = "%s%s" % (
            keyword, instance.id
        )
        instance.referral_code = referral_code.upper()
        instance.save()


##########################
# Signals setup
##########################
post_save.connect(member_post_save, sender=Member)

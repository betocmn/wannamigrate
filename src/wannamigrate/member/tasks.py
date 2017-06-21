"""
General tasks with the option to run in the background with Celery
"""

##########################
# Imports
##########################
from django.conf import settings
from celery import shared_task
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.urlresolvers import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from wannamigrate.member.models import PaymentMethod
from wannamigrate.core.tracking_processor import TrackingProcessor


##########################
# Function Definitions
##########################
@shared_task
def save_payment_method_info(member, is_default=False, stripe_customer=None, stripe_source=None):
    """
    Saves payment method to a member, such as a stripe card

    :param member: object
    :param is_default: integer
    :param stripe_customer: object
    :param stripe_source: string
    :return:
    """

    card = None
    if stripe_source:
        card = stripe_source

    elif stripe_customer:
        card = stripe_customer.sources.data[0]

    if card:

        if is_default:
            PaymentMethod.objects.filter(member=member).update(is_default=False)
        payment_method = PaymentMethod()
        payment_method.payment_type_id = settings.DB_ID_PAYMENT_TYPE_STRIPE_CARDS
        payment_method.payment_api_method_uuid = card.id
        payment_method.member = member
        payment_method.card_brand = card.brand
        payment_method.card_last4 = card.last4
        payment_method.card_expiry_month = card.exp_month
        payment_method.card_expiry_year = card.exp_year
        payment_method.is_default = is_default
        payment_method.save()
        return True

    return False


@shared_task
def track_payment_failure(member, order):
    """
    Send email notifications to members when a payment charge failed

    :param member: Member object
    :param order: Order object
    """
    TrackingProcessor.add(member, settings.TRACKING_EVENT_PAYMENT_FAILED, order=order)


@shared_task
def track_password_reset_request(member):
    """
    Send email notification to reset password

    :param member: Member Object
    """
    user = member.user

    # creates token
    token_generator = PasswordResetTokenGenerator()
    token = token_generator.make_token(user)

    # builds link
    base_secure_url = settings.BASE_URL_SECURE
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    link = base_secure_url + reverse('member:reset_password', args=(uid, token,))

    # Sends out notification via autopilot
    TrackingProcessor.add(
        member, settings.TRACKING_EVENT_REQUESTED_PASSWORD_RESET, {}, password_reset_url=link
    )

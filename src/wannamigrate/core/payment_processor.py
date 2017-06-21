"""
Class responsible to process payments.

It uses a 3rd party service through an API.

API Used: https://self.stripe.com/docs
"""

##########################
# Imports
##########################
import stripe
from django.conf import settings
from wannamigrate.core.util import convert_to_cents, format_monetary
from wannamigrate.core.tasks import create_alert
from wannamigrate.member.tasks import save_payment_method_info
from wannamigrate.member.models import PaymentMethod


##########################
# Class definitions
##########################
class PaymentProcessor(object):
    """
    Class responsible to make payments and related transactions
    using a 3rd party API (https://self.stripe.com/docs/)

    """

    def __init__(self):
        """
        Constructor responsible to set initial class attributes

        :return: None
        """

        # Sets api key for test or live mode
        self.stripe = stripe
        self.stripe.api_key = settings.STRIPE_SECRET_KEY
        self.stripe.api_version = '2016-07-06'

    @staticmethod
    def prepare_monetary_value(number, mode='send'):
        """
        Returns cents from a whole value.

        Example: 10.00 = 1000 |  144.20 = 14420

        :param: number
        :param: mode 'send' or 'receive'
        :return: Int
        """
        if mode == 'send':
            return convert_to_cents(number)
        else:
            return format_monetary(number/100)

    def create_card(self, member, token):
        """
        Adds a new card to the given member and make it as the default one

        :param member: Object
        :param token: String
        :return: Dictionary
        """

        try:
            # Tries to retrieve the Stripe Customer
            stripe_customer = None
            if member.payment_api_customer_uuid:
                stripe_customer = self.stripe.Customer.retrieve(member.payment_api_customer_uuid)

            # Create new customer or attach new card to an existing one
            if not stripe_customer:
                stripe_customer = self.create_customer(member, token)
                source = stripe_customer.sources.data[0]
            else:
                source = stripe_customer.sources.create(source=token)

            # Sets it as the new default one
            self.set_source_as_default(stripe_customer=stripe_customer, source_id=source.id)

            # Returns successfully created card
            return {
                'status': 'success',
                'source': source
            }

        except self.stripe.error.CardError as e:
            # Error on Stripe API Request
            body = e.json_body
            err = body['error']
            return {
                'status': 'error',
                'message': 'Stripe Request Failed',
                'api_response': {
                    'http_status': e.http_status,
                    'error_type': err['type'],
                    'error_code': err['code'],
                    'error_message': err['message'],
                }
            }
        except Exception as e:

            # Something else happened, completely unrelated to Stripe
            return {
                'status': 'error',
                'message': 'Unexpected Error',
                'api_response': {'exception': '%s' % e}
            }
            create_alert(
                "Payment Processor Charge",
                "Unexpected Error! Please check payments are working - %s" % e
            )
        return response

    def set_source_as_default(self, member=None, stripe_customer=None, source_id=None):
        """
        Creates a new customer on Stripe

        :param member: Object
        :param stripe_customer: Object
        :param source_id: String
        :return: Dictionary
        """

        # Identifies stripe customer
        if member and not stripe_customer:
            stripe_customer = self.stripe.Customer.retrieve(member.payment_api_customer_uuid)

        # Updates customer to use the given source as default
        if stripe_customer:
            stripe_customer.default_source = source_id
            stripe_customer.save()
            return True

        return False

    def delete_source(self, member=None, stripe_customer=None, source_id=None):
        """
        Creates a new customer on Stripe

        :param member: Object
        :param stripe_customer: Object
        :param source_id: String
        :return: Dictionary
        """

        # Identifies stripe customer
        customer = None
        if not stripe_customer:
            customer = self.stripe.Customer.retrieve(member.payment_api_customer_uuid)

        # Updates customer to use the given source as default
        if customer:
            result = customer.sources.retrieve(source_id).delete()
            if result.deleted:
                return True

        return False

    def create_customer(self, member, token):
        """
        Creates a new customer on Stripe

        :param member: Object
        :param token: String
        :return: Dictionary
        """

        # Sets up required data from the member account
        user = member.user

        # Creates customer on Stripe
        stripe_customer = self.stripe.Customer.create(
            source=token, description=user.get_full_name(), email=user.email,
            metadata={'member_id': member.id},
        )

        # Updates member to store stripe's customer ID for future transactions
        member.payment_api_customer_uuid = stripe_customer.stripe_id
        member.save()

        return stripe_customer

    def charge(self, member, total, token=None, try_alternative_methods=True):
        """
        Makes a credit-card or boleto payment

        'status' on response can be 'success', 'pending', 'declined', 'error'

        :param member: Object
        :param total: Float
        :param token: String
        :param try_alternative_methods: Boolean - Retry payment with other saved payment methods
        :return: Dictionary
        """

        try:

            # Creates a Customer on Stripe API
            if token and token not in ['saved', 'ignored']:
                stripe_customer = self.create_customer(member, token)
                stripe_customer_id = stripe_customer.stripe_id

                # Celery task to save credit card identifier to this member
                save_payment_method_info.delay(
                    member, stripe_customer=stripe_customer, is_default=True
                )
            else:
                stripe_customer_id = member.payment_api_customer_uuid

            # If total is zero, no need to charge
            if total == 0:
                return {
                    'status': 'success',
                    'order_status_id': settings.DB_ID_ORDER_STATUS_CHARGED_SUCCEEDED,
                    'api_response': {
                        'transaction_uuid': '',
                        'fee': 000,
                        'raw': ''
                    }
                }

            # Charges the Customer on Stripe
            stripe_charge = self.stripe.Charge.create(
                amount=self.prepare_monetary_value(total, 'send'),
                currency="aud",
                customer=stripe_customer_id,
                description="Wannamigrate Australia",
                expand=['balance_transaction']
            )

            # If it fails and we want to retry with other saved payment methods (if any)
            if try_alternative_methods and not stripe_charge.paid:
                payment_methods = PaymentMethod.objects.filter(member=member, is_default=False)
                for payment_method in payment_methods:
                    stripe_charge = self.stripe.Charge.create(
                        amount=self.prepare_monetary_value(total, 'send'),
                        currency="aud",
                        customer=stripe_customer_id,
                        description="Wannamigrate Australia",
                        expand=['balance_transaction'],
                        source=payment_method.payment_api_method_uuid
                    )
                    if stripe_charge.paid:
                        break

            # Formats response
            if stripe_charge.paid:
                status = 'success'
                order_status_id = settings.DB_ID_ORDER_STATUS_CHARGED_SUCCEEDED
            else:
                status = 'declined'
                order_status_id = settings.DB_ID_ORDER_STATUS_CHARGED_FAILED
            response = {
                'status': status,
                'order_status_id': order_status_id,
                'api_response': {
                    'transaction_uuid': stripe_charge.id,
                    'fee': str(self.prepare_monetary_value(
                        stripe_charge.balance_transaction.fee, 'receive'
                    )),
                    'raw': stripe_charge
                }
            }

        except self.stripe.error.CardError as e:
            # Error on Stripe API Request
            body = e.json_body
            err = body['error']
            response = {
                'status': 'error',
                'message': 'Stripe Request Failed',
                'order_status_id': settings.DB_ID_ORDER_STATUS_CHARGED_FAILED,
                'api_response': {
                    'http_status': e.http_status,
                    'error_type': err['type'],
                    'error_code': err['code'],
                    'error_message': err['message'],
                }
            }

        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            response = {
                'status': 'error',
                'message': 'Unexpected Error',
                'order_status_id': settings.DB_ID_ORDER_STATUS_CHARGED_FAILED,
                'api_response': {'exception': '%s' % e}
            }
            create_alert(
                "Payment Processor Charge",
                "Unexpected Error! Please check payments are working - %s" % e
            )

        return response

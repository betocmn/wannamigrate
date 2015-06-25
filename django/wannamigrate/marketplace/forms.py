"""
Site FORMS

Form definitions used by views/templates from the site app
"""

##########################
# Imports
##########################
from django import forms
from django.forms import TextInput, PasswordInput
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.forms import BaseForm, BaseModelForm, CountryChoiceField, GoalChoiceField, CountryImmigrationChoiceField
from wannamigrate.marketplace.models import (
    Order, OrderHistory, Service, ServiceHistory, ServiceStatus, OrderStatus, ServiceType
)
from django.forms import ModelChoiceField
from wannamigrate.marketplace.payment_processor import PaymentProcessor





#######################
# CUSTOM FORM FIELD CLASSES
#######################
class ServiceTypeChoiceField( ModelChoiceField ):
    """
    Custom Model for service types, to get translation
    """

    choices = ServiceType.get_translated_tuple( is_active = True )





#######################
# PAYMENT FORMS
#######################
class PaymentForm( BaseForm ):
    """
    Form for PAYMENT PAGE
    """

    # Form elements
    token = forms.CharField( required = False, widget = forms.HiddenInput() )
    payment_type = forms.CharField( required = False, widget = forms.HiddenInput() )

    def __init__( self, *args, **kwargs ):
        """
        Initializes attributes

        :return: Model Object
        """

        self.payment_api_result = {}
        self.payment_info = {}
        self.service = None

        if 'payment_info' in kwargs:
            self.payment_info = kwargs.pop( "payment_info" )
        super( PaymentForm, self ).__init__( *args, **kwargs )


    def clean( self ):
        """
        Run credit card authorization in here

        :return: Dictionary
        """

        # Gets all form submitted data
        cleaned_data = super( PaymentForm, self ).clean()

        # Cheks if payment info was passed
        if not hasattr( self, 'payment_info' ) or not self.payment_info:
            raise forms.ValidationError( _( "Payment information missing." ) )

        # If no payment-method was selected
        if not cleaned_data['payment_type'] or cleaned_data['payment_type'] not in ['boleto', 'credit-card']:
            raise forms.ValidationError( _( "Invalid Payment Method." ) )

        # Build items list
        if self.payment_info['is_service']:
            items = [{ 'description': self.payment_info['service_type'].name,
                       'quantity': 1,
                       'price': self.payment_info['provider_service_type'].price
            }]
        else:
            items = [{ 'description': self.payment_info['product'].name,
                       'quantity': 1,
                       'price': self.payment_info['product'].price
            }]

        # makes payment
        payment_processor = PaymentProcessor()
        payment_api_result = payment_processor.charge(
            method = 'bank_slip' if cleaned_data['payment_type'] == 'boleto' else '',
            token = self.payment_info['token'],
            email = self.payment_info['user'].email,
            discount = 0,
            items = items
        )

        # Passes result to private attribute
        self.payment_api_result = payment_api_result

        # If it's a service, do some required actions
        if self.payment_info['is_service']:

            # updates service status
            self.payment_info['service'].service_status_id = ServiceStatus.get_status_from_order_status( payment_api_result['order_status_id'] )
            self.payment_info['service'].save()

            # inserts first service_history
            service_history = ServiceHistory()
            service_history.service_id = self.payment_info['service'].id
            service_history.service_status_id = self.payment_info['service'].service_status_id
            service_history.user_id = self.payment_info['service'].user_id
            service_history.save()

        # If payment was not authorized, raise ERROR
        if not payment_api_result['success']:
            raise forms.ValidationError( _( "Payment not authorized." ) )

        return cleaned_data


    def save( self ):
        """
        Saves user using the 'create_user' manager method

        :param: order_info
        :return: Dictionary
        """

        # Configure variables for service or product
        if self.payment_info['is_service']:
            price = self.payment_info['provider_service_type'].price
            description = self.payment_info['service_type'].name
        else:
            price = self.payment_info['product'].price
            description = self.payment_info['product'].name

        # inserts details on order table
        order = Order()
        order.gross_total = price
        order.net_total = price
        order.description = description
        order.discount = 0
        order.fees = 0
        order.installments = 1
        order.external_code = self.payment_api_result['external_code']
        order.order_status_id = self.payment_api_result['order_status_id']
        if self.payment_info['is_service']:
            order.service = self.payment_info['service']
        else:
            order.product = self.payment_info['product']
        order.user = self.payment_info['user']
        order.save()

        # inserts first order_history
        order_history = OrderHistory()
        order_history.order_id = order.id
        order_history.order_status_id = order.order_status_id
        order_history.transaction_code = self.payment_api_result['transaction_code']
        order_history.full_api_response = self.payment_api_result['full_api_response']
        order_history.save()

        return order






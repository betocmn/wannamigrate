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





#######################
# CUSTOM FORM FIELD CLASSES
#######################
class ServiceTypeChoiceField( ModelChoiceField ):
    """
    Custom Model for service types, to get translation
    """

    choices = ServiceType.get_translated_tuple()





#######################
# PAYMENT FORMS
#######################
class PaymentForm( BaseForm ):
    """
    Form for PAYMENT PAGE
    """

    postal_code = forms.CharField( required = True, max_length = 12, label = _( "Postal Code" ) )

    def save( self, commit = True, order_info = False  ):
        """
        Saves user using the 'create_user' manager method

        :param: order_info
        :return: Dictionary
        """

        # inserts service
        service = Service()
        service.service_price = order_info['provider_service_type'].price
        service.user = order_info['user']
        service.provider = order_info['provider']
        service.service_type = order_info['service_type']
        service.service_status_id = ServiceStatus.get_status_from_payment_result( order_info['payment_api_result']['result'] )
        service.save()

        # inserts first service_history
        service_history = ServiceHistory()
        service_history.service_id = service.id
        service_history.service_status_id = service.service_status_id
        service_history.user_id = service.user_id
        service_history.save()

        # inserts details on order table
        order = Order()
        order.gross_total = order_info['provider_service_type'].price
        order.net_total = order_info['provider_service_type'].price
        order.discount = 0
        order.fees = 0
        order.installments = 1
        order.external_code = order_info['payment_api_result']['external_code']
        order.order_status_id = OrderStatus.get_status_from_payment_result( order_info['payment_api_result']['result'] )
        order.service = service
        order.user = order_info['user']
        order.save()

        # inserts first order_history
        order_history = OrderHistory()
        order_history.order_id = order.id
        order_history.order_status_id = order.order_status_id
        order_history.transaction_code = order_info['payment_api_result']['transaction_code']
        order_history.payment_code = order_info['payment_api_result']['payment_code']
        order_history.save()

        return order


    def clean( self ):
        """
        Extra validation for fields that depends on other fields

        :return: Dictionary
        """
        cleaned_data = super( PaymentForm, self ).clean()

        #TODO credit card form validation
        """
        credit_card_number = cleaned_data.get( "credit_card_number" )
        credit_card_name = cleaned_data.get( "credit_card_name" )
        if not credit_card_number:
            raise forms.ValidationError( _( "Error message here." ) )
        """

        return cleaned_data






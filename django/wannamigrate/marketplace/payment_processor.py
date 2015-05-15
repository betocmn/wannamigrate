"""
Class responsible to process payments.

It will use a 3rd party service through an API.

API Used: https://iugu.com/referencias
"""

##########################
# Imports
##########################
from wannamigrate.core.models import (
    Country, User
)
from wannamigrate.marketplace.models import (
    Order, OrderHistory, OrderStatus, Service, ServiceHistory,
    ServiceStatus, ServiceType, ProviderServiceType
)
from wannamigrate.core.util import calculate_age, get_object_or_false, get_list_or_false, date_difference
from django.conf import settings
import json
import re
import base64
import requests
from decimal import Decimal





##########################
# Class definitions
##########################
class PaymentProcessor( object ):
    """
    Class responsible to make payments and related transactions
    using a 3rd party API (https://iugu.com/referencias)

    """

    def __init__( self ):
        """
        Constructor responsible to set initial class atributes

        :return: None
        """

        # Sets api key for test or live mode
        if settings.PAYMENT_API_MODE == 'LIVE':
            self.api_key = settings.PAYMENT_API_KEY_LIVE
        else:
            self.api_key = settings.PAYMENT_API_KEY_TEST


    def charge_credit_card( self, **kwargs ):
        """
        Makes a credit-card or boleto payment

        :return: Dictionary
        """
        # Creates URL with the correct action
        url = self.make_url( ['charge'] )

        # Builds the items array
        items = []
        posted_items = kwargs.get( 'items' )
        for item in posted_items:
            temp = {
                'description': item['description'],
                'quantity': item['quantity'],
                'price_cents': self.convert_to_cents( item['price'] )
            }
            items.append( temp )

        # formats request data
        data = {
            'token': kwargs.get( 'token' ),
            'email': kwargs.get( 'email' ),
            'discount_cents': kwargs.get( 'discount' ),
            'items': items
        }

        # makes API request call
        return self.send_request( url, 'POST', settings.ID_ORDER_STATUS_APPROVED, data )


    def send_request( self, url, method, status_on_success, data = {} ):
        """
        Base request for the Payment Processor API server.

        Through here we will send information to the server, such as
        "charge $10 from this credit card" and get a response back.

        :param: url
        :param: method
        :param: data
        :param: status_on_success
        :return: Boolean
        """

        """
        req = requests.Request(
            method,
            url,
            data = json.dumps( data ),
            headers = self.get_headers()
        )
        prepped = req.prepare()

        return str( prepped.body )
        """

        # Sends request
        try:
            response = requests.request(
                method,
                url,
                data = json.dumps( data ),
                headers = self.get_headers(),
                verify = False
            )
            return self.format_response( response.content.decode( 'utf-8' ), status_on_success )

        #TODO: Create especifics exceptions
        except Exception as error:
            raise


    def get_headers( self ):
        """
        Constructs basic headers for all requests

        :return: String
        """
        api_key = self.api_key + ':'
        api_key = base64.b64encode( api_key.encode('ascii') ).decode()
        api_key = str( api_key ).replace( "\n", "" )
        return {
            "Authorization": "Basic %s" % api_key,
            "User-Agent": "Wanna Migrate Python Api",
            "Accept-Charset": "utf-8",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }


    def make_url( self, arguments ):
        """
        Constructs full URL by adding parameters after the base URL

        Example: https://api.iugu.com/v1/subscriptions/ID_DA_ASSINATURA/suspend

        :param: arguments - List of parameters
        :return: String
        """
        url = settings.PAYMENT_API_BASE_URL
        for path in arguments:
            url = re.sub( r'/?$', re.sub(r'^/?', '/', str( path ) ), url )
        return url


    def convert_to_cents( self, number ):
        """
        Returns cents from a whole value.

        Example: 10.00 = 1000 |  144.20 = 14420

        :param: number
        :return: Int
        """
        result = Decimal( number * 100 ).quantize( Decimal( '1.' ) )
        return int( result )


    def format_response( self, text, status_on_success ):
        """
        Receives UTF-8 json-text response, proccess it, formates it and return as
        a python dictionary

        It returns a dictionary with:
            'success' - True of False
            'order_status_id' - Empty or ORDER_STATUS_ID
            'external_code' - API identifier for the money transaction (such as invoice id hash)
            'transaction_code' - API transaction code created in every API request (it's empty for IUGU)
            'errors' - String or dict of errors
            'full_api_response' - Full text API response

        :param: text (Json text)
        :param: status_on_success (order status id)
        :return: Dictionary
        """

        # Converts from JSON to dictionary
        api_result = json.loads( text )

        # initializes our response
        response = {}
        response['order_status_id'] = settings.ID_ORDER_STATUS_PENDING
        response['transaction_code'] = ''
        response['external_code'] = ''
        response['full_api_response'] = text

        # if it was successfull
        if 'success' in api_result and api_result['success']:
            response['success'] = True
            response['order_status_id'] = status_on_success
        else:
            response['success'] = False

        # If there are errors
        if 'errors' in api_result and api_result['errors']:
            response['errors'] = api_result['errors']

        # If there is an external code
        if 'invoice_id' in api_result and api_result['invoice_id']:
            response['external_code'] = api_result['invoice_id']

        return response

        """ Credit Card Declined

        {
            "message":"Transacao negada",
            "errors":{},
            "success":false,
            "url":"https://iugu.com/invoices/c62e0243-3112-4460-8966-adf66abbf49f-b14c",
            "pdf":"https://iugu.com/invoices/c62e0243-3112-4460-8966-adf66abbf49f-b14c.pdf",
            "identification":null,
            "invoice_id":"C62E0243311244608966ADF66ABBF49F",
            "LR":"05"
        }



        ###### Errors in items
        {
            "errors":
            {
                "items.description":["não pode ficar em branco"],
                "items.quantity":["não é um número"],
                "total":["deve ser maior que 0"]
            }
        }


        ###### Invalid TOken
        {
            "errors":"token nao é válido"
        }



        ####### Invalid Email
        {
            "errors":
            {
                "email":["nao pode ficar em branco","nao é válido"]
            }
        }


        ###### Success

        {
            "message":"Autorizado",
            "errors":{},
            "success":true,
            "url":"https://iugu.com/invoices/4d845918-3f3a-4ac9-a985-5fe9ac59ceb3-6734",
            "pdf":"https://iugu.com/invoices/4d845918-3f3a-4ac9-a985-5fe9ac59ceb3-6734.pdf",
            "identification":null,
            "invoice_id":"4D8459183F3A4AC9A9855FE9AC59CEB3",
            "LR":"00"
        }

        """
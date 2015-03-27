"""
Marketplace Views

These are the views that control logic flow for
the templates on the marketplace app
"""

##########################
# Imports
##########################
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.utils import translation
from wannamigrate.core.util import get_object_or_false
from wannamigrate.marketplace.forms import PaymentForm
from wannamigrate.marketplace.models import (
    Provider, Review, ServiceType, Provider_ServiceTypes, Order
)
from wannamigrate.core.mailer import Mailer
from wannamigrate.site.views import get_situation_form





#######################
# LISTS SERVICE PROVIDERS
#######################
@login_required
def professionals( request ):
    """
    Listing of professionals

    :param: request
    :return: String - The html page rendered
    """

    # Initial template
    template_data = {}

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # If situation is defined, we load professionals related to it
    if 'situation' in request.session and 'from_country' in request.session['situation']:

        from_country = request.session['situation']['from_country']
        to_country = request.session['situation']['to_country']
        goal = request.session['situation']['goal']

        # Gets 5 most related service providers
        template_data['providers'] = Provider.get_listing( to_country.id, 0, 5 )

    # Print Template
    return render( request, 'marketplace/professionals/list.html', template_data )





#######################
# PROFILE PAGE OF A SERVICE PROVIDERS
#######################
@login_required
def profile( request, user_id, name ):
    """
    View detais of a professional

    :param: request
    :return: String - The html page rendered
    """

    # Identify database record
    provider = Provider.get_profile( user_id )
    if not provider:
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Initializes template data dictionary
    template_data = {}

    # passes form to template
    template_data['situation_form'] = get_situation_form( request )

    # passes service provider to template
    template_data['provider'] = provider
    template_data['provider_service_types'] = Provider_ServiceTypes.get_listing( provider.id )
    template_data['reviews'] = Review.get_listing( provider.user_id )

    # Prints Template
    return render( request, 'marketplace/professionals/view.html', template_data )





#######################
# PAYMENT PAGE
#######################
@login_required
def payment( request, user_id, service_type_id ):
    """
    Payment page for hiring a professional

    :param: request
    :return: String - The html page rendered
    """

    # Identify database records
    provider = Provider.get_profile( user_id )
    service_type = get_object_or_false( ServiceType, pk = service_type_id )
    provider_service_type = get_object_or_false( Provider_ServiceTypes, provider_id = provider.id, service_type_id = service_type.id )
    if not provider or not service_type or not provider_service_type:
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Initializes template data dictionary
    template_data = {}

    # Instantiates the form
    form = PaymentForm( request.POST or None )

    # if form was submitted and is valid
    if form.is_valid():

        #TODO create payment API request here
        payment_api_result = {}
        credit_card_name = form.cleaned_data['credit_card_name']
        credit_card_number = form.cleaned_data['credit_card_number']
        payment_api_result['result'] = 2
        payment_api_result['external_code'] = "xeu37203sk32"
        payment_api_result['transaction_code'] = "32342342134124214321421421"
        payment_api_result['payment_code'] = "88891"

        # If payment was successful we save order info and confirm to the user
        if payment_api_result['result'] == 2:

            # saves order information
            order_info = {
                'payment_api_result': payment_api_result,
                'from_user': request.user,
                'to_user': provider.user,
                'service_type': service_type,
                'provider_service_type': provider_service_type
            }
            order = form.save( order_info = order_info )

            # Sends Order Confirmation email
            # TODO Change this to a celery/signal background task
            Mailer.send_order_confirmation( request.user.email, provider_service_type, order )

            # Redirect to confirmation page
            return HttpResponseRedirect( reverse( 'marketplace:confirmation', args = ( order.id, ) ) )

        else:

            # Return error message to template
            messages.error( request, _( 'Payment was declined.' ) )

    # passes forms to template
    template_data['form'] = form
    template_data['situation_form'] = get_situation_form( request )

    # passes objects to the template
    template_data['provider'] = provider
    template_data['service_type'] = service_type

    # Prints Template
    return render( request, 'marketplace/service/payment.html', template_data )

    """
    # Print SQL Queries
    from django.db import connection
    queries_text = ''
    for query in connection.queries:
        queries_text += '<br /><br /><br />' + str( query['sql'] )
    return HttpResponse( queries_text )
    """





#######################
# ORDER CONFIRMATION
#######################
@login_required
def confirmation( request, order_id ):
    """
    Confirmation page after a payment was made

    :param: request
    :param: order_id
    :return: String - The html page rendered
    """

    # Identify database record
    order = get_object_or_404( Order, pk = order_id, user_id = request.user.id )

    # Initializes template data dictionary
    template_data = {}

    # Defines message and status
    if order.order_status_id == 1:
        template_data['message_text'] = "Your payment was <span>received</span> and will be processed soon."
        template_data['message_css_class'] = ""
    elif order.order_status_id == 2:
        template_data['message_text'] = "Your payment was <span>approved</span>."
        template_data['message_css_class'] = "approved"
    elif order.order_status_id == 3:
        template_data['message_text'] = "Your payment was <span>denied</span>."
        template_data['message_css_class'] = "denied"
    elif order.order_status_id == 4:
        template_data['message_text'] = "Your payment was <span>cancelled</span>."
        template_data['message_css_class'] = "denied"
    elif order.order_status_id == 5:
        template_data['message_text'] = "Your payment was <span>refunded</span>."
        template_data['message_css_class'] = "approved"

    # Prints Template
    return render( request, 'marketplace/service/confirmation.html', template_data )
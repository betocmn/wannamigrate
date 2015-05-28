"""
Marketplace Views

These are the views that control logic flow for
the templates on the marketplace app
"""

##########################
# Imports
##########################
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from wannamigrate.core.util import get_object_or_false
from wannamigrate.marketplace.forms import PaymentForm
from wannamigrate.marketplace.models import (
    Provider, Review, ServiceType, ProviderServiceType, Order,
    Service, ServiceStatus
)
from wannamigrate.core.models import UserStats
from wannamigrate.core.mailer import Mailer
from wannamigrate.site.views import get_situation_form
from django.conf import settings
from django.db.models import F
from django.db import transaction





#######################
# LISTS SERVICE PROVIDERS
#######################
def professionals( request ):
    """
    Listing of professionals

    :param: request
    :return: String - The html page rendered
    """

    # Initial template
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Find and Hire an Immigration Expert - Wanna Migrate' )
    template_data['meta_description'] =  _( 'Make faster & better decisions when planning to go to another country.  Get help from immigration experts in Wanna Migrate.' )

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # If situation is defined, we load professionals related to it
    if 'situation' in request.session and 'from_country' in request.session['situation']:

        from_country = request.session['situation']['from_country']
        to_country = request.session['situation']['to_country']
        goal = request.session['situation']['goal']

        # Gets 5 most related service providers
        template_data['providers'] = Provider.get_listing( to_country.id, 0, 20 )

    # Print Template
    return render( request, 'marketplace/professionals/list.html', template_data )





#######################
# PROFILE PAGE OF A SERVICE PROVIDER
#######################
@login_required
def profile( request, user_id, name ):
    """
    View detais of a professional

    :param: request
    :return: String - The html page rendered
    """

    # If form was submitted (to proceed to payment page)
    if request.method == 'POST':

        # Identifies database records
        provider = get_object_or_false( Provider, user_id = request.POST['provider_user_id'] )
        service_type = get_object_or_false( ServiceType, pk = request.POST['service_type_id'] )
        provider_service_type = get_object_or_false( ProviderServiceType, provider_id = provider.id, service_type_id = service_type.id )
        if not provider or not service_type or not provider_service_type:
            return HttpResponseRedirect( reverse( "site:dashboard" ) )

        # saves service
        service = Service()
        service.service_price = provider_service_type.price
        service.description = service_type.name
        service.user = request.user
        service.provider = provider
        service.service_type = service_type
        service.service_status_id = ServiceStatus.get_status_from_order_status()
        service.save()

        # saves details to session
        request.session['payment'] = {
            'provider': provider,
            'service_type': service_type,
            'provider_service_type': provider_service_type,
            'service': service
        }
        return HttpResponseRedirect( reverse( "marketplace:payment" ) )

    else:

        # Cleans payment session
        request.session['payment'] = {}

        # Identify database record
        provider = Provider.get_profile( user_id )
        if not provider:
            return HttpResponseRedirect( reverse( "site:dashboard" ) )

        # Increments Profile Views if it's a new session
        if 'profile_view_incremented' not in request.session:
            request.session['profile_view_incremented'] = []
        if user_id not in request.session['profile_view_incremented']:
            request.session['profile_view_incremented'].append( user_id )
            UserStats.objects.update_or_create(
                user_id = user_id, defaults = {
                    'total_profile_views': F( 'total_profile_views' ) + 1
                }
            )

        # Initializes template data dictionary
        template_data = {}

        # Overwrites meta title and description (for SEO)
        template_data['meta_title'] = provider.display_name + ' - ' + provider.headline
        template_data['meta_description'] = provider.display_name + ' ' + _( 'can be hired through Wanna Migrate. Sign-up to connect with thousands of experts in immigration and related.' )

        # Activates Page Conversion tags for Google Ad Words
        template_data['track_conversion_view_expert'] = True

        # passes form to template
        template_data['situation_form'] = get_situation_form( request )

        # passes service provider to template
        template_data['provider'] = provider
        template_data['provider_service_types'] = ProviderServiceType.get_listing( provider.id )
        template_data['reviews'] = Review.get_listing( provider.user_id )

        # Prints Template
        return render( request, 'marketplace/professionals/profile.html', template_data )





#######################
# PAYMENT PAGE
#######################
@login_required
def payment( request ):
    """
    Payment page for hiring a professional

    :param: request
    :return: String - The html page rendered
    """

    # Only allows if coming from form submission on view professional page
    if ( 'payment' not in request.session or not request.session['payment'] ) \
        or ( 'service' not in request.session['payment'] or not request.session['payment']['service'] ):
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Payment - Wanna Migrate' )
    template_data['meta_description'] =  _( 'Make faster & better decisions when planning to go to another country.  Get help from immigration experts in Wanna Migrate.' )

    # Activates Page Conversion tags for Google Ad Words
    template_data['track_conversion_view_payment'] = True

    # If form was submitted
    if request.method == 'POST':

        # Passes order info for for
        payment_info = {
            'payment_type': request.POST.get( 'payment_type', '' ),
            'token': request.POST.get( 'token', '' ),
            'user': request.user,
            'provider': request.session['payment']['provider'],
            'service_type': request.session['payment']['service_type'],
            'provider_service_type': request.session['payment']['provider_service_type'],
            'service': request.session['payment']['service'],
            'service_type_category': request.session['payment']['service_type'].service_type_category
        }
        form = PaymentForm( request.POST, payment_info = payment_info )

        # if payment was authorized
        with transaction.atomic():
            if form.is_valid():

                # Saves all order info
                order = form.save()

                # Adds additional data to payment_info
                payment_info['order'] = order
                if 'url' in form.payment_api_result:
                    payment_info['url'] = form.payment_api_result['url']

                # Sends Order Confirmation email to USER
                # TODO Change this to a celery/signal background task
                service_type = request.session['payment']['provider_service_type'].service_type
                Mailer.send_order_confirmation_user( request.user, order, payment_info )

                # Sends Order Confirmation email to PROVIDER
                # TODO Change this to a celery/signal background task
                Mailer.send_order_confirmation_provider( request.session['payment']['provider'], order, payment_info )

                # Redirect to confirmation page
                request.session['payment'] = {}
                request.session['order_confirmation'] = {
                    'order_id': order.id,
                    'payment_type': payment_info['payment_type'],
                    'url': form.payment_api_result['url'] if 'url' in form.payment_api_result else ''
                }
                return HttpResponseRedirect( reverse( 'marketplace:confirmation' ) )

    else:
        form = PaymentForm()

    # passes data to template
    template_data['form'] = form
    template_data['situation_form'] = get_situation_form( request )
    template_data['total_price'] = request.session['payment']['provider_service_type'].price
    template_data['provider'] = request.session['payment']['provider']
    template_data['service_type'] = request.session['payment']['service_type']
    template_data['payment_api_account_id'] = settings.PAYMENT_API_ACCOUNT_ID
    template_data['payment_api_test_mode'] = True if settings.PAYMENT_API_MODE != 'LIVE' else False

    # Prints Template
    return render( request, 'marketplace/service/payment.html', template_data )





#######################
# ORDER CONFIRMATION
#######################
@login_required
def confirmation( request ):
    """
    Confirmation page after a payment was made

    :param: request
    :return: String - The html page rendered
    """

    # Identify an active session
    if 'order_confirmation' not in request.session or not request.session['order_confirmation']:
        return HttpResponseRedirect( reverse( 'site:dashboard' ) )

    # Save session and kills it, allowing 1 access only
    order_info = request.session['order_confirmation']
    request.session['order_confirmation'] = {}
    
    # Gets order detail
    order = get_object_or_404( Order, pk = order_info['order_id'] )

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Order Confirmation - Wanna Migrate' )
    template_data['meta_description'] =  _( 'Make faster & better decisions when planning to go to another country.  Get help from immigration experts in Wanna Migrate.' )

    # Activates Page Conversion tags for Google Ad Words
    template_data['track_conversion_order_received'] = True
    template_data['track_conversion_value'] = float( order.net_total ) * float( 0.05 )

    # Defines message and status
    if order.order_status_id == settings.ID_ORDER_STATUS_PENDING:
        template_data['message_text'] = _( "Your order was <span>received</span> and will be processed soon." )
        template_data['message_css_class'] = ""
    elif order.order_status_id == settings.ID_ORDER_STATUS_APPROVED:
        template_data['message_text'] = _( "Your order was <span>approved</span>." )
        template_data['message_css_class'] = "approved"
    elif order.order_status_id == settings.ID_ORDER_STATUS_DENIED:
        template_data['message_text'] = _( "Your order was <span>denied</span>." )
        template_data['message_css_class'] = "denied"
    elif order.order_status_id == settings.ID_ORDER_STATUS_CANCELLED:
        template_data['message_text'] = _( "Your order was <span>cancelled</span>." )
        template_data['message_css_class'] = "denied"
    elif order.order_status_id == settings.ID_ORDER_STATUS_REFUNDED:
        template_data['message_text'] = _( "Your order was <span>refunded</span>." )
        template_data['message_css_class'] = "approved"

    # If there's a URL for boleto
    if order_info['payment_type'] == 'boleto':
        template_data['boleto_url'] = order_info['url']

    # Prints Template
    return render( request, 'marketplace/service/confirmation.html', template_data )
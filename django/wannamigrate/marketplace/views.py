"""
Marketplace Views

These are the views that control logic flow for
the templates on the marketplace app
"""

##########################
# Imports
##########################
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from wannamigrate.core.util import get_object_or_false
from wannamigrate.marketplace.forms import PaymentForm
from wannamigrate.marketplace.models import (
    Provider, Review, ServiceType, ProviderServiceType, Order,
    Service, ServiceStatus, Product, PromoCode, Subscription,
    SubscriptionStatus, ServiceHistory
)
from wannamigrate.core.models import UserStats
from wannamigrate.core.mailer import Mailer
from wannamigrate.site.views import get_situation_form
from wannamigrate.marketplace.payment_processor import PaymentProcessor
from wannamigrate.marketplace.tasks import (
    send_order_confirmation_user, send_order_confirmation_provider
)
from wannamigrate.core.decorators import subscription_required
from django.conf import settings
from django.db.models import F
from django.db import transaction
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.servers.basehttp import FileWrapper
from django.views.decorators.csrf import csrf_exempt
from django.utils import translation
from django.templatetags.static import static
import datetime
from datetime import timedelta
from django.utils import timezone





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
    if 'situation' in request.session and 'to_country' in request.session['situation']:

        # Gets 5 most related service providers
        template_data['providers'] = Provider.get_listing( request.session['situation']['to_country']['id'], 0, 20 )

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
            'provider': { 'id': provider.id, 'name': provider.display_name },
            'service_type': { 'id': service_type.id, 'name': service_type.name },
            'provider_service_type': { 'id': provider_service_type.id, 'price': provider_service_type.price },
            'service': { 'id': service.id, 'service_price': service.service_price, 'description': service.description }
        }
        return HttpResponseRedirect( reverse( "marketplace:payment" ) )

    else:

        # Cleans payment session
        request.session['payment'] = {}
        del request.session['payment']

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
# EBOOKS - VIEWS
#######################
def ebook( request ):
    """
    List all e-boks available

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initializes template data dictionary
    template_data = {}

    # If form was submitted (to proceed to payment page)
    if request.method == 'POST':

        # Identifies database records
        product = get_object_or_false( Product, pk = request.POST['product_id'], is_active = True )
        if not product:
            return HttpResponseRedirect( reverse( "site:dashboard" ) )

        # saves details to session
        request.session['payment'] = {
            'product': { 'id': product.id, 'name': product.name, 'price': product.price, 'product_category_id': product.product_category_id }
        }

        return HttpResponseRedirect( reverse( "marketplace:payment" ) )

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'E-Books - Immigration Guides - Wanna Migrate' )
    template_data['meta_description'] = _( 'Download our complete guides about immigrating to Canada, immigration to Australia and others.' )

    # Sets image as preview for sharing (as for facebook, twitter, etc.)
    template_data['meta_image'] = settings.BASE_URL + static( 'site/img/e-book-como-mudar-para-o-canada-preview-1.jpg' )

    # Activates Page Conversion tags for Google Ad Words
    template_data['track_conversion_view_ebooks'] = True

    # if language is english, we show warning that only portuguese guides are available for now
    if translation.get_language() == "en":
        messages.warning( request, "All e-books are in portuguese for now. We will soon release the english versions." )

    # Print Template
    return render( request, 'marketplace/ebook/ebook.html', template_data )


@subscription_required
def ebook_read( request, country_name ):
    """
    Read E-book PDF

    :param: request
    :param country_name:
    :return: String - HTML
    """

    # Initial settings
    template_data = { 'country_name': country_name }

    # Get Country and set options for it
    if country_name == 'canada' and settings.ID_COUNTRY_CANADA in request.session['subscription']['countries']:
        template_data['ebook_url'] = 'https://drive.google.com/file/d/0B3qN5CaSfrjhWjZpdWJyUS1ZNkk/preview'

    elif country_name == 'australia' and settings.ID_COUNTRY_AUSTRALIA in request.session['subscription']['countries']:
        template_data['ebook_url'] = 'https://drive.google.com/file/d/0B3qN5CaSfrjhejNoMkNtZjBiOVU/preview'

    else:
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Print Template
    return render( request, 'marketplace/ebook/read.html', template_data )






#######################
# IELTS COURSE - VIEWS
#######################
def ielts( request ):
    """
    Sales page for IELTS Course

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initializes template data dictionary
    template_data = {}

    # If form was submitted (to proceed to payment page)
    if request.method == 'POST':

        # Identifies database records
        provider = get_object_or_false( Provider, pk = 13 )
        service_type = get_object_or_false( ServiceType, pk = request.POST['service_type_id'] )
        provider_service_type = get_object_or_false( ProviderServiceType, provider_id = provider.id, service_type_id = service_type.id )
        if not provider or not service_type or not provider_service_type:
            return HttpResponseRedirect( reverse( "site:dashboard" ) )

        # order information
        payment_info = {
            'provider': { 'id': provider.id, 'name': provider.display_name },
            'service_type': { 'id': service_type.id, 'name': service_type.name },
            'provider_service_type': { 'id': provider_service_type.id, 'price': provider_service_type.price },
        }

        # saves service
        if request.user.is_authenticated():
            service = Service()
            service.service_price = provider_service_type.price
            service.description = service_type.name
            service.user = request.user
            service.provider = provider
            service.service_type = service_type
            service.service_status_id = ServiceStatus.get_status_from_order_status()
            service.save()
            payment_info['service'] = { 'id': service.id, 'service_price': service.service_price, 'description': service.description }

        # saves details to session
        request.session['payment'] = payment_info

        return HttpResponseRedirect( reverse( "marketplace:payment" ) )

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'IELTS Online Course - Wanna Migrate' )
    template_data['meta_description'] = _( 'Get ready for the English Exam for immigration with IELTS Online course.' )

    # Sets image as preview for sharing (as for facebook, twitter, etc.)
    template_data['meta_image'] = settings.BASE_URL + static( 'site/img/ielts-course-preview-image.jpg' )

    # Activates Page Conversion tags for Google Ad Words
    template_data['track_conversion_view_ielts_course'] = True


    # Print Template
    return render( request, 'marketplace/ielts/ielts.html', template_data )





#######################
# INTERNATIONAL CV - VIEWS
#######################
def international_cv( request ):
    """
    Sales page for the service 'international CV'

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initializes template data dictionary
    template_data = {}

    # If form was submitted (to proceed to payment page)
    if request.method == 'POST':

        # Identifies database records
        provider = get_object_or_false( Provider, pk = 13 )
        service_type = get_object_or_false( ServiceType, pk = request.POST['service_type_id'] )
        provider_service_type = get_object_or_false( ProviderServiceType, provider_id = provider.id, service_type_id = service_type.id )
        if not provider or not service_type or not provider_service_type:
            return HttpResponseRedirect( reverse( "site:dashboard" ) )

        # order information
        payment_info = {
            'provider': { 'id': provider.id, 'name': provider.display_name },
            'service_type': { 'id': service_type.id, 'name': service_type.name },
            'provider_service_type': { 'id': provider_service_type.id, 'price': provider_service_type.price },
        }

        # saves service
        if request.user.is_authenticated():
            service = Service()
            service.service_price = provider_service_type.price
            service.description = service_type.name
            service.user = request.user
            service.provider = provider
            service.service_type = service_type
            service.service_status_id = ServiceStatus.get_status_from_order_status()
            service.save()
            payment_info['service'] = { 'id': service.id, 'service_price': service.service_price, 'description': service.description }

        # saves details to session
        request.session['payment'] = payment_info

        return HttpResponseRedirect( reverse( "marketplace:payment" ) )

    else:
        # Cleans payment session
        request.session['payment'] = {}
        del request.session['payment']

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Build your International CV - Wanna Migrate' )
    template_data['meta_description'] = _( 'We will help you out by creating your international CV, cover letter and Linkedin profile.' )

    # Sets image as preview for sharing (as for facebook, twitter, etc.)
    template_data['meta_image'] = settings.BASE_URL + static( 'site/img/international-cv-preview-1.jpg' )

    # Activates Page Conversion tags for Google Ad Words
    template_data['track_conversion_view_international_cv'] = True

    # Print Template
    return render( request, 'marketplace/international_cv/international_cv.html', template_data )





#######################
# IMMI BOX SUBSCRIPTION - VIEWS
#######################
def immi_box( request ):
    """
    Home-Page for "Immi Box".

    :param: request
    :return String - HTML
    """

    # If there's no active subscription, we redirect to the subscription page
    if 'subscription' not in request.session or request.session['subscription'] is None:
        return HttpResponseRedirect( reverse( "marketplace:subscription" ) )
    elif request.session['situation']['to_country']['id'] not in request.session['subscription']['countries']:
        messages.warning( request, _( "You don't have an active subscription for this country. You can change your destination country above!" ) )

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Immi Box - Immigration Tools - Wanna Migrate' )
    template_data['meta_description'] = _( 'Powerful immigration tools to help you to immigrate to your dream country.' )

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # Print Template
    return render( request, 'marketplace/immi_box/immi_box.html', template_data )


def subscription( request ):
    """
    Sales page for the subscription service

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initializes template data dictionary
    template_data = {}
    error = False

    # If form was submitted (to proceed to payment page)
    if request.method == 'POST':

        # Identifies database records
        product = get_object_or_false( Product, pk = request.POST['product_id'], is_active = True )
        if not product:
            return HttpResponseRedirect( reverse( "site:dashboard" ) )

        # saves details to session
        payment_info = {
            'product': { 'id': product.id, 'name': product.name, 'price': product.price, 'product_category_id': product.product_category_id }
        }

        # saves subscription
        if request.user.is_authenticated() and product.product_category_id in settings.SUBSCRIPTION_PRODUCT_CATEGORIES:

            subscription = get_object_or_false(
                Subscription,
                user_id = request.user.id,
                product_id = product.id,
                subscription_status_id = settings.ID_SUBSCRIPTION_STATUS_ACTIVE
            )
            if subscription:
                error = True
                messages.error( request, _( "There's already an active subscription for this country and product." ) )
            else:
                subscription = Subscription()
                subscription.product_id = product.id
                subscription.subscription_status_id = SubscriptionStatus.get_status_from_order_status()
                subscription.user = request.user
                subscription.save()
                payment_info['subscription'] = { 'id': subscription.id, 'subscription_status_id': subscription.subscription_status_id }

        if not error:
            # saves details to session and redirect
            request.session['payment'] = payment_info
            return HttpResponseRedirect( reverse( "marketplace:payment" ) )

    else:
        # Cleans payment session
        request.session['payment'] = {}
        del request.session['payment']

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Immi Box - Immigration Tools - Wanna Migrate' )
    template_data['meta_description'] = _( 'Powerful immigration tools to help you to immigrate to your dream country.' )

    # Activates Page Conversion tags for Google Ad Words
    template_data['track_conversion_view_subscription_plan'] = True

    # Print Template
    return render( request, 'marketplace/immi_box/subscription.html', template_data )



#######################
# CONSULTING - VIEWS
#######################
def consulting( request ):
    """
    List all consulting options available

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initializes template data dictionary
    template_data = {}

    # If form was submitted (to proceed to payment page)
    if request.method == 'POST':

        # Identifies database records
        provider = get_object_or_false( Provider, pk = 30 )
        service_type = get_object_or_false( ServiceType, pk = request.POST['service_type_id'] )
        provider_service_type = get_object_or_false( ProviderServiceType, provider_id = provider.id, service_type_id = service_type.id )
        if not provider or not service_type or not provider_service_type:
            return HttpResponseRedirect( reverse( "site:dashboard" ) )

        # order information
        payment_info = {
            'provider': { 'id': provider.id, 'name': provider.display_name },
            'service_type': { 'id': service_type.id, 'name': service_type.name },
            'provider_service_type': { 'id': provider_service_type.id, 'price': provider_service_type.price },
        }

        # saves service
        if request.user.is_authenticated():
            service = Service()
            service.service_price = provider_service_type.price
            service.description = service_type.name
            service.user = request.user
            service.provider = provider
            service.service_type = service_type
            service.service_status_id = ServiceStatus.get_status_from_order_status()
            service.save()
            payment_info['service'] = { 'id': service.id, 'service_price': service.service_price, 'description': service.description }

        # saves details to session
        request.session['payment'] = payment_info

        return HttpResponseRedirect( reverse( "marketplace:payment" ) )

    else:
        # Cleans payment session
        request.session['payment'] = {}
        del request.session['payment']

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Immigration Evaluation - Wanna Migrate' )
    template_data['meta_description'] = _( 'In-person meeting to evaluate your chances to immigrate to Canada or Australia.' )

    # Sets image as preview for sharing (as for facebook, twitter, etc.)
    template_data['meta_image'] = settings.BASE_URL + static( 'site/img/consulting-individual.png' )

    # Activates Page Conversion tags for Google Ad Words
    #template_data['track_conversion_view_ebooks'] = True

    # if language is english, we show warning that only portuguese guides are available for now
    if translation.get_language() == "en":
        messages.warning( request, "All sessions are in portuguese for now. We will soon release the english edition." )

    # Print Template
    return render( request, 'marketplace/consulting/consulting.html', template_data )



#######################
# PAYMENT PAGE
#######################
@login_required( login_url = 'site:signup' )
def payment( request ):
    """
    Payment page for hiring a professional

    :param: request
    :return: String - The html page rendered
    """

    # Only allows if coming from form submission on a page that set a session
    if ( 'payment' not in request.session or not request.session['payment'] ) \
        or ( 'service_type' not in request.session['payment'] and 'product' not in request.session['payment'] ):
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # defines if it's a service, and if not, if product is subscription
    is_service = True if 'service_type' in request.session['payment'] else False
    is_subscription = False

    # If it's a service or a product with subscription, make sure extra data has been saved
    if is_service and 'service' not in request.session['payment']:
        service = Service()
        service.service_price = request.session['payment']['provider_service_type']['price']
        service.description = request.session['payment']['service_type']['name']
        service.user = request.user
        service.provider_id = request.session['payment']['provider']['id']
        service.service_type_id = request.session['payment']['service_type']['id']
        service.service_status_id = ServiceStatus.get_status_from_order_status()
        service.save()
        request.session['payment']['service'] = { 'id': service.id, 'service_price': service.service_price, 'description': service.description }
    elif not is_service:
        if request.session['payment']['product']['product_category_id'] in settings.SUBSCRIPTION_PRODUCT_CATEGORIES:
            is_subscription = True
            if 'subscription' not in request.session['payment']:
                subscription = get_object_or_false(
                    Subscription,
                    user_id = request.user.id,
                    product_id = request.session['payment']['product']['id'],
                    subscription_status_id = settings.ID_SUBSCRIPTION_STATUS_ACTIVE
                )
                if subscription:
                    messages.error( request, _( "There's already an active subscription for this country and product." ) )
                    del request.session['payment']
                    return HttpResponseRedirect( reverse( 'marketplace:subscription' ) )
                else:
                    subscription = Subscription()
                    subscription.product_id = request.session['payment']['product']['id']
                    subscription.subscription_status_id = SubscriptionStatus.get_status_from_order_status()
                    subscription.user = request.user
                    subscription.save()
                    request.session['payment']['subscription'] = { 'id': subscription.id, 'subscription_status_id': subscription.subscription_status_id }

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Payment - Wanna Migrate' )
    template_data['meta_description'] =  _( 'Make faster & better decisions when planning to go to another country.  Get help from immigration experts in Wanna Migrate.' )

    # Activates Page Conversion tags for Google Ad Words
    template_data['track_conversion_view_payment'] = True

    # If form was submitted
    if request.method == 'POST':

        # Creates order information dictionary (will be used on form)
        payment_info = {
            'payment_type_id': int( request.POST.get( 'payment_type_id', '' ) ),
            'token': request.POST.get( 'token', '' ),
            'user': request.user,
            'is_service': is_service
        }
        if is_service:
            provider = Provider.objects.get( pk = request.session['payment']['provider']['id'] )
            payment_info['provider'] = provider
            payment_info['service_type'] = request.session['payment']['service_type']
            payment_info['provider_service_type'] = request.session['payment']['provider_service_type']
            payment_info['service'] = request.session['payment']['service']
        else:
            provider = None
            payment_info['product'] = request.session['payment']['product']
            if 'subscription' in request.session['payment']:
                payment_info['subscription'] = request.session['payment']['subscription']

        # Instantiates form passing the payment info
        form = PaymentForm( request.POST, payment_info = payment_info )

        # if payment was authorized
        with transaction.atomic():
            if form.is_valid():

                # Saves all order info
                order = form.save()

                # Cleans out session and set just enough for confirmation page
                del request.session['payment']
                request.session['order_confirmation'] = {}
                request.session['order_confirmation']['order_id'] = order.id
                request.session['order_confirmation']['is_service'] = is_service
                request.session['order_confirmation']['is_subscription'] = is_subscription
                request.session['order_confirmation']['payment_type_id'] = payment_info['payment_type_id']
                request.session['order_confirmation']['url'] = form.payment_api_result['url'] if 'url' in form.payment_api_result else ''

                # Add celery background tasks to send out confirmation emails
                send_order_confirmation_user.delay( request.user, order, provider )
                if order.service_id and order.order_status_id == settings.ID_ORDER_STATUS_APPROVED:
                    send_order_confirmation_provider.delay( request.user, order, provider )

                # Redirects to confirmation page
                return HttpResponseRedirect( reverse( 'marketplace:confirmation' ) )

    else:
        form = PaymentForm()

    # passes data to template
    template_data['form'] = form
    template_data['is_service'] = is_service
    template_data['situation_form'] = get_situation_form( request )
    template_data['payment_api_account_id'] = settings.PAYMENT_API_ACCOUNT_ID
    template_data['payment_api_test_mode'] = True if settings.PAYMENT_API_MODE != 'LIVE' else False
    if is_service:
        template_data['total_price'] = request.session['payment']['provider_service_type']['price']
        template_data['provider'] = Provider.objects.get( pk = request.session['payment']['provider']['id'] )
        template_data['provider_user'] = template_data['provider'].user
        template_data['service_type'] = ServiceType.objects.get( pk = request.session['payment']['service_type']['id'] )
    else:
        template_data['total_price'] = request.session['payment']['product']['price']
        template_data['product'] = Product.objects.get( pk = request.session['payment']['product']['id'] )

    # Prints Template
    return render( request, 'marketplace/order/payment.html', template_data )



def get_promo_discount( request ):
    """
    Returns discount (in percent) from a promo code

    :param: request
    :return String
    """

    # Only allows if there's a payment session activated
    if ( 'payment' not in request.session or not request.session['payment'] ) \
        or ( 'service_type' not in request.session['payment'] and 'product' not in request.session['payment'] ):
        return ''

    # Searches for promo code
    result = 0
    if request.is_ajax() and request.method == 'POST':

        code = request.POST['promo_code']

        # Runs query accordingly to order type (product or service)
        if 'service_type' in request.session['payment']:
            service_type_id = request.session['payment']['service_type']['id']
            promo_code = get_object_or_false(
                PromoCode,
                name = code,
                expiry_date__gte = datetime.date.today(),
                service_type_id = service_type_id
            )
        else:
            product_id = request.session['payment']['product']['id']
            promo_code = get_object_or_false(
                PromoCode,
                name = code,
                expiry_date__gte = datetime.date.today(),
                product_id = product_id
            )

        if promo_code:
            result = promo_code.discount

    return HttpResponse( result )




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

    # Identifies an active session
    if 'order_confirmation' not in request.session or not request.session['order_confirmation']:
        return HttpResponseRedirect( reverse( 'site:dashboard' ) )

    # Identifies order
    order = get_object_or_false( Order, pk = request.session['order_confirmation']['order_id'] )
    if not order:
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Saves session and kills it, allowing 1 access only
    order_info = request.session['order_confirmation']
    request.session['order_confirmation'] = {}

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
        if order_info['is_subscription']:
            template_data['extra_message'] = _( "You can now click on 'Immi Box' from the top menu to access the premium area." )
        template_data['message_css_class'] = "approved"
        del request.session['subscription']
    elif order.order_status_id == settings.ID_ORDER_STATUS_DENIED:
        template_data['message_text'] = _( "Your order was <span>denied</span>." )
        template_data['message_css_class'] = "denied"
    elif order.order_status_id == settings.ID_ORDER_STATUS_CANCELLED:
        template_data['message_text'] = _( "Your order was <span>cancelled</span>." )
        template_data['message_css_class'] = "denied"
    elif order.order_status_id == settings.ID_ORDER_STATUS_REFUNDED:
        template_data['message_text'] = _( "Your order was <span>refunded</span>." )
        template_data['message_css_class'] = "approved"

    # If there's an URL for boleto
    if order_info['payment_type_id'] == 2:
        template_data['boleto_url'] = order_info['url']

    # Prints Template
    return render( request, 'marketplace/order/confirmation.html', template_data )



#######################
# UPDATE ORDER STATUS
#######################
@csrf_exempt
@sensitive_post_parameters()
@never_cache
def payment_api_updated( request ):
    """
    When there's a trigger 'updated' the payment API sends
    the data to this view, which needs to run some actions
    inside.

    :param: request
    :return: Boolean
    """

    # If form was submitted
    if request.method == 'POST' and 'event' in request.POST and request.POST['event'] == 'invoice.status_changed':

        # gets post data from API request
        payment_processor = PaymentProcessor()
        external_code = request.POST['data[id]']
        order_status_id = payment_processor.get_order_status_id( request.POST['data[status]'] )

        # identifies order by external code (invoice ID)
        order = get_object_or_false( Order, external_code = external_code )
        if not order:
            return HttpResponse( 'False' )

        # If it's an approval update of an order which was already approved, we stop it here
        if order_status_id == settings.ID_ORDER_STATUS_APPROVED and order.order_status_id == settings.ID_ORDER_STATUS_APPROVED:
            return HttpResponse( 'False' )

        # updates order status
        order.order_status_id = order_status_id
        order.save()

        # updates service status
        if order.service_id:
            service = Service.objects.get( pk = order.service_id )
            service.service_status_id = ServiceStatus.get_status_from_order_status( order.order_status_id )
            service.save()
            service_history = ServiceHistory()
            service_history.service_id = service.id
            service_history.service_status_id = service.service_status_id
            service_history.user_id = service.user_id
            service_history.save()

        # updates subscription status
        else:
            product = get_object_or_false( Product, pk = order.product_id )
            if product.product_category_id in settings.SUBSCRIPTION_PRODUCT_CATEGORIES:
                subscription = Subscription.objects.get( product_id = product.id, user_id = order.user_id )
                subscription.subscription_status_id = SubscriptionStatus.get_status_from_order_status( order.order_status_id )
                if subscription.subscription_status_id == settings.ID_SUBSCRIPTION_STATUS_ACTIVE:
                    subscription.start_date = timezone.now()
                    subscription.expiry_date = timezone.now() + timedelta( days = 365 ) #@TODO improve this to use year
                subscription.save()

        # updates subscription status

        # Gets user and provider from order
        user = order.user
        if order.service_id:
            provider = order.service.provider
        else:
            provider = None

        # sets user language
        preferred_language = user.preferred_language
        if not preferred_language:
            preferred_language = 'en'
        translation.activate( preferred_language )
        request.session[translation.LANGUAGE_SESSION_KEY] = preferred_language

        # Sends Order Confirmation email to USER
        if order_status_id in [settings.ID_ORDER_STATUS_APPROVED, settings.ID_ORDER_STATUS_PENDING, settings.ID_ORDER_STATUS_REFUNDED]:
            Mailer.send_order_confirmation_user( user, order, provider )

        # Sends Order Confirmation email to PROVIDER
        if order.service_id and order_status_id == settings.ID_ORDER_STATUS_APPROVED:
            Mailer.send_order_confirmation_provider( user, order, provider )

        return HttpResponse( 'True' )

    return HttpResponse( 'False' )
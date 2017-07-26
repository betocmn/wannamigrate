"""
Landing Views

These are the views that control logic flow for
the templates on landing pages
"""

##########################
# Imports
##########################
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from wannamigrate.order.models import Order, Product, PromoCode
from wannamigrate.member.models import Member
from wannamigrate.core.util import get_object_or_false, format_monetary, date_now
from wannamigrate.order.tasks import process_order, create_alert


#######################
# HOME-PAGE VIEWS
#######################
@login_required(login_url='member:signup')
def checkout(request):
    """
    Checkout

    :param request:
    :return: String
    """

    # If already subscribed
    if 'subscription_id' in request.session and request.session['subscription_id']:
        return redirect('member:dashboard')

    # If user has an incomplete profile (e.g. just completed the quiz)
    if not request.user.first_name or not request.user.last_name:
        return redirect('%s?next=%s' % (reverse("member:signup"), reverse("order:checkout")))

    # Retrieves member
    member = get_object_or_404(Member, user=request.user)

    # Initialises the checkout session
    if 'checkout' not in request.session:

        # Setups dict
        request.session['checkout'] = {
            'total': 15, 'discount': None, 'discount_code': None, 'products': []
        }

    # Retrieves order total and discount
    order_total = request.session['checkout']['total']
    discount_value = None
    discount_code = None
    if 'discount' in request.session['checkout'] and request.session['checkout']['discount']:
        discount_code = request.session['checkout']['discount_code']
        discount_value = request.session['checkout']['discount']
        order_total -= discount_value

    # If there was a payment error (debug purposes)
    payment_error = {}
    if 'payment_error' in request.session:
        payment_error = request.session['payment_error']

    # Builds template data dictionary
    template_data = {
        'member': member,
        'order_total': order_total,
        'discount_code': discount_code,
        'discount_value': discount_value,
        'payment_error': payment_error,
        'tracking_event_typed_payment_details': settings.TRACKING_EVENT_TYPED_PAYMENT_DETAILS,
        'tracking_event_proceeded_to_payment': settings.TRACKING_EVENT_PROCEEDED_TO_PAYMENT,
        'meta_title': _('Checkout | Wanna Migrate'),
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    }

    # Displays HTML template
    return render(request, 'order/checkout.html', template_data)


@login_required
def get_promo_info(request):
    """
    Retrieves information for a promo or referral code

    :param: request
    :return: Json
    """

    # Checks if a code was given
    code = request.GET.get('code', False)
    order_total = request.GET.get('order_total', False)
    discount_value = None
    discount_percentage = None
    response = {'status': 'error', 'message': 'Invalid code'}
    if code and order_total:

        # Searches for PROMO Code
        code = code.upper()
        promo_code = get_object_or_false(
            PromoCode,
            name=code, expiry_date__gte=date_now().to_date_string()
        )
        if promo_code:
            discount_value = promo_code.discount_value
            discount_percentage = promo_code.discount_percentage

        # Calculates the discount
        if discount_value or discount_percentage:
            if 'checkout' in request.session:
                if discount_percentage:
                    total = format_monetary(order_total)
                    discount_percentage = format_monetary(discount_percentage)
                    discount_value = format_monetary(total * (discount_percentage / 100))
                request.session['checkout']['discount'] = float(discount_value)
                request.session['checkout']['discount_code'] = code
                request.session.modified = True
                response = {'status': 'success', 'discount': discount_value}

    return JsonResponse(response, safe=False)


@login_required
@transaction.atomic
def process_payment(request):
    """
    Performs the payment using the checkout session and a posted
    Stripe token.

    :param: request
    :return: JSON
    """

    # If already subscribed
    if 'subscription_id' in request.session and request.session['subscription_id']:
        return redirect('member:dashboard')

    # If user has an incomplete profile (e.g. just completed the quiz)
    if not request.user.first_name or not request.user.last_name:
        return redirect('%s?next=%s' % (reverse("member:signup"), reverse("order:checkout")))

    # Retrieves member
    member = get_object_or_404(Member, user=request.user)

    # If form was submitted
    if request.method == 'POST':

        # Checks if a payment token was passed
        token = request.POST.get('token', False)
        if not token:
            messages.error(request, _('No payment details provided.'))
            create_alert.delay(
                "Process Order Error",
                "No payment details provided.\nMember: %s" % member
            )
            return redirect("order:checkout")

        # Builds the product dict
        product_id = request.POST.get('product_id', False)
        product = None
        if product_id:
            product = get_object_or_false(Product, id=product_id)
        if not product:
            messages.error(request, _('No product details provided.'))
            create_alert.delay(
                "Process Order Error",
                "No product details provided.\nMember: %s" % member
            )
            return redirect("order:checkout")
        products = [{
            'product_id': product.id, 'product_name': product.name,
            'product_price': float(product.price)
        }]
        request.session['checkout']['products'] = products

        # Calculates order total and saves in the session
        request.session['checkout']['total'] = float(product.price)
        request.session.modified = True

        # Initial Order data
        order = None
        subscription = None
        discount_value = None
        discount_code = None
        if 'discount' in request.session['checkout'] and request.session['checkout']['discount']:
            discount_value = request.session['checkout']['discount']
            discount_code = request.session['checkout']['discount_code']

        # Retrieves order totals
        gross_total = request.session['checkout']['total']

        # If order was already saved (so this is coming from a payment retry)
        if 'checkout_order_id' in request.session and request.session['checkout_order_id']:
            order = get_object_or_false(Order, pk=request.session['checkout_order_id'])
            if order:
                gross_total = order.gross_total
                subscription = order.subscription

        # Processes order
        result = process_order(
            member, products=request.session['checkout']['products'],
            order=order, payment_token=token, subscription=subscription,
            create_subscription_if_none=True, discount_value=discount_value,
            discount_code=discount_code, gross_total=gross_total
        )

        # Process order response
        if not result:

            # Unexpected error
            create_alert.delay(
                "Invalid Data on New Order",
                "Attention Needed: Investigate invalid data for this order:"
                "\nOrder ID: %s \nStatus: %s \nMember: %s %s" % (
                    order.id, order.order_status.name, member.user.first_name, member.user.last_name
                ),
            )
            messages.error(request, _('We found invalid data on your account, please contact us.'))
            return redirect("order:checkout")

        else:

            # Saves order in the session so that we don't try to insert all over again
            order = result['order']
            request.session['checkout_order_id'] = order.id

            # If payment failed, stops here and redirects back for a new attempt
            payment_result = result['payment_result']
            if payment_result['status'] != 'success':
                messages.error(request, _('Your payment was not approved. Please try again.'))
                request.session['payment_error'] = payment_result
                return redirect("order:checkout")

            else:

                # Success! Redirects to thank you page
                del request.session['checkout_order_id']
                del request.session['checkout']
                request.session['subscription_id'] = result['subscription'].id
                request.session['thankyou_order_id'] = order.id
                request.session['thankyou_order_track_js'] = True
                return redirect("order:thank_you")

    return redirect("order:checkout")


@login_required
def thank_you(request):
    """
    Thank you (Confirmation) page

    :param: request
    :return: String HTML
    """

    # Makes sure order was completed
    if 'thankyou_order_id' not in request.session or not request.session['thankyou_order_id']:
        return redirect('landing:home')

    # Identifies order
    order = get_object_or_false(Order, pk=request.session['thankyou_order_id'])
    if not order:
        return redirect('landing:home')

    # Defines if we should track the order
    track_order = False
    if 'thankyou_order_track_js' in request.session and request.session['thankyou_order_track_js']:
        track_order = True
        request.session['thankyou_order_track_js'] = False

    # Builds template data dictionary
    template_data = {
        'meta_title': 'Order Confirmation | Wanna Migrate',
        'order': order,
        'track_order': track_order,
        'tracking_event_placed_order': settings.TRACKING_EVENT_PLACED_ORDER,
    }

    # Displays HTML template
    return render(request, 'order/thank_you.html', template_data)

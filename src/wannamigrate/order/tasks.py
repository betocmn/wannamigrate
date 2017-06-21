"""
General tasks with the option to run in the background with Celery
"""

##########################
# Imports
##########################
import json
from django.conf import settings
from django.db.models import Q, F, Sum
from django.db import transaction
from celery import shared_task
from wannamigrate.core.tasks import create_alert
from wannamigrate.core.payment_processor import PaymentProcessor
from wannamigrate.core.util import (
    date_now, format_monetary, calculate_gst, get_object_or_false, date_subtract, date_add,
    date_from_params
)
from wannamigrate.order.models import Order, OrderItem, OrderHistory, PromoCode, Subscription
from wannamigrate.member.tasks import track_payment_failure


##########################
# Function Definitions
##########################
@transaction.atomic
def process_order(member, products=None, gross_total=None, order=None, payment_token=None,
                  subscription=None, create_subscription_if_none=False,
                  discount_code=None, discount_value=None):
    """
    Processes and saves all order details.

    1- Process payment
    2- If it's a new order, save all related details (items, subscription, stock, etc..)
    3- Update order and subscription status accordingly to payment result

    :param member: object
    :param products: list with 'product_id', 'product_name', 'product_price' and 'product_quantity'
    :param gross_total: float
    :param order: object
    :param payment_token: string
    :param subscription: object
    :param create_subscription_if_none: boolean
    :param discount_code: string
    :param discount_value: float
    :return: dictionary payment result on success, boolean false on failure
    """

    # If it's a new order, gross_total and products are required
    if not order and (not gross_total or not products):
        return False

    # If it's an existing order already approved
    if order and order.order_status_id == settings.DB_ID_ORDER_STATUS_CHARGED_SUCCEEDED:
        return False

    # Organises order totals
    if order:
        gross_total = format_monetary(order.gross_total)
        if order.discount:
            discount_value = format_monetary(order.discount)
        if gross_total and discount_value:
            net_total = format_monetary(gross_total - format_monetary(discount_value))
        else:
            net_total = gross_total
        gst = calculate_gst(net_total)
    else:
        gross_total = format_monetary(gross_total)
        if discount_value:
            discount_value = format_monetary(discount_value)
        if gross_total and discount_value:
            net_total = format_monetary(gross_total - format_monetary(discount_value))
        else:
            net_total = gross_total
        gst = calculate_gst(net_total)

    # If discount was greater than total value
    if net_total < 0:
        net_total = format_monetary(0.00)
        gst = format_monetary(0.00)

    # Performs external payment charge
    payment_processor = PaymentProcessor()
    payment_result = payment_processor.charge(
        member, net_total, token=payment_token
    )
    payment_ok = payment_result['order_status_id'] == settings.DB_ID_ORDER_STATUS_CHARGED_SUCCEEDED

    # If it's a subscription, save its details
    if subscription or create_subscription_if_none:

        # Updates subscription details
        if not subscription:
            subscription = get_object_or_false(Subscription, member_id=member.id)
        if not subscription:
            subscription = Subscription()
            subscription.member_id = member.id
        if payment_ok:
            subscription.subscription_status_id = settings.DB_ID_SUBSCRIPTION_STATUS_ACTIVE
            # TODO: Retrieve from product table when using more products
            subscription.expiry_date = date_add(date_now(), years=1)
        else:
            subscription.subscription_status_id = settings.DB_ID_SUBSCRIPTION_STATUS_NEVER_ACTIVATED
        subscription.save()

    # Creates or updates order details
    if order:

        # Updates existing Order details after new payment result
        order.order_status_id = payment_result['order_status_id']
        if subscription:
            order.subscription = subscription
        if 'transaction_uuid' in payment_result['api_response']:
            order.payment_api_transaction_uuid = payment_result['api_response']['transaction_uuid']
        if 'fee' in payment_result['api_response']:
            order.payment_fees = format_monetary(payment_result['api_response']['fee'])
        order.save()

        # This is a retry payment
        is_retry = True

    else:

        # Creates Order
        order = Order()
        order.member = member
        order.payment_type_id = settings.DB_ID_PAYMENT_TYPE_STRIPE_CARDS
        order.order_status_id = payment_result['order_status_id']
        if subscription:
            order.subscription = subscription
        order.gross_total = gross_total
        order.net_total = net_total
        order.gst = gst
        order.discount = discount_value
        order.discount_code = discount_code
        if 'fee' in payment_result['api_response']:
            order.payment_fees = format_monetary(payment_result['api_response']['fee'])
        if 'transaction_uuid' in payment_result['api_response']:
            order.payment_api_transaction_uuid = payment_result['api_response']['transaction_uuid']
        order.save()

        # Creates Order Items
        order_items = []
        for item in products:
            order_item = OrderItem()
            order_item.order = order
            order_item.product_id = item['product_id']
            order_item.product_name = item['product_name']
            order_item.product_price = format_monetary(item['product_price'])
            order_item.quantity_ordered = 1
            order_item.save()
            order_items.append(order_item)

        # This is a new order
        is_retry = False

    # Logs Order History
    order_history = OrderHistory()
    order_history.order = order
    order_history.order_status_id = order.order_status_id
    order_history.payment_api_transaction_uuid = order.payment_api_transaction_uuid
    order_history.full_api_response = json.dumps(payment_result)
    order_history.save()

    # If payment was approved
    if payment_ok:

        # Update promo code usage in the background
        if discount_code and discount_value:
            update_promo_code_usage.delay(discount_code)

    return {
        'payment_result': payment_result, 'order': order, 'subscription': subscription,
        'discount_code': discount_code,  'discount_value': discount_value,
    }


@shared_task
def update_promo_code_usage(discount_code):
    """
    If promo code has an usage limit and this is reached, disable it right away

    :param discount_code: str
    """
    promo_code = get_object_or_false(PromoCode, name=discount_code)
    if promo_code and promo_code.usage_limit:
        order_count = Order.objects.filter(
            order_status_id=settings.DB_ID_ORDER_STATUS_CHARGED_SUCCEEDED,
            discount_code__iexact=discount_code
        ).count()
        if order_count and order_count >= promo_code.usage_limit:
            promo_code.is_gift_enabled = False
            promo_code.is_subscription_enabled = False
            promo_code.is_oneoff_enabled = False
            promo_code.save()

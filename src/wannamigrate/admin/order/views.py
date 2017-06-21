"""
Order Views

These are the views that control logic flow for
the crud operations.
"""

##########################
# Imports
##########################
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.http import urlsafe_base64_encode
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import F, CharField, Value
from django.db.models.functions import Concat
from django.conf import settings
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import user_passes_test, permission_required
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import (
    build_datatable_json, format_monetary, calculate_gst, get_object_or_false,
    remove_non_alphanumeric
)
from wannamigrate.order.models import Order, OrderItem
from wannamigrate.admin.login.views import admin_check
from wannamigrate.admin.order.forms import (
    AddOrderForm, EditOrderForm, OrderItemForm
)
from wannamigrate.core.tasks import create_alert
from wannamigrate.core.payment_processor import PaymentProcessor
from wannamigrate.member.models import Member
from wannamigrate.order.tasks import process_order


#######################
# ORDER VIEWS
#######################
@restrict_internal_ips
@permission_required('member.admin_add_credit', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new Credit

    :param: request
    :return: String
    """

    # Instantiate FORM
    order_form = AddOrderForm(request.POST or None)

    # Order Items FORMSET
    OrderItemInlineFormset = inlineformset_factory(
        Order, OrderItem, form=OrderItemForm, extra=1, can_delete=True
    )
    order_item_formset = OrderItemInlineFormset(
        request.POST or None, instance=order_form.instance
    )

    # If form was submitted, it tries to validate order details
    if order_form.is_valid():

        # Retrievers OrderItem Info
        if order_item_formset.is_valid():

            # Builds products list from the shopping cart items
            products = []
            product_ids = []
            gross_total = 0
            order_items = order_item_formset.save(commit=False)
            for order_item in order_items:
                product = order_item.product
                products.append({
                    'product_id': product.id,
                    'product_name': product.name,
                    'product_price': product.price,
                })
                product_ids.append(product.id)
                gross_total += product.selling_price * int(order_item.quantity_ordered)

            # Processes order
            member = order_form.cleaned_data['member']
            gross_total = format_monetary(gross_total)
            shipping_fees = format_monetary(settings.SHIPPING_DEFAULT_PRICE)
            gross_total += shipping_fees
            result = process_order(
                member, products=products, discount_value=gross_total, discount_code='Manual Order',
                gross_total=gross_total, staff_notes=order_form.cleaned_data['staff_notes'],
                shipping_fees=shipping_fees
            )
            if not result:
                create_alert.delay(
                    "Invalid Data on New Order",
                    "Attention Needed: Investigate invalid data for member %s:" % member,
                )
                messages.error(request, 'Invalid data. Please try again')

            else:

                # Celery task to create shipping order in the background
                order = result['order']

                # Redirects with success message
                messages.success(request, 'Success! The order was successfully approved.')
                return HttpResponseRedirect(reverse('admin:order:details', args=(order.id,)))

    # Template data
    context = {
        'form': order_form,
        'order_item_formset': order_item_formset,
        'cancel_url': reverse('admin:order:list'),
    }

    # Print Template
    return render(request, 'admin/order/add.html', context)


@restrict_internal_ips
@permission_required('order.admin_view_order', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, order_id):
    """
    View order page

    :param: request
    :param: order_id
    :return: String
    """

    # Identifies database record
    order = get_object_or_404(Order, pk=order_id)
    member = order.member

    # Gets all order items
    order_items = OrderItem.objects.select_related(
        'order', 'product'
    ).filter(order=order).order_by('-created_date')

    # Builds tax invoice URL
    order_url_invoice = None
    if member.referral_code:
        order_url_invoice = "%s%s" % (
            settings.BASE_URL_SECURE,
            reverse(
                'order:tax_invoice', args=(
                    urlsafe_base64_encode(str(order.id).encode('ascii')),
                    urlsafe_base64_encode(str(member.id).encode('ascii')),
                    urlsafe_base64_encode(member.referral_code.encode('ascii'))
                )
            )
        )

    # Template data
    context = {
        'order': order,
        'order_url_invoice': order_url_invoice,
        'order_items': order_items,
        'urls': {
            'back': reverse('admin:order:list'),
            'edit': reverse('admin:order:edit', args=(order.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/order/details.html', context)


@restrict_internal_ips
@permission_required('order.admin_change_order', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, order_id):
    """
    Edit Subscription personal data

    :param: request
    :param: order_id
    :return: String
    """
    # Identifies database record
    order = get_object_or_404(Order, pk=order_id)

    # Instantiate FORM
    form = EditOrderForm(request.POST or None, instance=order)

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        order = form.save()

        messages.success(request, 'Order was successfully updated.')
        return HttpResponseRedirect(reverse('admin:order:details', args=(order_id,)))

    # Template data
    context = {
        'form': form,
        'cancel_url': reverse('admin:order:details', args=(order_id,))
    }

    # Print Template
    return render(request, 'admin/order/edit.html', context)


@restrict_internal_ips
@permission_required('order.admin_view_order', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all orders with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    # Starts up GET params
    querystring = ''

    # Builds template data
    template_data = {
        'querystring': querystring,
    }

    # Prints out template
    return render(request, 'admin/order/list.html', template_data)


@restrict_internal_ips
@permission_required('order.admin_view_order', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = Order.objects.select_related(
        'order_status', 'member__user',
    ).annotate(
        full_name=Concat(
            F('member__user__first_name'), Value(' '), F('member__user__last_name'),
            output_field=CharField()
        ),
    ).distinct()

    # settings
    info = {
        'fields_to_select': [
            'id', 'order_status.name', 'full_name',
            'net_total', 'created_date', 'modified_date'
        ],
        'fields_to_search': [
            'id', 'order_status__name', 'member__user__email', 'full_name',
            'net_total', 'created_date', 'discount_code'
        ],
        'default_order_by': 'id',
        'url_base_name': 'order',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

"""
Subscriptions Views

These are the views that control logic flow for
the crud operations.
"""

##########################
# Imports
##########################
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test, permission_required
from wannamigrate.admin.subscription.forms import (
    SubscriptionForm
)
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json
from wannamigrate.admin.login.views import admin_check
from wannamigrate.order.models import OrderItem, Subscription


#######################
# FRUIT VIEWS
#######################
@restrict_internal_ips
@permission_required('subscription.admin_add_subscription', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new Subscription

    :param: request
    :return: String
    """

    return redirect('admin:subscription:list')


@restrict_internal_ips
@permission_required('subscription.admin_delete_subscription', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, subscription_id):
    """
    Delete Subscription action.
    In the case of subscriptions, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: subscription_id
    :return: String
    """
    # Identifies database record
    subscription = get_object_or_404(Subscription, pk=subscription_id)

    # mark as CANCELLED
    subscription.subscription_status_id = settings.DB_ID_SUBSCRIPTION_STATUS_CANCELLED
    subscription.save()

    # Tracks subscription status update
    # track_subscription_status_update.delay(subscription.member)

    # Redirect with success message
    messages.success(request, 'Subscription was successfully marked as DISABLED.')
    return HttpResponseRedirect(reverse('admin:subscription:list'))


@restrict_internal_ips
@permission_required('subscription.admin_view_subscription', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, subscription_id):
    """
    View Subscription page

    :param: request
    :param: subscription_id
    :return: String
    """

    # Identifies database record
    subscription = get_object_or_404(Subscription, pk=subscription_id)

    # Orders
    order_items = OrderItem.objects.select_related(
        'order', 'product',
    ).filter(order__subscription=subscription).order_by('-order__created_date')

    # Template data
    context = {
        'subscription': subscription,
        'order_items': order_items,
        'urls': {
            'back': reverse('admin:subscription:list'),
            'add': reverse('admin:subscription:add'),
            'edit': reverse('admin:subscription:edit', args=(subscription.id,)),
            'delete': reverse('admin:subscription:delete', args=(subscription.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/subscription/details.html', context)


@restrict_internal_ips
@permission_required('subscription.admin_change_subscription', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, subscription_id):
    """
    Edit Subscription personal data

    :param: request
    :param: subscription_id
    :return: String
    """
    # Identifies database record
    subscription = get_object_or_404(Subscription, pk=subscription_id)

    # Instantiate FORM
    form = SubscriptionForm(request.POST or None, instance=subscription)

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        form.save()

        # Tracks subscription status update
        # track_subscription_status_update.delay(subscription.member)

        # Redirects with success message
        messages.success(request, 'Subscription was successfully updated.')
        return HttpResponseRedirect(reverse('admin:subscription:details', args=(subscription_id,)))

    # Template data
    context = {
        'form': form,
        'cancel_url': reverse('admin:subscription:details', args=(subscription_id,))
    }

    # Print Template
    return render(request, 'admin/subscription/edit.html', context)


@restrict_internal_ips
@permission_required('subscription.admin_view_subscription', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all subscriptions with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    querystring = ''

    # If status was passed
    subscription_status_id = request.GET.get('subscription_status_id', False)
    if subscription_status_id:
        querystring = '?subscription_status_id=%s' % subscription_status_id

    context = {
        'querystring': querystring
    }
    return render(request, 'admin/subscription/list.html', context)


@restrict_internal_ips
@permission_required('subscription.admin_view_subscription', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = Subscription.objects.select_related('subscription_status', 'member__user')

    # If subscription status filter was passed
    subscription_status_id = request.GET.get('subscription_status_id', False)
    if subscription_status_id:
        subscription_status_id = subscription_status_id.split(',')
        objects = objects.filter(
            subscription_status_id__in=subscription_status_id
        )

    # settings
    info = {
        'fields_to_select': [
            'id', 'subscription_status.name', 'member.user.first_name', 'member.user.last_name',
            'expiry_date'
        ],
        'fields_to_search': [
            'id', 'subscription_status__name', 'member__user__email', 'member__user__first_name',
            'member__user__last_name', 'expiry_date'
        ],
        'default_order_by': 'id',
        'url_base_name': 'subscription',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

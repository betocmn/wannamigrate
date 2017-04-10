"""
Members Views

These are the views that control logic flow for
the crud operations.
"""

##########################
# Imports
##########################
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import CharField, Value, Q, F, Avg, DecimalField
from django.db.models.functions import Concat
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.db import transaction
from wannamigrate.admin.member.forms import (
    MemberForm, UserForm
)
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json, get_object_or_false
from wannamigrate.member.models import Member
from wannamigrate.admin.login.views import admin_check


#######################
# MEMBER VIEWS
#######################
@restrict_internal_ips
@permission_required('member.admin_add_member', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new member

    :param: request
    :return: String
    """

    # Checks if any field of SHIPPING ADDRESS was given
    shipping_address_fields = [
        'shipping-country', 'shipping-line_1', 'shipping-line_2', 'shipping-city',
        'shipping-state', 'shipping-postcode'
    ]
    shipping_address_form_empty = True
    shipping_post_data = None
    for key in shipping_address_fields:
        field = request.POST.get(key, None)
        if field is not None and field != '':
            shipping_address_form_empty = False
            shipping_post_data = request.POST
            break

    # Checks if any field of BILLING ADDRESS was given
    billing_address_fields = [
        'billing-country', 'billing-line_1', 'billing-line_2', 'billing-city',
        'billing-state', 'billing-postcode'
    ]
    billing_address_form_empty = True
    billing_post_data = None
    for key in billing_address_fields:
        field = request.POST.get(key, None)
        if field is not None and field != '':
            billing_address_form_empty = False
            billing_post_data = request.POST
            break

    # Instantiates FORMs
    user_form = UserForm(request.POST or None)
    member_form = MemberForm(request.POST or None, request.FILES or None)
    shipping_form = ShippingAddressForm(shipping_post_data, prefix="shipping")
    billing_form = BillingAddressForm(billing_post_data, prefix="billing")
    shipping_address = None
    billing_address = None

    # If forms were submitted
    if request.method == 'POST':

        # Starts a DB transaction so that one failure cancels all previous operations
        with transaction.atomic():

            # Saves Shipping Address (Not Required)
            shipping_address_form_errors = False
            if not shipping_address_form_empty:
                if shipping_form.is_valid():
                    shipping_address = shipping_form.save()
                else:
                    shipping_address_form_errors = True

            # Saves Billing Address (not required)
            billing_address_form_errors = False
            if not billing_address_form_empty:
                if billing_form.is_valid():
                    billing_address = billing_form.save()
                else:
                    billing_address_form_errors = True

            # Validates and Saves the User Form
            if not shipping_address_form_errors and not billing_address_form_errors and \
                    user_form.is_valid():

                # Sets additional data
                user_form.is_active = True
                user_form.is_admin = False
                user = user_form.save()

                # Validates and saves Member
                member_form.user = user
                if member_form.is_valid():
                    member = member_form.save()

                    # Saves Addresses
                    if shipping_address or billing_address:
                        member.shipping_address = shipping_address if shipping_address else None
                        member.billing_address = billing_address if billing_address else None
                        member.save()

                    # Sends Welcome Email to User
                    # TODO Change this to a celery/signal background task
                    #Mailer.send_welcome_email(user)

                    # Redirects with success message
                    messages.success(request, 'Member was successfully added.')
                    return HttpResponseRedirect(reverse('admin:member:details', args=(member.id,)))

            # Cancel the whole transaction if it gets here
            transaction.set_rollback(True)

    # Template data
    context = {
        'user_form': user_form, 'member_form': member_form,
        'shipping_form': shipping_form, 'billing_form': billing_form,
        'cancel_url': reverse('admin:member:list')
    }

    # Prints Template
    return render(request, 'admin/member/add.html', context)


@restrict_internal_ips
@permission_required('member.admin_delete_member', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, member_id):
    """
    Delete member action.
    In the case of users, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: member_id
    :return: String
    """
    # Identifies database record
    member = get_object_or_404(Member, pk=member_id)

    # mark as INACTIVE
    user = member.user
    user.is_active = False
    user.save()

    # Redirect with success message
    messages.success(request, 'Member was successfully marked as INACTIVE.')
    return HttpResponseRedirect(reverse('admin:member:list'))


@restrict_internal_ips
@permission_required('member.admin_view_member', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, member_id):
    """
    View member page

    :param: request
    :param: user_id
    :return: String
    """

    # Identifies database record
    member = Member.objects.annotate(
        average_rating=Avg(
            'winerating__score',
            output_field=DecimalField(max_digits=3, decimal_places=2)
        )
    ).filter(id=member_id).first()
    if not member:
        return redirect('admin:member:list')

    # Gifts received
    gifts_given = Gift.objects.filter(from_member_id=member.id)
    gifts_received = Gift.objects.filter(to_member_id=member.id)

    # Orders
    order_items = OrderItem.objects.select_related(
        'order', 'product', 'order_item_source'
    ).filter(order__member=member).order_by('-order__created_date')

    # Wine Ratings
    wine_ratings = WineRating.objects.filter(member=member)

    # Template data
    context = {
        'member': member,
        'wine_ratings': wine_ratings,
        'gifts_given': gifts_given,
        'gifts_received': gifts_received,
        'member_credits': Credit.objects.select_related('credit_reason').filter(member_id=member.id),
        'user': member.user,
        'subscription': get_object_or_false(Subscription, member_id=member.id),
        'order_items': order_items,
        'shipping_address': member.shipping_address,
        'billing_address': member.billing_address,
        'urls': {
            'back': reverse('admin:member:list'),
            'add': reverse('admin:member:add'),
            'edit': reverse('admin:member:edit', args=(member.id,)),
            'delete': reverse('admin:member:delete', args=(member.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/member/details.html', context)


@restrict_internal_ips
@permission_required('member.admin_change_member', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, member_id):
    """
    Edit member personal data

    :param: request
    :param: user_id
    :return: String
    """
    # Identifies database record
    member = get_object_or_404(Member, pk=member_id)
    wine_preference = get_object_or_false(WinePreference, member_id=member_id)

    # Checks if any field of SHIPPING ADDRESS was given
    shipping_address_fields = [
        'shipping-country', 'shipping-line_1', 'shipping-line_2', 'shipping-city',
        'shipping-state', 'shipping-postcode'
    ]
    shipping_address_form_empty = True
    shipping_post_data = None
    for key in shipping_address_fields:
        field = request.POST.get(key, None)
        if field is not None and field != '':
            shipping_address_form_empty = False
            shipping_post_data = request.POST
            break

    # Checks if any field of BILLING ADDRESS was given
    billing_address_fields = [
        'billing-country', 'billing-line_1', 'billing-line_2', 'billing-city',
        'billing-state', 'billing-postcode'
    ]
    billing_address_form_empty = True
    billing_post_data = None
    for key in billing_address_fields:
        field = request.POST.get(key, None)
        if field is not None and field != '':
            billing_address_form_empty = False
            billing_post_data = request.POST
            break

    # Checks if any field of MEMBER WINE PREFERENCES was given
    wine_preferences_fields = ['preferences-red_bottles', 'preferences-white_bottles']
    wine_preferences_form_empty = True
    wine_preferences_post_data = None
    for key in wine_preferences_fields:
        field = request.POST.get(key, None)
        if field is not None and field != '':
            wine_preferences_form_empty = False
            wine_preferences_post_data = request.POST
            break

    # Instantiates FORM
    user_form = UserForm(request.POST or None, instance=member.user)
    member_form = MemberForm(request.POST or None, request.FILES or None, instance=member)
    shipping_form = ShippingAddressForm(
        shipping_post_data, prefix="shipping", instance=member.shipping_address
    )
    billing_form = BillingAddressForm(
        billing_post_data, prefix="billing", instance=member.billing_address
    )
    wine_preferences_form = MemberWinePreferencesForm(
        wine_preferences_post_data, prefix="preferences", instance=wine_preference
    )
    shipping_address = None
    billing_address = None

    # If forms were submitted
    if request.method == 'POST':

        # Starts a DB transaction so that one failure cancels all previous operations
        with transaction.atomic():

            # Saves Wine Preferences (Not Required)
            wine_preferences_form_errors = False
            if not wine_preferences_form_empty:
                if wine_preferences_form.is_valid():

                    # Validate min number of bottles
                    min_total_bottles = settings.SUBSCRIPTION_MINIMUM_TOTAL_BOTTLES
                    red_bottles = wine_preferences_form.cleaned_data.get('red_bottles', False)
                    white_bottles = wine_preferences_form.cleaned_data.get('white_bottles', False)
                    if red_bottles and white_bottles:

                        # Validates input data
                        red_bottles = int(red_bottles)
                        white_bottles = int(white_bottles)
                        total_bottles_selected = (red_bottles + white_bottles)
                        if total_bottles_selected < min_total_bottles:
                            messages.error(request, 'You need a minimum of 3 bottles in total')
                            wine_preferences_form_errors = True
                        elif total_bottles_selected > min_total_bottles and \
                                not member.payment_api_customer_uuid:
                            messages.error(request, 'Member needs to add a payment method '
                                                    'to be charged for the extra bottles')
                            wine_preferences_form_errors = True

                        # Saves preferences
                        if not wine_preferences_form_errors:
                            wine_preferences_form.save()

                            # Updates total bottles on subscription
                            subscription = get_object_or_false(Subscription, member=member)
                            if subscription:
                                subscription.total_bottles = red_bottles + white_bottles
                                subscription.save()

                else:
                    wine_preferences_form_errors = True

            # Saves Shipping Address (Not Required)
            shipping_address_form_errors = False
            if not shipping_address_form_empty:
                if shipping_form.is_valid():
                    shipping_address = shipping_form.save()
                else:
                    shipping_address_form_errors = True

            # Saves Billing Address (not required)
            billing_address_form_errors = False
            if not billing_address_form_empty:
                if billing_form.is_valid():
                    billing_address = billing_form.save()
                else:
                    billing_address_form_errors = True

            # Validates and Saves the User Form
            if not shipping_address_form_errors and not billing_address_form_errors and \
                    not wine_preferences_form_errors and user_form.is_valid():

                # Sets additional data
                user_form.is_active = True
                user_form.is_admin = False
                user = user_form.save()

                # Validates and saves Member
                member_form.user = user
                if member_form.is_valid():
                    member = member_form.save()

                    # Saves Addresses
                    if shipping_address or billing_address:
                        member.shipping_address = shipping_address if shipping_address else None
                        member.billing_address = billing_address if billing_address else None
                        member.save()

                        # Celery task to update order address for pending orders
                        update_pending_order_addresses.delay(member, shipping_address)

                    # Redirects with success message
                    messages.success(request, 'Member was successfully added.')
                    return HttpResponseRedirect(reverse('admin:member:details', args=(member.id,)))

            # Cancel the whole transaction if it gets here
            transaction.set_rollback(True)

    # Template data
    context = {
        'user_form': user_form, 'member_form': member_form,
        'shipping_form': shipping_form, 'billing_form': billing_form,
        'wine_preferences_form': wine_preferences_form,
        'member': member,
        'cancel_url': reverse('admin:member:details', args=(member.id,))
    }

    # Print Template
    return render(request, 'admin/member/edit.html', context)


@restrict_internal_ips
@permission_required('member.admin_view_member', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all members with pagination, order by, search, etc. using www.datatables.net

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
    return render(request, 'admin/member/list.html', context)


@restrict_internal_ips
@permission_required('member.admin_view_member', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = Member.objects.select_related('user', 'subscription').annotate(
        full_name=Concat(
            F('user__first_name'), Value(' '), F('user__last_name'),
            output_field=CharField()
        ),
        subscription_status=F('subscription__subscription_status__name'),
        subscription_month=F('subscription__month_count'),
    )

    # If subscription status filter was passed
    subscription_status_id = request.GET.get('subscription_status_id', False)
    if subscription_status_id:
        objects = objects.filter(
            subscription__subscription_status_id=subscription_status_id
        )

    # settings
    info = {
        'fields_to_select': [
            'id', 'full_name', 'user.email', 'created_date', 'subscription_status',
            'subscription_month'
        ],
        'fields_to_search': [
            'id', 'full_name', 'user__email', 'subscription_status'
        ],
        'default_order_by': '-created_date',
        'url_base_name': 'member',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)


@restrict_internal_ips
@user_passes_test(admin_check)
def search_json(request):
    """
    Generates JSON for the results of a search

    :param: request
    :return: String
    """

    # Query data
    result = {'members': []}
    keyword = request.GET.get('keyword', None)
    if keyword:
        members = Member.objects.select_related('user').annotate(
            full_name=Concat(
                F('user__first_name'), Value(' '), F('user__last_name'),
                output_field=CharField()
            )
        ).filter(
            Q(full_name__icontains=keyword) | Q(user__email__icontains=keyword)
            | Q(id__iexact=keyword)
        )[:10]
        for member in members:
            result['members'].append({
                'id': member.id,
                'description': "%s - %s" % (member.user.get_full_name(), member.user.email),
            })

    return JsonResponse(result, safe=False)

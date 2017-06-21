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
from wannamigrate.order.models import OrderItem, Subscription
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

    # Instantiates FORMs
    user_form = UserForm(request.POST or None)
    member_form = MemberForm(request.POST or None, request.FILES or None)

    # If forms were submitted
    if request.method == 'POST':

        # Starts a DB transaction so that one failure cancels all previous operations
        with transaction.atomic():

            # Validates and Saves the User Form
            if user_form.is_valid():

                # Sets additional data
                user_form.is_active = True
                user_form.is_admin = False
                user = user_form.save()

                # Validates and saves Member
                member_form.user = user
                if member_form.is_valid():
                    member = member_form.save()

                    # Redirects with success message
                    messages.success(request, 'Member was successfully added.')
                    return HttpResponseRedirect(reverse('admin:member:details', args=(member.id,)))

            # Cancel the whole transaction if it gets here
            transaction.set_rollback(True)

    # Template data
    context = {
        'user_form': user_form, 'member_form': member_form,
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
    member = Member.objects.filter(id=member_id).first()
    if not member:
        return redirect('admin:member:list')

    # Orders
    order_items = OrderItem.objects.select_related(
        'order', 'product'
    ).filter(order__member=member).order_by('-order__created_date')

    # Template data
    context = {
        'member': member,
        'user': member.user,
        'subscription': get_object_or_false(Subscription, member_id=member.id),
        'order_items': order_items,
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

    # Instantiates FORM
    user_form = UserForm(request.POST or None, instance=member.user)
    member_form = MemberForm(request.POST or None, request.FILES or None, instance=member)

    # If forms were submitted
    if request.method == 'POST':

        # Starts a DB transaction so that one failure cancels all previous operations
        with transaction.atomic():

            # Validates and Saves the User Form
            if user_form.is_valid():

                # Sets additional data
                user_form.is_active = True
                user_form.is_admin = False
                user = user_form.save()

                # Validates and saves Member
                member_form.user = user
                if member_form.is_valid():
                    member = member_form.save()

                    # Redirects with success message
                    messages.success(request, 'Member was successfully added.')
                    return HttpResponseRedirect(reverse('admin:member:details', args=(member.id,)))

            # Cancel the whole transaction if it gets here
            transaction.set_rollback(True)

    # Template data
    context = {
        'user_form': user_form, 'member_form': member_form,
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

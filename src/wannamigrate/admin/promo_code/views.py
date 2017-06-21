"""
PromoCodes Views

These are the views that control logic flow for
the crud operations.
"""

##########################
# Imports
##########################
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required
from wannamigrate.admin.promo_code.forms import PromoCodeForm
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json
from wannamigrate.order.models import PromoCode
from wannamigrate.admin.login.views import admin_check


#######################
# FRUIT VIEWS
#######################
@restrict_internal_ips
@permission_required('order.admin_add_promo_code', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new PromoCode

    :param: request
    :return: String
    """

    # Instantiate FORM
    form = PromoCodeForm(request.POST or None)

    # If form was submitted, it tries to validate and save data
    if form.is_valid():

        # Saves PromoCode
        promo_code = form.save()
        messages.success(request, 'Promo Code was successfully added.')

        # Redirect with success message
        return HttpResponseRedirect(reverse('admin:promo_code:details', args=(promo_code.id,)))

    # Template data
    context = {'form': form, 'cancel_url': reverse('admin:promo_code:list')}

    # Print Template
    return render(request, 'admin/promo_code/add.html', context)


@restrict_internal_ips
@permission_required('order.admin_delete_promo_code', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, promo_code_id):
    """
    Delete PromoCode action.
    In the case of promo_codes, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: promo_code_id
    :return: String
    """

    # Identifies database record
    promo_code = get_object_or_404(PromoCode, pk=promo_code_id)

    # mark as INACTIVE
    promo_code.is_enabled = False
    promo_code.save()

    # Redirect with success message
    messages.success(request, 'Promo Code was successfully marked as DISABLED.')
    return HttpResponseRedirect(reverse('admin:promo_code:list'))


@restrict_internal_ips
@permission_required('order.admin_view_promo_code', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, promo_code_id):
    """
    View PromoCode page

    :param: request
    :param: promo_code_id
    :return: String
    """

    # Identifies database record
    promo_code = get_object_or_404(PromoCode, pk=promo_code_id)

    # Template data
    context = {
        'promo_code': promo_code,
        'urls': {
            'back': reverse('admin:promo_code:list'),
            'add': reverse('admin:promo_code:add'),
            'edit': reverse('admin:promo_code:edit', args=(promo_code.id,)),
            'delete': reverse('admin:promo_code:delete', args=(promo_code.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/promo_code/details.html', context)


@restrict_internal_ips
@permission_required('order.admin_change_promo_code', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, promo_code_id):
    """
    Edit PromoCode personal data

    :param: request
    :param: promo_code_id
    :return: String
    """
    # Identifies database record
    promo_code = get_object_or_404(PromoCode, pk=promo_code_id)

    # Instantiate FORM
    form = PromoCodeForm(request.POST or None, instance=promo_code)

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        form.save()
        messages.success(request, 'PromoCode was successfully updated.')
        return HttpResponseRedirect(reverse('admin:promo_code:details', args=(promo_code_id,)))

    # Template data
    context = { 'form': form, 'cancel_url': reverse('admin:promo_code:details', args = (promo_code_id,)) }

    # Print Template
    return render(request, 'admin/promo_code/edit.html', context)


@restrict_internal_ips
@permission_required('order.admin_view_promo_code', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all promo_codes with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render(request, 'admin/promo_code/list.html', context)


@restrict_internal_ips
@permission_required('order.admin_view_promo_code', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = PromoCode.objects.all()

    # settings
    info = {
        'fields_to_select': [
            'id', 'name', 'discount_percentage', 'discount_value', 'expiry_date',
            'usage_count', 'usage_limit', 'is_enabled'
        ],
        'fields_to_search': ['id', 'name'],
        'default_order_by': 'id',
        'url_base_name': 'promo_code',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

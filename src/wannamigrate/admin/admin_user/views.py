"""
Admin Users Views

These are the views that control logic flow for
the crud operations.
"""

##########################
# Imports
##########################
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from wannamigrate.admin.admin_user.forms import AdminUserForm
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json
from wannamigrate.admin.login.views import admin_check
from wannamigrate.member.models import Member


#######################
# ADMIN USERS VIEWS
#######################
@restrict_internal_ips
@permission_required('core.admin_add_admin_user', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new Admin USER

    :param: request
    :param: user_id
    :return: String
    """

    # Instantiate FORM
    form = AdminUserForm(request.POST or None)

    # If form was submitted, it tries to validate and save data
    if form.is_valid():

        # Sets additional data
        form.is_active = True
        form.is_admin = True

        # Saves User
        user = form.save()

        # Saves member for this user
        member, created = Member.objects.get_or_create(user_id=user.id)

        # Redirect with success message
        messages.success(request, 'User was successfully added.')
        return HttpResponseRedirect(reverse('admin:admin_user:details', args = (user.id,)))

    # Template data
    context = { 'form': form, 'cancel_url': reverse('admin:admin_user:list') }

    # Print Template
    return render(request, 'admin/admin_user/add.html', context)


@restrict_internal_ips
@permission_required('core.admin_delete_admin_user', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, user_id):
    """
    Delete Admin USER action.
    In the case of users, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: user_id
    :return: String
    """
    # Identifies database record
    user = get_object_or_404(get_user_model(), pk=user_id)

    # mark as INACTIVE
    user.is_active = False
    user.save()

    # Redirect with success message
    messages.success(request, 'User was successfully marked as INACTIVE.')
    return HttpResponseRedirect(reverse('admin:admin_user:list'))


@restrict_internal_ips
@permission_required('core.admin_view_admin_user', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, user_id):
    """
    View Admin USER page

    :param: request
    :param: user_id
    :return: String
    """

    # Identifies database record
    user = get_object_or_404(get_user_model(), pk=user_id, is_admin=True)

    # Template data
    context = {
        'user': user,
        'urls': {
            'back': reverse('admin:admin_user:list'),
            'add': reverse('admin:admin_user:add'),
            'edit': reverse('admin:admin_user:edit', args=(user.id,)),
            'delete': reverse('admin:admin_user:delete', args=(user.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/admin_user/details.html', context)


@restrict_internal_ips
@permission_required('core.admin_change_admin_user', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, user_id):
    """
    Edit Admin USER personal data

    :param: request
    :param: user_id
    :return: String
    """
    # Identifies database record
    user = get_object_or_404(get_user_model(), pk=user_id, is_admin=True)

    # Instantiate FORM
    form = AdminUserForm(request.POST or None, instance=user)

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        user = form.save()

        # Saves member for this user
        member, created = Member.objects.get_or_create(user_id=user.id)

        messages.success(request, 'User was successfully updated.')
        return HttpResponseRedirect(reverse('admin:admin_user:details', args = (user_id,)))

    # Template data
    context = { 'form': form, 'cancel_url': reverse('admin:admin_user:details', args = (user_id,)) }

    # Print Template
    return render(request, 'admin/admin_user/edit.html', context)


@restrict_internal_ips
@permission_required('core.admin_view_admin_user', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all admin users with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render(request, 'admin/admin_user/list.html', context)


@restrict_internal_ips
@permission_required('core.admin_view_admin_user', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = get_user_model().objects.filter(is_admin=True)

    # settings
    info = {
        'fields_to_select': ['id', 'first_name', 'email', 'is_superuser'],
        'fields_to_search': ['id', 'first_name', 'email', 'is_superuser'],
        'default_order_by': 'id',
        'url_base_name': 'admin_user',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

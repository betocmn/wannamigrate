"""
Group Views

These are the views that control logic flow for
the templates on admin
"""

##########################
# Imports
##########################
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.models import Group
from wannamigrate.admin.group.forms import GroupForm
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json
from wannamigrate.admin.login.views import admin_check


#######################
# GROUPS AND PERMISSIONS VIEWS
#######################
@restrict_internal_ips
@permission_required('auth.add_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new Group

    :param: request
    :param: user_id
    :return: String
    """

    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and save data
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request, 'Group was successfully added.')
            return HttpResponseRedirect(reverse('admin:group:details', args = (group.id,)))

    else:
        form = GroupForm()

    # Template data
    context = { 'form': form, 'cancel_url': reverse('admin:group:list') }

    # Print Template
    return render(request, 'admin/group/add.html', context)


@restrict_internal_ips
@permission_required('auth.delete_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, group_id):
    """
    Delete Group action.

    :param: request
    :param: group_id
    :return: String
    """

    # Identifies database record
    group = get_object_or_404(Group, pk=group_id)

    # Deletes it
    group.delete()

    # Redirect with success message
    messages.success(request, 'group was successfully DELETED.')
    return HttpResponseRedirect(reverse('admin:group:list'))


@restrict_internal_ips
@permission_required('auth.view_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, group_id):
    """
    View GROUP page

    :param: request
    :param: group_id
    :return: String
    """

    # Identifies database record
    group = get_object_or_404(Group, pk=group_id)

    # Template data
    context = {'group': group}

    # Print Template
    return render(request, 'admin/group/details.html', context)


@restrict_internal_ips
@permission_required('auth.edit_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, group_id):
    """
    Edit Group data

    :param: request
    :param: group_id
    :return: String
    """

    # Identifies database record
    group = get_object_or_404(Group, pk=group_id)

    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and save data
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, 'Group was successfully updated.')
            return HttpResponseRedirect(reverse('admin:group:details', args = (group_id,)))

    else:
        form = GroupForm(instance=group)

    # Template data
    context = { 'form': form, 'cancel_url': reverse('admin:group:details', args = (group_id,)) }

    # Print Template
    return render(request, 'admin/group/edit.html', context)


@restrict_internal_ips
@permission_required('auth.view_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all admin users with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render(request, 'admin/group/list.html', context)


@restrict_internal_ips
@permission_required('auth.view_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    #group = Group()
    objects = Group.objects.all()

    # settings
    info = {
        'fields_to_select': [ 'id', 'name' ],
        'fields_to_search': [ 'id', 'name' ],
        'default_order_by': 'name',
        'url_base_name': 'group',
        'namespace': 'admin:',
    }

    #build json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

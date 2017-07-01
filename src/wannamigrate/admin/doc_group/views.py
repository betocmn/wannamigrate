"""
DocGroups Views

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
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from wannamigrate.admin.doc_group.forms import DocGroupForm
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json
from wannamigrate.doc.models import DocGroup
from wannamigrate.admin.login.views import admin_check


#######################
# FRUIT VIEWS
#######################
@restrict_internal_ips
@permission_required('doc.admin_add_doc_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new DocGroup

    :param: request
    :return: String
    """

    # Instantiate FORM
    form = DocGroupForm(request.POST or None, request.FILES or None)

    # If form was submitted, it tries to validate and save data
    if form.is_valid():

        # Saves DocGroup
        doc_group = form.save()
        messages.success(request, 'Doc Group was successfully added.')

        # Redirect with success message
        return HttpResponseRedirect(reverse('admin:doc_group:details', args=(doc_group.id,)))

    # Template data
    context = {'form': form, 'cancel_url': reverse('admin:doc_group:list')}

    # Print Template
    return render(request, 'admin/doc_group/add.html', context)


@restrict_internal_ips
@permission_required('doc.admin_delete_doc_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, doc_group_id):
    """
    Delete DocGroup action.
    In the case of doc_groups, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: doc_group_id
    :return: String
    """
    # Identifies database record
    doc_group = get_object_or_404(DocGroup, pk=doc_group_id)

    # mark as INACTIVE
    doc_group.is_enabled = False
    doc_group.save()

    # Redirect with success message
    messages.success(request, 'Doc Group was successfully marked as DISABLED.')
    return HttpResponseRedirect(reverse('admin:doc_group:list'))


@restrict_internal_ips
@permission_required('doc.admin_view_doc_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, doc_group_id):
    """
    View DocGroup page

    :param: request
    :param: doc_group_id
    :return: String
    """

    # Identifies database record
    doc_group = get_object_or_404(DocGroup, pk=doc_group_id)

    # Template data
    context = {
        'doc_group': doc_group,
        'urls': {
            'back': reverse('admin:doc_group:list'),
            'add': reverse('admin:doc_group:add'),
            'edit': reverse('admin:doc_group:edit', args=(doc_group.id,)),
            'delete': reverse('admin:doc_group:delete', args=(doc_group.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/doc_group/details.html', context)


@restrict_internal_ips
@permission_required('doc.admin_change_doc_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, doc_group_id):
    """
    Edit DocGroup personal data

    :param: request
    :param: doc_group_id
    :return: String
    """
    # Identifies database record
    doc_group = get_object_or_404(DocGroup, pk=doc_group_id)

    # Instantiate FORM
    form = DocGroupForm(request.POST or None, request.FILES or None, instance=doc_group)

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        form.save()
        messages.success(request, 'Doc Group was successfully updated.')
        return HttpResponseRedirect(reverse('admin:doc_group:details', args=(doc_group_id,)))

    # Template data
    context = { 'form': form, 'cancel_url': reverse('admin:doc_group:details', args = (doc_group_id,)) }

    # Print Template
    return render(request, 'admin/doc_group/edit.html', context)


@restrict_internal_ips
@permission_required('doc.admin_view_doc_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all promo_codes with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render(request, 'admin/doc_group/list.html', context)


@restrict_internal_ips
@permission_required('doc.admin_view_doc_group', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = DocGroup.objects.select_related('country').order_by('country__name', 'sort_order')

    # settings
    info = {
        'fields_to_select': ['id', 'country.name', 'name', 'sort_order', 'is_enabled'],
        'fields_to_search': ['id', 'name', 'country__name'],
        'default_order_by': 'name',
        'url_base_name': 'doc_group',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

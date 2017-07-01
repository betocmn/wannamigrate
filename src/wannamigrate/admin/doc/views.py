"""
Docs Views

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
from wannamigrate.admin.doc.forms import DocForm
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json
from wannamigrate.doc.models import Doc
from wannamigrate.admin.login.views import admin_check


#######################
# FRUIT VIEWS
#######################
@restrict_internal_ips
@permission_required('doc.admin_add_doc', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new Doc

    :param: request
    :return: String
    """

    # Instantiate FORM
    form = DocForm(request.POST or None, request.FILES or None)

    # If form was submitted, it tries to validate and save data
    if form.is_valid():

        # Saves Doc
        doc = form.save()
        messages.success(request, 'Doc was successfully added.')

        # Redirect with success message
        return HttpResponseRedirect(reverse('admin:doc:details', args=(doc.id,)))

    # Template data
    context = {'form': form, 'cancel_url': reverse('admin:doc:list')}

    # Print Template
    return render(request, 'admin/doc/add.html', context)


@restrict_internal_ips
@permission_required('doc.admin_delete_doc', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, doc_id):
    """
    Delete Doc action.
    In the case of docs, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: doc_id
    :return: String
    """
    # Identifies database record
    doc = get_object_or_404(Doc, pk=doc_id)

    # mark as INACTIVE
    doc.is_enabled = False
    doc.save()

    # Redirect with success message
    messages.success(request, 'Doc was successfully marked as DISABLED.')
    return HttpResponseRedirect(reverse('admin:doc:list'))


@restrict_internal_ips
@permission_required('doc.admin_view_doc', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, doc_id):
    """
    View Doc page

    :param: request
    :param: doc_id
    :return: String
    """

    # Identifies database record
    doc = get_object_or_404(Doc, pk=doc_id)

    # Template data
    context = {
        'doc': doc,
        'urls': {
            'back': reverse('admin:doc:list'),
            'add': reverse('admin:doc:add'),
            'edit': reverse('admin:doc:edit', args=(doc.id,)),
            'delete': reverse('admin:doc:delete', args=(doc.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/doc/details.html', context)


@restrict_internal_ips
@permission_required('doc.admin_change_doc', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, doc_id):
    """
    Edit Doc personal data

    :param: request
    :param: doc_id
    :return: String
    """
    # Identifies database record
    doc = get_object_or_404(Doc, pk=doc_id)

    # Instantiate FORM
    form = DocForm(request.POST or None, request.FILES or None, instance=doc)

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        form.save()
        messages.success(request, 'Doc was successfully updated.')
        return HttpResponseRedirect(reverse('admin:doc:details', args=(doc_id,)))

    # Template data
    context = { 'form': form, 'cancel_url': reverse('admin:doc:details', args = (doc_id,)) }

    # Print Template
    return render(request, 'admin/doc/edit.html', context)


@restrict_internal_ips
@permission_required('doc.admin_view_doc', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all promo_codes with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render(request, 'admin/doc/list.html', context)


@restrict_internal_ips
@permission_required('doc.admin_view_doc', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = Doc.objects.select_related(
        'doc_group', 'doc_group__country'
    ).order_by('doc_group__country__name', 'doc_group__sort_order', 'sort_order')

    # settings
    info = {
        'fields_to_select': ['id', 'doc_group.country.name', 'doc_group.name', 'name', 'sort_order',
                             'is_enabled'],
        'fields_to_search': ['id', 'name', 'doc_group__country__name', 'doc_group__name'],
        'default_order_by': 'name',
        'url_base_name': 'doc',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

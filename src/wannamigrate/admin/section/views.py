"""
Sections Views

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
from wannamigrate.admin.section.forms import SectionForm
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json
from wannamigrate.guide.models import Section
from wannamigrate.admin.login.views import admin_check


#######################
# FRUIT VIEWS
#######################
@restrict_internal_ips
@permission_required('guide.admin_add_section', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new Section

    :param: request
    :return: String
    """

    # Instantiate FORM
    form = SectionForm(request.POST or None, request.FILES or None)

    # If form was submitted, it tries to validate and save data
    if form.is_valid():

        # Saves Section
        section = form.save()
        messages.success(request, 'Section was successfully added.')

        # Redirect with success message
        return HttpResponseRedirect(reverse('admin:section:details', args=(section.id,)))

    # Template data
    context = {'form': form, 'cancel_url': reverse('admin:section:list')}

    # Print Template
    return render(request, 'admin/section/add.html', context)


@restrict_internal_ips
@permission_required('guide.admin_delete_section', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, section_id):
    """
    Delete Section action.
    In the case of sections, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: section_id
    :return: String
    """
    # Identifies database record
    section = get_object_or_404(Section, pk=section_id)

    # mark as INACTIVE
    section.is_enabled = False
    section.save()

    # Redirect with success message
    messages.success(request, 'Section was successfully marked as DISABLED.')
    return HttpResponseRedirect(reverse('admin:section:list'))


@restrict_internal_ips
@permission_required('guide.admin_view_section', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, section_id):
    """
    View Section page

    :param: request
    :param: section_id
    :return: String
    """

    # Identifies database record
    section = get_object_or_404(Section, pk=section_id)

    # Template data
    context = {
        'section': section,
        'urls': {
            'back': reverse('admin:section:list'),
            'add': reverse('admin:section:add'),
            'edit': reverse('admin:section:edit', args=(section.id,)),
            'delete': reverse('admin:section:delete', args=(section.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/section/details.html', context)


@restrict_internal_ips
@permission_required('guide.admin_change_section', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, section_id):
    """
    Edit Section personal data

    :param: request
    :param: section_id
    :return: String
    """
    # Identifies database record
    section = get_object_or_404(Section, pk=section_id)

    # Instantiate FORM
    form = SectionForm(request.POST or None, request.FILES or None, instance=section)

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        form.save()
        messages.success(request, 'Section was successfully updated.')
        return HttpResponseRedirect(reverse('admin:section:details', args=(section_id,)))

    # Template data
    context = { 'form': form, 'cancel_url': reverse('admin:section:details', args = (section_id,)) }

    # Print Template
    return render(request, 'admin/section/edit.html', context)


@restrict_internal_ips
@permission_required('guide.admin_view_section', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all promo_codes with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render(request, 'admin/section/list.html', context)


@restrict_internal_ips
@permission_required('guide.admin_view_section', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = Section.objects.select_related(
        'chapter', 'chapter__country'
    ).order_by('chapter__country__name', 'chapter__sort_order', 'sort_order')

    # settings
    info = {
        'fields_to_select': ['id', 'chapter.country.name', 'chapter.title', 'title', 'sort_order',
                             'is_enabled'],
        'fields_to_search': ['id', 'title', 'chapter__country__name', 'chapter__title'],
        'default_order_by': 'name',
        'url_base_name': 'section',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

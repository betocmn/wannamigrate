"""
Chapters Views

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
from wannamigrate.admin.chapter.forms import ChapterForm
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json
from wannamigrate.guide.models import Chapter
from wannamigrate.admin.login.views import admin_check


#######################
# FRUIT VIEWS
#######################
@restrict_internal_ips
@permission_required('guide.admin_add_chapter', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new Chapter

    :param: request
    :return: String
    """

    # Instantiate FORM
    form = ChapterForm(request.POST or None, request.FILES or None)

    # If form was submitted, it tries to validate and save data
    if form.is_valid():

        # Saves Chapter
        chapter = form.save()
        messages.success(request, 'Chapter was successfully added.')

        # Redirect with success message
        return HttpResponseRedirect(reverse('admin:chapter:details', args=(chapter.id,)))

    # Template data
    context = {'form': form, 'cancel_url': reverse('admin:chapter:list')}

    # Print Template
    return render(request, 'admin/chapter/add.html', context)


@restrict_internal_ips
@permission_required('guide.admin_delete_chapter', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, chapter_id):
    """
    Delete Chapter action.
    In the case of chapters, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: chapter_id
    :return: String
    """
    # Identifies database record
    chapter = get_object_or_404(Chapter, pk=chapter_id)

    # mark as INACTIVE
    chapter.is_enabled = False
    chapter.save()

    # Redirect with success message
    messages.success(request, 'Chapter was successfully marked as DISABLED.')
    return HttpResponseRedirect(reverse('admin:chapter:list'))


@restrict_internal_ips
@permission_required('guide.admin_view_chapter', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, chapter_id):
    """
    View Chapter page

    :param: request
    :param: chapter_id
    :return: String
    """

    # Identifies database record
    chapter = get_object_or_404(Chapter, pk=chapter_id)

    # Template data
    context = {
        'chapter': chapter,
        'urls': {
            'back': reverse('admin:chapter:list'),
            'add': reverse('admin:chapter:add'),
            'edit': reverse('admin:chapter:edit', args=(chapter.id,)),
            'delete': reverse('admin:chapter:delete', args=(chapter.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/chapter/details.html', context)


@restrict_internal_ips
@permission_required('guide.admin_change_chapter', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, chapter_id):
    """
    Edit Chapter personal data

    :param: request
    :param: chapter_id
    :return: String
    """
    # Identifies database record
    chapter = get_object_or_404(Chapter, pk=chapter_id)

    # Instantiate FORM
    form = ChapterForm(request.POST or None, request.FILES or None, instance=chapter)

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        form.save()
        messages.success(request, 'Chapter was successfully updated.')
        return HttpResponseRedirect(reverse('admin:chapter:details', args=(chapter_id,)))

    # Template data
    context = { 'form': form, 'cancel_url': reverse('admin:chapter:details', args = (chapter_id,)) }

    # Print Template
    return render(request, 'admin/chapter/edit.html', context)


@restrict_internal_ips
@permission_required('guide.admin_view_chapter', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all promo_codes with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render(request, 'admin/chapter/list.html', context)


@restrict_internal_ips
@permission_required('guide.admin_view_chapter', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = Chapter.objects.select_related('country').order_by('country__name', 'sort_order')

    # settings
    info = {
        'fields_to_select': ['id', 'country.name', 'title', 'sort_order', 'is_enabled'],
        'fields_to_search': ['id', 'title', 'country__name'],
        'default_order_by': 'name',
        'url_base_name': 'chapter',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

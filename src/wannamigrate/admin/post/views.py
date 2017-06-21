"""
Posts Views

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
from wannamigrate.admin.post.forms import PostForm
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json
from wannamigrate.story.models import Post
from wannamigrate.admin.login.views import admin_check


#######################
# FRUIT VIEWS
#######################
@restrict_internal_ips
@permission_required('story.admin_add_post', login_url='admin:restricted')
@user_passes_test(admin_check)
def add(request):
    """
    Add new Post

    :param: request
    :return: String
    """

    # Instantiate FORM
    form = PostForm(request.POST or None, request.FILES or None)

    # If form was submitted, it tries to validate and save data
    if form.is_valid():

        # Saves Post
        post = form.save()
        messages.success(request, 'Post was successfully added.')

        # Redirect with success message
        return HttpResponseRedirect(reverse('admin:post:details', args=(post.id,)))

    # Template data
    context = {'form': form, 'cancel_url': reverse('admin:post:list')}

    # Print Template
    return render(request, 'admin/post/add.html', context)


@restrict_internal_ips
@permission_required('story.admin_delete_post', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, post_id):
    """
    Delete Post action.
    In the case of posts, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: post_id
    :return: String
    """
    # Identifies database record
    post = get_object_or_404(Post, pk=post_id)

    # mark as INACTIVE
    post.is_enabled = False
    post.save()

    # Redirect with success message
    messages.success(request, 'Post was successfully marked as DISABLED.')
    return HttpResponseRedirect(reverse('admin:post:list'))


@restrict_internal_ips
@permission_required('story.admin_view_post', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, post_id):
    """
    View Post page

    :param: request
    :param: post_id
    :return: String
    """

    # Identifies database record
    post = get_object_or_404(Post, pk=post_id)

    # Template data
    context = {
        'post': post,
        'urls': {
            'back': reverse('admin:post:list'),
            'add': reverse('admin:post:add'),
            'edit': reverse('admin:post:edit', args=(post.id,)),
            'delete': reverse('admin:post:delete', args=(post.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/post/details.html', context)


@restrict_internal_ips
@permission_required('story.admin_change_post', login_url='admin:restricted')
@user_passes_test(admin_check)
def edit(request, post_id):
    """
    Edit Post personal data

    :param: request
    :param: post_id
    :return: String
    """
    # Identifies database record
    post = get_object_or_404(Post, pk=post_id)

    # Instantiate FORM
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        form.save()
        messages.success(request, 'Post was successfully updated.')
        return HttpResponseRedirect(reverse('admin:post:details', args=(post_id,)))

    # Template data
    context = { 'form': form, 'cancel_url': reverse('admin:post:details', args = (post_id,)) }

    # Print Template
    return render(request, 'admin/post/edit.html', context)


@restrict_internal_ips
@permission_required('story.admin_view_post', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all promo_codes with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render(request, 'admin/post/list.html', context)


@restrict_internal_ips
@permission_required('story.admin_view_post', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = Post.objects.order_by('name')

    # settings
    info = {
        'fields_to_select': ['id', 'title', 'created_date', 'is_enabled'],
        'fields_to_search': ['id', 'title', 'html_content'],
        'default_order_by': 'name',
        'url_base_name': 'post',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

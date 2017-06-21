"""
Landing Views

These are the views that control logic flow for
the templates on landing pages
"""

##########################
# Imports
##########################
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from wannamigrate.core.decorators import subscription_required
from wannamigrate.core.util import (
    get_object_or_false, date_to_string, date_from_string
)
from wannamigrate.member.models import Member
from wannamigrate.story.models import Post


#######################
# VIEW METHODS
#######################
@login_required
@subscription_required
def index(request):
    """
    How it works

    :param request:
    :return: String
    """

    # Retrieves latest stories
    posts = Post.objects.filter(
        is_enabled=True,
        country_id=request.session['country_id']
    ).order_by('-created_date')

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'posts': posts,
        'dashboard_section': 'story',
        'meta_title': _('Immi Stories | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'story/index.html', template_data)


@login_required
@subscription_required
def details(request, slug):
    """
    How it works

    :param request:
    :param slug:
    :return: String
    """

    # Retrieves post
    post = get_object_or_false(Post, slug=slug)
    if not post:
        return redirect('story:index')

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'post': post,
        'dashboard_section': 'story',
        'meta_title': _('%s | Wanna Migrate' % post.title),
    }

    # Displays HTML template
    return render(request, 'story/details.html', template_data)

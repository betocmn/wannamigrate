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
def index(request, country_slug):
    """
    How it works

    :param request:
    :param country_slug:
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


def details(request, country_slug, story_slug):
    """
    How it works

    :param request:
    :param country_slug:
    :param story_slug:
    :return: String
    """

    # Retrieves post
    post = get_object_or_false(Post, slug=story_slug)
    if not post:
        return redirect('story:index', country_slug)

    # Insert images on content text
    image_1 = ''
    image_2 = ''
    img = '<div class="image main"><img src="{0}" alt="{1}" /><div class="legend">{1}</div></div>'
    if post.image_1:
        image_1 = img.format(post.image_1.large.url, post.image_description_1)
    if post.image_2:
        image_2 = img.format(post.image_2.large.url, post.image_description_2)
    story_html_content = post.html_content.format(
        image_1=image_1, image_2=image_2
    )

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'post': post,
        'story_html_content': story_html_content,
        'dashboard_section': 'story',
        'meta_title': _('%s | Wanna Migrate' % post.title),
    }

    # Displays HTML template
    return render(request, 'story/details.html', template_data)

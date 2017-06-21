"""
Product Views - Wines, gifts, etc...

These are the views that control logic flow for
the html templates
"""

##########################
# Imports
##########################
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.decorators import subscription_required
from wannamigrate.guide.models import Chapter, Section
from wannamigrate.core.util import get_object_or_false


#######################
# View Methods
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
    chapters = Chapter.objects.filter(
        is_enabled=True,
        country_id=request.session['country_id']
    ).order_by('sort_order')

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'chapters': chapters,
        'dashboard_section': 'guide',
        'meta_title': _('Guide | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'guide/index.html', template_data)


@login_required
@subscription_required
def chapter_details(request, slug):
    """
    How it works

    :param request:
    :param slug:
    :return: String
    """

    # Retrieves chapter
    chapter = get_object_or_false(Chapter, slug=slug)
    if not chapter:
        return redirect('guide:index')

    # Retrieves sections
    sections = Section.objects.filter(chapter=chapter).order_by('sort_order')

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'chapter': chapter,
        'sections': sections,
        'dashboard_section': 'guide',
        'meta_title': _('%s | Wanna Migrate' % chapter.title),
    }

    # Displays HTML template
    return render(request, 'guide/chapter_details.html', template_data)

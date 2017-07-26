"""
Product Views - Wines, gifts, etc...

These are the views that control logic flow for
the html templates
"""

##########################
# Imports
##########################
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from wannamigrate.guide.models import Chapter, Section
from wannamigrate.core.util import get_object_or_false


#######################
# View Methods
#######################
def index(request, country_slug):
    """
    How it works

    :param request:
    :param country_slug:
    :return: String
    """

    # Retrieves all sections by chapter
    sections = Section.objects.select_related('chapter').filter(
        is_enabled=True, chapter__is_enabled=True,
        chapter__country_id=request.session['country_id']
    ).order_by('chapter__sort_order', 'sort_order')

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'sections': sections,
        'dashboard_section': 'guide',
        'meta_title': _('Guide | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'guide/index.html', template_data)


def chapter_details(request, country_slug, chapter_slug):
    """
    How it works

    :param request:
    :param country_slug:
    :param chapter_slug:
    :return: String
    """

    # Retrieves chapter
    chapter = get_object_or_false(Chapter, slug=chapter_slug)
    if not chapter:
        return redirect('guide:index')

    # If restricted for premium subscribers
    if not chapter.is_free and 'subscription_id' not in request.session:
        messages.error(request, 'Sorry, this is only available for premium members.')
        return redirect('company:pricing')

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

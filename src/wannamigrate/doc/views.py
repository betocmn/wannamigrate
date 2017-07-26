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
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from wannamigrate.doc.models import Doc
from wannamigrate.core.util import get_object_or_false


#######################
# View Methods
#######################
@login_required
def index(request, country_slug):
    """
    How it works

    :param request:
    :param country_slug:
    :return: String
    """

    # Retrieves all documents by document group
    docs = Doc.objects.select_related('doc_group').filter(
        is_enabled=True, doc_group__is_enabled=True,
        doc_group__country_id=request.session['country_id']
    ).order_by('doc_group__sort_order', 'sort_order')

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'docs': docs,
        'dashboard_section': 'doc',
        'meta_title': _('Docs | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'doc/index.html', template_data)


@login_required
def download(request, country_slug, doc_id):
    """
    Downloads a doc file

    :param request:
    :param country_slug:
    :param doc_id:
    :return: String
    """

    # Retrieves chapter
    doc = get_object_or_false(Doc, id=doc_id)
    if not doc:
        return redirect('doc:index')

    # If restricted for premium subscribers
    if not doc.is_free and 'subscription_id' not in request.session:
        messages.error(request, 'Sorry, this is only available for premium members.')
        return redirect('company:pricing')

    # Redirects to file download
    return redirect(doc.file.url)

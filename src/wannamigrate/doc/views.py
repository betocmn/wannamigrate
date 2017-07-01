"""
Product Views - Wines, gifts, etc...

These are the views that control logic flow for
the html templates
"""

##########################
# Imports
##########################
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.decorators import subscription_required
from wannamigrate.doc.models import Doc


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

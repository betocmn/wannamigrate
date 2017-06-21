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

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'dashboard_section': 'doc',
        'meta_title': _('Docs | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'doc/index.html', template_data)

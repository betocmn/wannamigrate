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
def index(request, country_slug):
    """
    How it works

    :param request:
    :param country_slug:
    :return: String
    """

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'dashboard_section': 'task',
        'meta_title': _('Tasks | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'task/index.html', template_data)

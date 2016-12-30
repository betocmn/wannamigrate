"""
Landing Views

These are the views that control logic flow for
the templates on landing pages
"""

##########################
# Imports
##########################
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import translation
from django.utils.translation import ugettext_lazy as _


#######################
# HOME-PAGE VIEWS
#######################
@login_required
def checkout(request):
    """
    Checkout

    :param request:
    :return: String
    """

    # Builds template data dictionary
    template_data = {
        'meta_title': _('Checkout | Wanna Migrate'),
        'tracking_event_proceeded_to_payment': settings.TRACKING_EVENT_PROCEEDED_TO_PAYMENT,
    }

    # Displays HTML template
    return render(request, 'order/checkout.html', template_data)

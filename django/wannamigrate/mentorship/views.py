"""
Marketplace Views

These are the views that control logic flow for
the templates on the marketplace app
"""

##########################
# Imports
##########################
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from wannamigrate.core.util import get_object_or_false
from wannamigrate.mentorship.models import (
    Applicant
)
from wannamigrate.core.models import UserStats
from wannamigrate.core.mailer import Mailer
from wannamigrate.site.views import get_situation_form
from wannamigrate.marketplace.payment_processor import PaymentProcessor
from wannamigrate.marketplace.tasks import (
    send_order_confirmation_user, send_order_confirmation_provider
)
from wannamigrate.core.decorators import subscription_required
from django.conf import settings
from django.db.models import F
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.utils import translation
import datetime
from datetime import timedelta
from django.utils import timezone





#######################
# LANDING-PAGE
#######################
def landing( request ):
    """
    Listing of professionals

    :param: request
    :return: String - The html page rendered
    """

    # Initializes template data dictionary
    template_data = {}

    # Prints Template
    return render( request, 'mentorship/landing/landing.html', template_data )




#######################
# APPLY
#######################
def apply( request ):
    """
    Listing of professionals

    :param: request
    :return: String - The html page rendered
    """

    # Initializes template data dictionary
    template_data = {}

    # Prints Template
    return render( request, 'mentorship/landing/landing.html', template_data )




#######################
# PROGRAM (ABOUT)
#######################
def about( request ):
    """
    Listing of professionals

    :param: request
    :return: String - The html page rendered
    """

    # Initializes template data dictionary
    template_data = {}

    # Prints Template
    return render( request, 'mentorship/about/about.html', template_data )





#######################
# FAQ
#######################
def faq( request ):
    """
    Listing of professionals

    :param: request
    :return: String - The html page rendered
    """

    # Initializes template data dictionary
    template_data = {}

    # Prints Template
    return render( request, 'mentorship/faw/faq.html', template_data )



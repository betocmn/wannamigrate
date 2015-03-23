"""
Marketplace Views

These are the views that control logic flow for
the templates on the marketplace app
"""

##########################
# Imports
##########################
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.utils.translation import ugettext as _
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.conf import settings
import math
from wannamigrate.core.util import (
    get_object_or_false, get_dashboard_country_progress_css_class, get_dashboard_user_progress_css_class
)
from wannamigrate.site.forms import (
    ContactForm, LoginForm, SignupForm, PasswordRecoveryForm, PasswordResetForm,
    EditAccountInfoForm, EditAccountPasswordForm, SituationForm
)
from wannamigrate.core.models import (
    Country, UserSituation, Goal, Situation
)
from wannamigrate.marketplace.models import (
    Provider
)
from wannamigrate.core.mailer import Mailer
from wannamigrate.site.views import get_situation_form
from django.utils import translation





#######################
# VIEWS PROFESSIONAL
#######################
@login_required
def view_professional( request, user_id, name ):
    """
    View detais of a professional

    :param: request
    :return: String - The html page rendered
    """

    # Identify database record
    provider = get_object_or_404( Provider, user_id = user_id )

    # Initializes template data dictionary
    template_data = {}

    # passes form to template
    template_data['form'] = get_situation_form( request )

    # passes service provider to template
    template_data['provider'] = provider

    # Prints Template
    return render( request, 'marketplace/professionals/view.html', template_data )

    """
    # Print SQL Queries
    from django.db import connection
    queries_text = ''
    for query in connection.queries:
        queries_text += '<br /><br /><br />' + str( query['sql'] )
    return HttpResponse( queries_text )
    """





#######################
# LISTS PROFESSIONALS
#######################
@login_required
def list_professionals( request ):
    """
    Listing of professionals

    :param: request
    :return: String - The html page rendered
    """

    # Initial template
    template_data = {}

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # If situation is defined, we load professionals related to it
    if 'situation' in request.session and 'from_country' in request.session['situation']:

        from_country = request.session['situation']['from_country']
        to_country = request.session['situation']['to_country']
        goal = request.session['situation']['goal']

        # Gets 5 most related service providers
        template_data['providers'] = Provider.get_listing( to_country.id, 0, 5 )

    # Print Template
    return render( request, 'marketplace/professionals/list.html', template_data )






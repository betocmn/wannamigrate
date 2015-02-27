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
from django.utils import translation
from django.contrib.gis.geoip import GeoIP





#######################
# VIEW PROFESSIONAL
#######################

def view_professional( request, user_id, name ):
    """
    View detais of a professional

    :param: request
    :return: String - The html page rendered
    """

    return HttpResponse( 'View Professional Details :)' + user_id + ' - ' + name )
    # Initializes template data dictionary
    template_data = {}

    # passes form to template
    template_data['form'] = get_situation_form( request )

    # Prints Template
    return render( request, 'site/home/home.html', template_data )






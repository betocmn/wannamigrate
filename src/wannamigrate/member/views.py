"""
Product Views - Wines, gifts, etc...

These are the views that control logic flow for
the html templates
"""

##########################
# Imports
##########################
import requests
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse, Http404
from django.core.files.base import ContentFile
from django.contrib.auth import (
    login as auth_login, authenticate, logout as auth_logout,
    get_user_model
)
from django.db.models.aggregates import Sum
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from wannamigrate.core.util import (
    get_object_or_false, date_next_from_day, date_to_string, date_first_day_of_month,
    date_from_params, date_now, date_from_string
)
from wannamigrate.member.forms import (
    LoginForm, SignupForm, PasswordRecoveryForm, PasswordResetForm
)
from wannamigrate.member.models import Member, PaymentMethod
from wannamigrate.order.models import OrderItem, Order


#######################
# Member General Methods
#######################
def signup(request):
    """
    Home sweet home

    :param request:
    :return: String
    """

    context = {'user': request.user}
    return render(request, 'member/signup.html', context)

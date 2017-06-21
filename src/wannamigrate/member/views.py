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
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.contrib.auth import (
    login as auth_login, authenticate, logout as auth_logout,
    get_user_model
)
from django.utils.translation import ugettext_lazy as _
from django.db import transaction
from wannamigrate.core.util import (
    get_object_or_false, date_to_string, date_from_string
)
from wannamigrate.member.forms import (
    LoginForm, SignupForm
)
from wannamigrate.core.models import Country
from wannamigrate.member.models import Member
from wannamigrate.order.models import Subscription


#######################
# Member General Methods
#######################
def login(request):
    """
    Login Form

    :param request:
    :return: String
    """

    # Defines the next page to redirect
    redirect_next = reverse('member:dashboard')
    if 'next' in request.GET:
        redirect_next = request.GET.get('next', redirect_next)
    elif 'next' in request.POST:
        redirect_next = request.POST.get('next', redirect_next)

    # Checks if user is already logged and full-registered
    if request.user.is_authenticated:
        return redirect(redirect_next)

    # Instantiates forms
    form = LoginForm(request.POST or None)

    # if LOGIN FORM was submitted and is valid
    if form.is_valid():

        # Authenticates user
        user = authenticate(
            email=form.cleaned_data['email'].lower(),
            password=form.cleaned_data['password']
        )
        if user is not None and user.is_active:

            # Logs user in
            auth_login(request, user)

            # Identifies member
            member = get_object_or_false(Member, user_id=user.id)

            # Redirects to next page
            return redirect(redirect_next)

        else:
            messages.error(request, _('Invalid login. Please try again.'))

    # Builds template data dictionary
    template_data = {
        'meta_title': _('Log in | Wanna Migrate'),
        'form': form,
        'facebook_app_id': settings.FACEBOOK_APP_ID,
        'next': redirect_next,
    }

    # Displays HTML template
    return render(request, 'member/login.html', template_data)


def login_facebook(request):
    """
    Receives facebook user id and access token, validates it and logs user in

    :param: request
    :return: String
    """

    # Initial settings
    is_signup = False

    # Receives facebook parameters
    facebook_user_id = request.POST.get('facebook_user_id', False)
    facebook_access_token = request.POST.get('facebook_access_token', False)
    if facebook_user_id and facebook_access_token:

        # Gets Facebook data from Graph API
        basic_request = requests.get(
            'https://graph.facebook.com/me?fields=email,first_name,last_name,gender,birthday'
            '&access_token=%s' % facebook_access_token
        )
        facebook_basic_data = basic_request.json()
        if 'email' in facebook_basic_data:

            # Tries go get facebook profile photo
            photo = None
            picture_request = requests.get(
                'https://graph.facebook.com/%s/picture?width=600'
                '&access_token=%s' % (facebook_basic_data['id'], facebook_access_token),
                stream=True
            )
            if picture_request.status_code == 200:
                picture_request.raw.decode_content = True
                photo = ContentFile(picture_request.raw.read())

            with transaction.atomic():

                # Tries to identify current user in our database
                user = get_object_or_false(get_user_model(), facebook_id=facebook_user_id)
                if not user:
                    user = get_object_or_false(get_user_model(), email=facebook_basic_data['email'])

                # If we need to create a new user
                if not user:
                    is_signup = True
                    user = get_user_model().objects.create_user(
                        facebook_basic_data['email'],
                        first_name=facebook_basic_data['first_name'],
                        last_name=facebook_basic_data['last_name'],
                        facebook_id=facebook_basic_data['id']
                    )

                # Identifies member
                member = get_object_or_false(Member, user=user)
                if not member:
                    member = Member()
                    member.user = user

                # Saves member information
                if 'gender' in facebook_basic_data:
                    member.gender = facebook_basic_data['gender'][0:1].upper().strip()
                if 'birthday' in facebook_basic_data and len(facebook_basic_data['birthday']) == 10:
                    member.birth_date = date_to_string(date_from_string(
                        facebook_basic_data['birthday'], '%m/%d/%Y'
                    ), '%Y-%m-%d')
                member.save()

                # Saves member photo
                if photo:
                    member.avatar.save('temp.jpg', photo)

                # Update user settings
                user.has_updated_password = True
                user.facebook_id = facebook_basic_data['id']
                user.save()

                # Logs user in
                auth_user = authenticate(email=user.email, id=user.id, password_hash=user.password)
                auth_login(request, auth_user)

                # Return JSON success data
                return JsonResponse({'status': 'success', 'message': _('user logged in')})

    return JsonResponse({'status': 'error', 'message': _('facebook graph API request failed')})


def logout(request):
    """
    Process Logout

    :param: request
    :return: HTTP Redirection
    """

    # Executes auth Logout
    if request.user.is_authenticated:
        auth_logout(request)

    # Redirects to home-page
    return redirect('%s?logout=1' % reverse("landing:home"))


def signup(request):
    """
    Sign-Up Form

    :param request:
    :return: String
    """

    # Defines the next page to redirect
    redirect_next = reverse('order:checkout')
    if 'next' in request.GET:
        redirect_next = request.GET.get('next', redirect_next)
    elif 'next' in request.POST:
        redirect_next = request.POST.get('next', redirect_next)

    # Checks if user is already logged and full-registered
    if request.user.is_authenticated and request.user.has_updated_password:
        return redirect(redirect_next)

    # If it's a user logged in with just email, pre-load it on the form
    email = request.user.email if request.user.is_authenticated() else None
    initial_data = None if request.POST else {'email': email}

    # Instantiates forms
    form = SignupForm(request.POST or None, initial=initial_data)

    # if SIGNUP FORM was submitted and is valid
    if form.is_valid():

        # Saves user
        member = form.save()
        if member is not None:

            # Logs user in
            user = authenticate(
                email=form.cleaned_data['email'].lower(),
                password=form.cleaned_data['password']
            )
            auth_login(request, user)

            # Redirects to next page
            return redirect(redirect_next)

    # Builds template data dictionary
    template_data = {
        'meta_title': _('Sign-Up | Wanna Migrate'),
        'form': form,
        'facebook_app_id': settings.FACEBOOK_APP_ID,
        'next': redirect_next,
    }

    # Displays HTML template
    return render(request, 'member/signup.html', template_data)


@login_required
def dashboard(request):
    """
    How it works

    :param request:
    :return: String
    """

    # Sets Australia as the default country
    country = get_object_or_false(Country, id=settings.DB_ID_COUNTRY_AUSTRALIA)
    request.session['country_id'] = country.id
    request.session['country_name'] = country.name
    request.session['country_slug'] = country.slug
    request.session.modified = True

    # Retrieves member
    member = get_object_or_false(Member, user=request.user)
    if not member:
        return redirect('quiz:result', country.slug)

    # Checks if there's an active subscription
    subscription = get_object_or_false(Subscription, member=member)
    active = settings.DB_ID_SUBSCRIPTION_STATUS_ACTIVE
    if subscription and subscription.subscription_status_id == active:
        request.session['subscription_id'] = subscription.id
        return redirect('story:index')
    else:
        if 'subscription_id' in request.session:
            del request.session['subscription_id']
        return redirect('quiz:result', country.slug)

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
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
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
    LoginForm, SignupForm, PasswordRecoveryForm, PasswordResetForm
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

    # Checks if user is already logged and fully registered
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

            # Redirects dashboard to retrieve subscription info and then to next page
            return redirect('%s?next=%s' % (reverse("member:dashboard"), redirect_next))

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
                user.first_name = facebook_basic_data['first_name']
                user.last_name = facebook_basic_data['last_name']
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
            return redirect('%s?next=%s' % (reverse("member:dashboard"), redirect_next))

    # Builds template data dictionary
    template_data = {
        'meta_title': _('Sign-Up | Wanna Migrate'),
        'form': form,
        'facebook_app_id': settings.FACEBOOK_APP_ID,
        'next': redirect_next,
    }

    # Displays HTML template
    return render(request, 'member/signup.html', template_data)


def recover_password(request):
    """
    Sends a link to user redefine it password

    :param: request
    :return: String - The html page rendered
    """

    # Checks if the user is already authenticated.
    if request.user.is_authenticated:
        return redirect("member:dashboard")

    # Instantiates the form
    track_password_reset_email = None
    password_reset_url = None
    form = PasswordRecoveryForm(request.POST or None)

    # if form was submitted and is valid
    if form.is_valid():

        email = form.cleaned_data['email']
        user = get_object_or_false(get_user_model(), email__iexact=email)

        if user and user.is_active:

            # Activates flag to send out notification to reset password
            track_password_reset_email = user.email

            # builds reset link
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            password_reset_url = settings.BASE_URL_SECURE + reverse(
                'member:reset_password', args=(uid, token,)
            )

            # Return success message to template
            messages.success(
                request, 'Password reset instructions will be sent to your e-mail shortly.'
            )

        else:
            messages.error(
                request, 'No member found with email: %s.' % email
            )

    # Builds template data dictionary
    template_data = {
        'meta_title': 'Password Recovery | Wanna Migrate',
        'track_password_reset_email': track_password_reset_email,
        'password_reset_url': password_reset_url,
        'tracking_event_requested_password_reset': settings.TRACKING_EVENT_REQUESTED_PASSWORD_RESET,
        'form': form
    }

    # Displays HTML template
    return render(request, 'member/recover_password.html', template_data)


@sensitive_post_parameters()
@never_cache
def reset_password(request, uidb64=None, token=None):
    """
    Page to set a new password after clicking on a link from email
    sent by 'recover password feature'

    :param: request
    :param: uidb64
    :param: token
    :return: String - The html page rendered
    """

    # If user is already authenticated, logout
    if request.user.is_authenticated:
        auth_logout(request)

    # Tries to find user by the uid given
    uid = urlsafe_base64_decode(uidb64)
    user = get_object_or_false(get_user_model(), pk=uid)
    if not user:
        return redirect('member:recover_password')

    # Checks if token is valid
    token_generator = PasswordResetTokenGenerator()
    if user is None or not token_generator.check_token(user, token):
        return redirect('member:recover_password')

    # Create form
    form = PasswordResetForm(request.POST or None)

    # If form was submitted, it tries to validate and save new password
    if form.is_valid():

        # Saves New password for user
        email = user.email
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Logs user in
        user = authenticate(
            email=email, password=form.cleaned_data['password']
        )
        auth_login(request, user)

        # marks in the template that it was successfully finished
        messages.success(request, 'You password has been updated.')
        return redirect("member:dashboard")

    # Builds template data dictionary
    template_data = {'meta_title': 'Password Reset | Wanna Migrate', 'form': form}

    # Displays HTML template
    return render(request, 'member/reset_password.html', template_data)


@login_required
def dashboard(request):
    """
    How it works

    :param request:
    :return: String
    """

    # Retrieves member
    member = get_object_or_false(Member, user=request.user)
    if not member:
        return redirect('quiz:result', request.session['country_slug'])

    # Checks if there's an active subscription
    subscription = get_object_or_false(Subscription, member=member)
    active = settings.DB_ID_SUBSCRIPTION_STATUS_ACTIVE
    if subscription and subscription.subscription_status_id == active:
        request.session['subscription_id'] = subscription.id
    else:
        if 'subscription_id' in request.session:
            del request.session['subscription_id']

    # Updates the avatar URL
    if member.avatar:
        request.session['avatar_url'] = member.avatar.thumbnail.url

    # Redirects to the next page if not the dashboard
    redirect_next = None
    if 'next' in request.GET:
        redirect_next = request.GET.get('next', redirect_next)
    elif 'next' in request.POST:
        redirect_next = request.POST.get('next', redirect_next)
    if redirect_next and redirect_next != reverse('member:dashboard'):
        return redirect(redirect_next)

    # Builds template data dictionary
    template_data = {
        'meta_title': 'Dashboard | Wanna Migrate',
    }

    # Displays HTML template
    return render(request, 'member/dashboard.html', template_data)

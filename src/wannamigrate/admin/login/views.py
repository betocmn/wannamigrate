"""
Login Views

These are the views that control logic flow for
the crud operations.
"""

##########################
# Imports
##########################
import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from wannamigrate.admin.login.forms import (
    LoginForm, MyAccountForm
)
from wannamigrate.core.decorators import restrict_internal_ips


#######################
# Function to check user is admin
#######################
def admin_check(user):
    return user.is_admin


#######################
# LOGIN / LOGOUT / MY ACCOUNT
#######################
@restrict_internal_ips
@login_required(login_url='admin:login:index')
@user_passes_test(admin_check)
def edit_my_account(request):
    """
    Edit personal data from the logged user

    :param: request
    :return: String
    """
    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and save data
        form = MyAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            request.user = form.save()
            messages.success(request, 'You personal data was successfully updated.')
            return HttpResponseRedirect(reverse('admin:login:my_account'))

    else:
        form = MyAccountForm(instance=request.user)

    # Template data
    context = {'form': form, 'cancel_url': reverse('admin:login:my_account')}

    # Print Template
    return render(request, 'admin/login/edit_my_account.html', context)


@restrict_internal_ips
def index(request):
    """
    Login Form

    :param: request
    :return: String
    """

    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and authenticate user
        form = LoginForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email = email, password = password)

            if user is not None and user.is_active and user.is_admin:
                # Login Successfully
                auth_login(request, user)
                return HttpResponseRedirect(reverse('admin:home'))
            else:
                # Login Failed :(
                messages.error(request, 'Invalid Login. Please Try Again.')

    else:
        form = LoginForm()

    # Template data
    context = { 'form': form }

    # Print Template
    return render(request, 'admin/login/home.html', context)


@restrict_internal_ips
@login_required(login_url='admin:login:index')
@user_passes_test(admin_check)
def logout(request):
    """
    Action for logout

    :param: request
    :return: String
    """
    auth_logout(request)
    return HttpResponseRedirect(reverse('admin:login:index'))


@restrict_internal_ips
@login_required(login_url='admin:login:index')
@user_passes_test(admin_check)
def my_account(request):
    """
    Displays personal data from the logged user

    :param: request
    :return: String
    """

    # Template data
    context = {}

    # Print Template
    return render(request, 'admin/login/my_account.html', context)

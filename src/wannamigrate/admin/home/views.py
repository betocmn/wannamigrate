"""
Home Views

Home sweet home :)
"""

##########################
# Imports
##########################
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.admin.login.views import admin_check


#######################
# HOME
#######################
@restrict_internal_ips
@login_required(login_url='admin:login:index')
@user_passes_test(admin_check, login_url='admin:login:index')
def index(request):
    """
    Index Dashboard - After an user successfully logs in

    :param: request
    :return: String
    """

    # Initial settings
    template_data = {
        'user': request.user,

    }

    return render(request, 'admin/home/index.html', template_data)


@restrict_internal_ips
@login_required(login_url='admin:login:index')
@user_passes_test(admin_check, login_url='admin:login:index')
def restricted(request):
    """
    Restricted notification page

    :param: request
    :return: String
    """

    context = {
        'user': request.user,
    }
    return render(request, 'admin/home/restricted.html', context)

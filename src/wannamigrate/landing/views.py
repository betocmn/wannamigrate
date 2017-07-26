"""
Landing Views

These are the views that control logic flow for
the templates on landing pages
"""

##########################
# Imports
##########################
from django.shortcuts import render, redirect, HttpResponse
from django.utils.translation import ugettext_lazy as _


#######################
# HOME-PAGE VIEWS
#######################
def home(request):
    """
    Home sweet home

    :param request:
    :return: String
    """

    # If logged in, send to dashboard
    if request.user.is_authenticated:
        return redirect('member:dashboard')

    # If coming from a logout
    has_logged_out = request.GET.get('logout', False)

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'has_logged_out': has_logged_out
    }

    # Displays HTML template
    return render(request, 'landing/home.html', template_data)

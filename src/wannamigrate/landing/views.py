"""
Landing Views

These are the views that control logic flow for
the templates on landing pages
"""

##########################
# Imports
##########################
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.conf import settings
from django.utils import translation
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

    context = {'user': request.user}
    return render(request, 'landing/home.html', context)

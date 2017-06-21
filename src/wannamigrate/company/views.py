"""
Admin Views

These are the views that control logic flow for
the templates on admin
"""

##########################
# Imports
##########################
from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from wannamigrate.company.forms import ContactForm
from wannamigrate.core.email_processor import EmailProcessor


#######################
# COMPANY VIEWS
#######################
def contact(request):
    """
    Contact Us

    :param request:
    :return: String
    """

    # Instantiates forms
    form = ContactForm(request.POST or None)

    # if SIGNUP FORM was submitted and is valid
    if form.is_valid():

        # Sends out email
        EmailProcessor.send(
            settings.EMAIL_DEFAULT_TO_ADDRESS, settings.TRACKING_EVENT_SENT_SUPPORT_MESSAGE, {
                'contact_name': form.cleaned_data['name'],
                'contact_email': form.cleaned_data['email'],
                'contact_message': form.cleaned_data['message'],
            })

        # Displays success message
        messages.success(request, _('Your message has been successfully sent.'))

    # Builds template data dictionary
    template_data = {
        'form': form,
        'meta_title': _('Contact Us | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'company/contact.html', template_data)


def about(request):
    """
    How it works

    :param request:
    :return: String
    """

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'meta_title': _('About Us | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'company/about.html', template_data)


def terms(request):
    """
    Terms

    :param request:
    :return: String
    """

    context = {
        'user': request.user,
        'meta_title': _('Terms | Wanna Migrate'),

    }
    return render(request, 'company/terms.html', context)


def privacy(request):
    """
    Privacy

    :param request:
    :return: String
    """

    context = {
        'user': request.user,
        'meta_title': _('Privacy | Wanna Migrate'),

    }
    return render(request, 'company/privacy.html', context)

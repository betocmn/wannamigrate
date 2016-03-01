"""
Marketplace Views

These are the views that control logic flow for
the templates on the marketplace app
"""

##########################
# Imports
##########################
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import ugettext as _
from wannamigrate.core.mailer import Mailer
from wannamigrate.mentorship.forms import ApplyForm





#######################
# LANDING-PAGE
#######################
def landing( request ):
    """
    Home-page for the mentorship product

    :param: request
    :return: String - The html page rendered
    """

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Move to Australia by getting an I.T. job' )
    template_data['meta_description'] = _( '6-week program to learn from professionals who already made it there' )

    # Prints Template
    return render( request, 'mentorship/landing/landing.html', template_data )




#######################
# APPLY
#######################
def apply( request ):
    """
    Apply

    :param: request
    :return: String - The html page rendered
    """

    # Initializes template data dictionary
    template_data = {}
    sent = False

    # Creates form
    form = ApplyForm( request.POST or None )

    # If the form has been submitted...
    if form.is_valid():

        email = form.cleaned_data[ 'email' ]
        name = form.cleaned_data[ 'name' ]
        english_level = form.cleaned_data[ 'english_level' ]
        about = form.cleaned_data[ 'about' ]
        message = "English Level %s <br /><br />%s" % (english_level, about)

        # Send Email with message
        # TODO: Change this to a celery background event and use a try/exception block
        send_result = Mailer.send_contact_email( email, name, message, 'Mentorship Application' )
        messages.success( request, _( 'Your application was successfully sent.' ) )
        sent = True

    # pass form to template
    template_data['form'] = form
    template_data['sent'] = sent

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Move to Australia by getting an I.T. job' )
    template_data['meta_description'] = _( '6-week program to learn from professionals who already made it there' )

    # Prints Template
    return render( request, 'mentorship/apply/apply.html', template_data )




#######################
# PROGRAM (ABOUT)
#######################
def about( request ):
    """
    About page

    :param: request
    :return: String - The html page rendered
    """

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Move to Australia by getting an I.T. job' )
    template_data['meta_description'] = _( '6-week program to learn from professionals who already made it there' )

    # Prints Template
    return render( request, 'mentorship/about/about.html', template_data )





#######################
# FAQ
#######################
def faq( request ):
    """
    FAQ

    :param: request
    :return: String - The html page rendered
    """

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Move to Australia by getting an I.T. job' )
    template_data['meta_description'] = _( '6-week program to learn from professionals who already made it there' )

    # Prints Template
    return render( request, 'mentorship/faq/faq.html', template_data )



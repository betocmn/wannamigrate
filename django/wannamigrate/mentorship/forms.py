"""
Site FORMS

Form definitions used by views/templates from the site app
"""

##########################
# Imports
##########################
from django import forms
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.forms import BaseForm






#######################
# APPLY FORMS
#######################
class ApplyForm( BaseForm ):
    """
    Form to apply for the mentorship progra

    Attributes:
        email    EmailField that grabs the e-mail of the user.
        message  CharField that grabs the message of the user.
    """
    LEVELS = (
        ( '', _( 'Select English Level' ) ),
        ( 'basic', _( 'Basic' ) ),
        ( 'intermediate', _( 'Intermediate' ) ),
        ( 'advanced', _( 'Advanced' ) )
    )
    english_level = forms.ChoiceField( required = True, label = _( "English Level" ), choices = LEVELS, widget = forms.Select( attrs = { 'placeholder' : _( 'English Level' ) } )  )
    name = forms.CharField( required = True, label = _( "Name" ), widget = forms.TextInput( attrs = { 'placeholder' : _( 'Name' ) } ) )
    email = forms.EmailField( required = True, label = _( "E-mail" ), widget = forms.TextInput( attrs = { 'placeholder' : _( 'Email' ) } ) )
    about = forms.CharField( required = True, label = _( "About" ), widget = forms.Textarea( attrs = { 'placeholder' : _( 'About You. Explain what you do, what work experience you have and make sure to include URLs of your online presence (linkedin, facebook, twitter, github, etc...)' ), 'rows': '10' } ) )



"""
company FORMS

Form definitions used by views/templates from the product app
"""

##########################
# Imports
##########################
from django.utils.translation import ugettext_lazy as _
from django.forms import (
    EmailField, CharField, Textarea, EmailInput, TextInput
)
from wannamigrate.core.forms import BaseForm


#######################
# FORM Classes
#######################
class ContactForm(BaseForm):
    """
    Form for regular email/password login
    """
    email = EmailField(required=True, label=_('Your E-mail'), widget=EmailInput(
        attrs={'placeholder': _('barney.simpsom@gmail.com')}
    ))
    name = CharField(required=True, label=_('Your Name'), widget=TextInput(
        attrs={'placeholder': _('Barney Simpsom')}
    ))
    message = CharField(required=True, label=_('Your Message'), widget=Textarea(
        attrs={'placeholder': _('How can we help?'), 'rows': '5'}
    ))

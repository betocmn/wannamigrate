from django import forms
from wannamigrate.core.forms import BaseForm, BaseModelForm
from django.forms import TextInput, PasswordInput, SelectMultiple
from wannamigrate.core.mailer import Mailer


#######################
# LOGIN FORMS
#######################
# Login class here



#######################
# SIGNUP FORMS
#######################
# Signup class here



#######################
# CONTACT FORMS
#######################
class ContactForm( BaseForm ):
    """
    Form to send an e-mail to wannamigrate's admin.

    Attributes:
        email    EmailField that grabs the e-mail of the user.
        message  CharField that grabs the message of the user.
    """
    email = forms.EmailField( widget = forms.TextInput( attrs = { 'placeholder':'E-mail', 'class' : 'form-control' } ) )
    message = forms.CharField( widget = forms.Textarea( attrs = { 'placeholder':'Message', 'class' : 'form-control' } ) )


#######################
# DASHBOARD FORMS
#######################
# Dashboard class here
from django import forms

class LandingPageEmailForm( forms.Form ):
    """ Form that collects the emails from users who are interested on the platform.

        Attributes:
            email    EmailField that grabs the e-mail of the user.
    """
    email = forms.EmailField( widget = forms.TextInput( attrs = { 'id' : 'email', 'placeholder' : 'E-MAIL', 'type' : 'email', } ) )
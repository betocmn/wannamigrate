from django import forms
from django.forms import TextInput, PasswordInput, RadioSelect
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.mailer import Mailer
from wannamigrate.core.forms import BaseForm, BaseModelForm
from wannamigrate.core.models import (
    UserPersonal, UserLanguage, UserLanguageProficiency, UserEducation, UserEducationHistory,
    UserWork, UserWorkExperience, UserWorkOffer
)


#######################
# LOGIN FORMS
#######################
class LoginForm( BaseForm ):
    """
    Form for LOGIN to DASHBOARD
    """
    email = forms.EmailField( required = True, label = _( "E-mail" ), widget = forms.TextInput( attrs = { 'placeholder': ( "E-mail" ), 'class': 'full', 'id': 'login-email' } ) )
    password = forms.CharField( required = True, label = _( "Password" ), widget = forms.PasswordInput( attrs = { 'placeholder': _( "Password" ), 'class': 'half', 'id': 'login-password' } ) )


class PasswordRecoveryForm( BaseForm ):
    """
    Form for RECOVER PASSWORD
    """
    email = forms.EmailField( required = True, label = _( "E-mail" ), widget = forms.TextInput( attrs = { 'placeholder': _( "E-mail" ), 'class': 'full', 'id': 'recovery_email' } ) )


class PasswordResetForm( BaseForm ):
    """
    Form to set a new password

    """
    password = forms.CharField( required = True, label = _( "Password" ), widget = forms.PasswordInput( attrs = { 'class' : ''  } ) )
    password_confirmation = forms.CharField( required = True, label = _( "Confirm Password" ), widget = forms.PasswordInput( attrs = { 'class' : ''  } ) )

    def clean( self ):
        """
        Extra validation for fields that depends on other fields

        :return: Dictionary
        """
        cleaned_data = super( PasswordResetForm, self ).clean()
        password = cleaned_data.get( "password" )
        password_confirmation = cleaned_data.get( "password_confirmation" )

        if password != password_confirmation:
            raise forms.ValidationError( _( "The two passwords do not match." ) )

        return cleaned_data


#######################
# SIGNUP FORMS
#######################
class SignupForm( BaseModelForm ):
    """
    Form for SIGNUP
    """

    email_confirmation = forms.EmailField(
        required = True,
        label = _( "E-Email Confirmation" ),
        error_messages = { 'required': _( 'Please confirm your e-mail address' ) },
        widget = forms.TextInput( attrs = { 'placeholder': _( 'Confirm E-mail' ), 'class': 'full', 'id': 'signup_email_confirmation' } )
    )

    class Meta:
        model = get_user_model()
        fields = [ 'email', 'password' ]
        widgets = {
            'email': TextInput( attrs = { 'placeholder': _( 'E-mail' ), 'class': 'full', 'id': 'signup_email' } ),
            'password': PasswordInput( attrs = { 'placeholder': _( 'Password:' ), 'class': 'half', 'id': 'signup_password' } )
        }
        error_messages = {
            'email': { 'required': _( 'E-mail is required.' ) },
            'password': { 'required': _( 'Password is required' ) }
        }


    def save( self, commit = True ):
        """
        Saves user using the 'create_user' manager method

        :return: Dictionary
        """
        user = get_user_model().objects.create_user( self.cleaned_data["email"], name = '', password = self.cleaned_data["password"] )
        return user

    def clean( self ):
        """
        Extra validation for fields that depends on other fields

        :return: Dictionary
        """
        cleaned_data = super( SignupForm, self ).clean()
        email = cleaned_data.get( "email" )
        email_confirmation = cleaned_data.get( "email_confirmation" )

        if email != email_confirmation:
            raise forms.ValidationError( _( "The two e-mails do not match." ) )

        return cleaned_data


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
    name = forms.CharField( required = True, label = _( "Name" ), widget = forms.TextInput( attrs = { 'class' : '' } ) )
    email = forms.EmailField( required = True, label = _( "E-mail" ), widget = forms.TextInput( attrs = { 'class' : '' } ) )
    message = forms.CharField( required = True, label = _( "Message" ), widget = forms.Textarea( attrs = { 'class' : '' } ) )


#######################
# DASHBOARD FORMS
#######################
class EditUserPersonal( BaseModelForm ):
    """
    Form for EDIT PERSONAL data
    """

    gender = forms.ChoiceField( label = _( "Gender" ), widget = forms.RadioSelect( attrs = { 'class' : 'css-checkbox'  } ) )

    class Meta:
        model = UserPersonal
        fields = [ 'birth_date', 'australian_regional_immigration', 'country' ]
        """widgets = {
            'gender': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
        }"""
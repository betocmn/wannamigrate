"""
Site FORMS

Form definitions used by views/templates from the site app
"""

##########################
# Imports
##########################
from django import forms
from django.forms import TextInput, PasswordInput
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.forms import BaseForm, BaseModelForm
from django.contrib.auth.hashers import is_password_usable





#######################
# LOGIN FORMS
#######################
class LoginForm( BaseForm ):
    """
    Form for LOGIN to DASHBOARD
    """
    email = forms.EmailField( required = True, label = _( "E-mail" ), widget = forms.TextInput( attrs = { 'placeholder': ( "E-mail" ), 'class': 'full', 'id': 'login-email' } ), error_messages = { 'required': _( 'Please inform your e-mail.' ) }, )
    password = forms.CharField( required = True, label = _( "Password" ), widget = forms.PasswordInput( attrs = { 'placeholder': _( "Password" ), 'class': 'half', 'id': 'login-password' } ), error_messages = { 'required': _( 'Please inform your password' ) } )



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
        fields = [ 'name', 'email', 'password' ]
        widgets = {
            'name': TextInput( attrs = { 'placeholder': _( 'Name' ), 'class': 'full', 'id': 'signup_name' } ),
            'email': TextInput( attrs = { 'placeholder': _( 'E-mail' ), 'class': 'full', 'id': 'signup_email' } ),
            'password': PasswordInput( attrs = { 'placeholder': _( 'Password:' ), 'class': 'half', 'id': 'signup_password' } )
        }
        error_messages = {
            'name': { 'required': _( 'Name is required.' ) },
            'email': { 'required': _( 'E-mail is required.' ) },
            'password': { 'required': _( 'Password is required' ) }
        }


    def save( self, commit = True ):
        """
        Saves user using the 'create_user' manager method

        :return: Dictionary
        """
        user = get_user_model().objects.create_user( self.cleaned_data["email"], name = self.cleaned_data["name"], password = self.cleaned_data["password"] )
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
# USER FORMS
#######################
class EditAccountInfoForm( BaseModelForm ):
    """
    Form for EDIT MY ACCOUNT INFO
    """
    # Initializes form values with user data.
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        if 'user' in kwargs:
            self.user = kwargs.pop( "user" )

    # The form data is from User model.
    class Meta:
        model = get_user_model()
        fields = [ 'name', 'email', 'preferred_language' ]
        widgets = {
            'name': TextInput( attrs = { 'class': 'form-control', 'autofocus': 'true' } ),
            'email': TextInput( attrs = { 'class': 'form-control', 'disabled' : 'disabled' } ),
        }



class EditAccountPasswordForm( BaseForm ):
    """
    Form for EDIT MY ACCOUNT PASSWORD
    """
    # Initializes form values with user data.
    def __init__( self, user,  *args, **kwargs ):
        super( BaseForm, self ).__init__( *args, **kwargs )


        self.is_password_usable = False
        self.user = user
        self.is_password_usable = is_password_usable( self.user.password )
       
        # Creates an old password input dinamically
        if self.is_password_usable:
            self.fields['old_password'] = forms.CharField( required = True, label = _( "Old Password" ), widget = forms.PasswordInput( attrs = { 'class' : ''  } ) )

        # Other form fields
        self.fields['new_password'] = forms.CharField( required = True, label = _( "New Password" ), widget = forms.PasswordInput( attrs = { 'class' : ''  } ) )
        self.fields['password_confirmation'] = forms.CharField( required = True, label = _( "Confirm New Password" ), widget = forms.PasswordInput( attrs = { 'class' : ''  } ) )


    def save( self ):
        
        # Save user new password
        self.user.set_password( self.cleaned_data.get( "new_password" ) )
        return self.user.save()


    # Extra validation
    def clean( self ):
        cleaned_data = super( BaseForm, self ).clean()
        
        # Gets cleaned data.
        new_password = cleaned_data[ 'new_password' ]
        password_confirmation = cleaned_data[ 'password_confirmation' ]

        # Check if old password matches.
        if self.is_password_usable:
            old_password = cleaned_data[ 'old_password' ]
            if not self.user.check_password( old_password ):
                raise forms.ValidationError( _( "The old password does not match." ) )    

        # Check if new password and password confirmation matches.
        if new_password != password_confirmation:
            raise forms.ValidationError( _( "The new password and confirmation does not match." ) )    

        # Everything ok
        return cleaned_data




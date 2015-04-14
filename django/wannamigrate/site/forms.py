"""
Site FORMS

Form definitions used by views/templates from the site app
"""

##########################
# Imports
##########################
from django import forms
from django.forms import TextInput, PasswordInput, Select, Textarea
from django.forms.models import BaseInlineFormSet
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.forms import (
    BaseForm, BaseModelForm, CountryChoiceField,
    GoalChoiceField, CountryImmigrationChoiceField
)
from wannamigrate.marketplace.forms import ServiceTypeChoiceField
from wannamigrate.core.models import Situation, Country, Goal, UserSituation, UserPersonal
from wannamigrate.marketplace.models import Provider, ProviderCountry, ProviderServiceType, ServiceType
from django.contrib.auth.hashers import is_password_usable
from django.db.models import F





#######################
# LOGIN FORMS
#######################
class LoginForm( BaseForm ):
    """
    Form for LOGIN to DASHBOARD
    """
    email = forms.EmailField( required = True, label = _( "E-mail" ), widget = forms.TextInput( attrs = { 'placeholder': ( "E-mail" ), 'class': 'full' } ) )
    password = forms.CharField( required = True, label = _( "Password" ), widget = forms.PasswordInput( attrs = { 'placeholder': _( "Password" ), 'class': 'half' } ) )



class PasswordRecoveryForm( BaseForm ):
    """
    Form for RECOVER PASSWORD
    """
    email = forms.EmailField( required = True, label = _( "E-mail" ), widget = forms.TextInput( attrs = { 'placeholder': _( "E-mail" ), 'class': 'full' } ) )



class PasswordResetForm( BaseForm ):
    """
    Form to set a new password

    """
    password = forms.CharField( required = True, label = _( "Password" ), widget = forms.PasswordInput( attrs = { 'placeholder': _( "New Password" ), 'class' : 'full'  } ) )
    password_confirmation = forms.CharField( required = True, label = _( "Confirm Password" ), widget = forms.PasswordInput( attrs = { 'placeholder': _( "Password Confirmation" ), 'class' : 'full'  } ) )

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
# SITUATION FORMS
#######################
class SituationForm( BaseModelForm ):
    """
    Form for visitors or logged users on landing-page and top of dashboard
    """

    from_country = CountryChoiceField( queryset = Country.objects.all(), empty_label = _( 'Select Country' ), widget = forms.Select( attrs = { 'class': 'custom-select country' } ) )
    to_country = CountryImmigrationChoiceField( queryset = Country.objects.filter( immigration_enabled = True ), empty_label = _( 'Select Country' ), widget = forms.Select( attrs = { 'class': 'custom-select country' } ) )
    goal = GoalChoiceField( queryset = Goal.objects.filter( is_active = True ), empty_label = _( 'Select Goal' ), widget = forms.Select( attrs = { 'class': 'custom-select' } ) )

    class Meta:
        model = Situation
        fields = [ 'from_country', 'goal', 'to_country' ]


    def __init__( self, *args, **kwargs ):
        """
        Injects user to the form

        :return: Model Object
        """
        if 'user' in kwargs:
            self.user = kwargs.pop( "user" )
        super( SituationForm, self ).__init__( *args, **kwargs )


    def save( self, commit = True ):
        """
        - Sets the request user before saving to the DB
        - If combination of from_country/goal/to_country already exists, it just
        increments the total visitors or users field, otherwise it inserts a new one.

        :return: Model Object
        """

        # if it's a logged user
        if hasattr( self, 'user' ):

            # checks if user had a previous situation so we can decrement the number of users
            try:
                user_situation = UserSituation.objects.get( user = self.user )
                situation = user_situation.situation
                situation.total_users = F('total_users') - 1
                situation.save()
            except UserSituation.DoesNotExist:
                user_situation = False

            # searches for (or inserts) new situation
            try:
                situation = Situation.objects.get(
                    from_country = self.cleaned_data["from_country"],
                    to_country = self.cleaned_data["to_country"],
                    goal = self.cleaned_data["goal"]
                )
                situation.total_users += 1
                situation.save()
            except Situation.DoesNotExist:
                situation = Situation()
                situation.from_country = self.cleaned_data["from_country"]
                situation.to_country = self.cleaned_data["to_country"]
                situation.goal = self.cleaned_data["goal"]
                situation.total_visitors = 0
                situation.total_users = 1
                situation.save()

            # saves user_situation
            try:
                user_situation = UserSituation.objects.get( user = self.user )
                user_situation.situation = situation
                user_situation.save()
            except UserSituation.DoesNotExist:
                user_situation = UserSituation()
                user_situation.user = self.user
                user_situation.situation = situation
                user_situation.save()

        # if it's a visitor
        else:
            try:
                situation = Situation.objects.get(
                    from_country = self.cleaned_data["from_country"],
                    to_country = self.cleaned_data["to_country"],
                    goal = self.cleaned_data["goal"]
                )
                situation.total_visitors = F('total_visitors') + 1
                situation.save()
            except Situation.DoesNotExist:
                situation = Situation()
                situation.from_country = self.cleaned_data["from_country"]
                situation.to_country = self.cleaned_data["to_country"]
                situation.goal = self.cleaned_data["goal"]
                situation.total_visitors = 1
                situation.total_users = 0
                situation.save()

        return situation





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
        widget = forms.TextInput( attrs = { 'placeholder': _( 'Confirm E-mail' ), 'class': 'full' } )
    )

    class Meta:
        model = get_user_model()
        fields = [ 'name', 'email', 'password' ]
        widgets = {
            'name': TextInput( attrs = { 'placeholder': _( 'Name' ), 'class': 'full' } ),
            'email': TextInput( attrs = { 'placeholder': _( 'E-mail' ), 'class': 'full' } ),
            'password': PasswordInput( attrs = { 'placeholder': _( 'Password:' ), 'class': 'half' } )
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
    SUBJECTS = (
        ( '', _( 'Select Subject' ) ),
        ( '', _( 'General Questions' ) ),
        ( '', _( 'Become a Service Provider' ) ),
        ( '', _( 'Errors & Bugs' ) ),
        ( '', _( 'Payment Problems' ) )
    )
    subject = forms.ChoiceField( required = True, label = _( "Subject" ), choices = SUBJECTS, widget = forms.Select( attrs = { 'class' : '' } )  )
    name = forms.CharField( required = True, label = _( "Name" ), widget = forms.TextInput( attrs = { 'class' : '' } ) )
    email = forms.EmailField( required = True, label = _( "E-mail" ), widget = forms.TextInput( attrs = { 'class' : '' } ) )
    message = forms.CharField( required = True, label = _( "Message" ), widget = forms.Textarea( attrs = { 'class' : '' } ) )





#######################
# MY ACCOUNT FORMS
#######################
class EditAccountForm( BaseModelForm ):
    """
    Form for EDIT MY ACCOUNT INFO
    """

    class Meta:
        model = get_user_model()
        fields = [ 'name', 'email', 'preferred_language' ]
        widgets = {
            'name': TextInput( attrs = { 'class': '', 'autofocus': 'true' } ),
            'email': TextInput( attrs = { 'class': '' } ),
            'preferred_language': Select( attrs = { 'class': 'default-select' } ),
        }



class EditProviderForm( BaseModelForm ):
    """
    Form for EDIT MY ACCOUNT on provider information
    """

    class Meta:
        model = Provider
        fields = [ 'display_name', 'headline', 'description' ]
        widgets = {
            'description': Textarea( attrs = { 'cols': '30', 'rows': '10' } ),
        }

    def __init__( self, *args, **kwargs ):
        """
        Injects user to the form

        :return: Model Object
        """
        if 'user' in kwargs:
            self.user = kwargs.pop( "user" )
        super( EditProviderForm, self ).__init__( *args, **kwargs )

    def save( self, commit = True ):
        """
        Set the request user before saving to the DB

        :return: Model Object
        """
        provider = super( EditProviderForm, self ).save( commit = False )
        if hasattr( self, 'user' ):
            provider.user = self.user
        if commit:
            provider.save()
        return provider



class ProviderCountryForm( BaseModelForm ):
    """
    Form for SUPPORTED COUNTRIES for providers
    """

    country = CountryChoiceField(
        required = True,
        label = _( "Country" ),
        queryset = Country.objects.order_by( 'name' ),
        empty_label = _( 'Select Country' ),
        widget = forms.Select( attrs = { 'class': 'default-select' } )
    )

    class Meta:
        model = ProviderCountry
        fields = [ 'id', 'country', 'provider' ]


class BaseProviderCountryFormSet( BaseInlineFormSet ):
    """
    Formset for supported countries for providers
    """

    def clean( self ):
        """
        Checks that no two records have the same country.

        :return: None
        """
        countries = []
        for form in self.forms:
            if form not in self.deleted_forms and 'country' in form.cleaned_data:
                country = form.cleaned_data['country'].id
                if country in countries:
                    raise forms.ValidationError( _( "You must choose different countries for supported countries." ) )
                countries.append( country )



class ProviderServiceTypeForm( BaseModelForm ):
    """
    Form for SUPPORTED COUNTRIES for providers
    """

    service_type = ServiceTypeChoiceField(
        required = True,
        queryset = ServiceType.objects.filter(),
        empty_label = _( 'Select Service' ),
        widget = forms.Select( attrs = { 'class': 'default-select' } )
    )

    class Meta:
        model = ProviderServiceType
        fields = [ 'id', 'service_type', 'provider', 'price' ]
        widgets = {
            'price': TextInput( attrs = { 'class': 'price' } ),
        }


class BaseProviderServiceTypeFormSet( BaseInlineFormSet ):
    """
    Formset for supported countries for providers
    """

    def clean( self ):
        """
        Checks that no two records have the same service.

        :return: None
        """

        service_types = []
        for form in self.forms:
            if form not in self.deleted_forms and 'service_type' in form.cleaned_data:
                service_type = form.cleaned_data['service_type'].id
                if service_type in service_types:
                    raise forms.ValidationError( _( "You must choose different services for supported services." ) )
                service_types.append( service_type )



class UploadAvatarForm( BaseModelForm ):
    """
    Form for upload avatar
    """

    class Meta:
        model = UserPersonal
        fields = [ 'avatar' ]



class EditPasswordForm( BaseForm ):
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




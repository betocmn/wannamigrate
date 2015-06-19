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
from wannamigrate.core.models import Situation, Country, Goal, UserSituation, UserPersonal, Conversation, ConversationMessage
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
                situation.total_users = F( 'total_users' ) - 1
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
        ( 'General Questions', _( 'General Questions' ) ),
        ( 'Become a Service Provider', _( 'Become a Service Provider' ) ),
        ( 'Website Errors', _( 'Website Errors' ) ),
        ( 'Payment Problems', _( 'Payment Problems' ) ),
        ( 'Report User or Content', _( 'Report User or Content' ) )
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
        fields = [ 'name', 'email', 'preferred_language', 'preferred_timezone' ]
        widgets = {
            'name': TextInput( attrs = { 'class': '', 'autofocus': 'true' } ),
            'email': TextInput( attrs = { 'class': '' } ),
            'preferred_language': Select( attrs = { 'class': 'default-select' } ),
            'preferred_timezone': Select( attrs = { 'class': 'default-select' } ),
        }



class EditPasswordForm( BaseModelForm ):
    """
    Form for EDIT PASSWORD
    """

    confirm_password = forms.CharField( required = True, label = "Confirm New Password", widget = forms.PasswordInput( attrs = { 'class' : ''  } ) )

    class Meta:
        model = get_user_model()
        fields = [ 'password' ]
        widgets = {
            'password': PasswordInput(),
        }


    def save( self, commit = True ):
        """
        If passwords are set, they need to be set on a different way

        :return: Dictionary
        """
        user = super( EditPasswordForm, self ).save( commit = False )
        password = self.cleaned_data["password"]
        if password:
            user.set_password( password )
        if commit:
            user.save()
        return user


    def clean( self ):
        """
        Extra validation for fields that depends on other fields

        :return: Dictionary
        """
        cleaned_data = super( EditPasswordForm, self ).clean()
        password = cleaned_data.get( "password" )
        confirm_password = cleaned_data.get( "confirm_password" )

        if password != confirm_password:
            raise forms.ValidationError( _( "Passwords do not match." ) )

        return cleaned_data



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
        queryset = ServiceType.objects.filter( is_active = True ),
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



class StartConversationForm( BaseModelForm ):
    """
    Form to create a message on site.
    """
    # The content of the initial message.
    content = forms.CharField( widget=forms.Textarea )

    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = Conversation
        fields = [ "subject" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):
        # The owner of the conversation (from_user)
        owner = kwargs.pop( "owner" )
        to_user = kwargs.pop( "to_user" )

        # Calls the constructor
        super( StartConversationForm, self ).__init__( *args, **kwargs )

        # Initialize pre-defined data.
        self.instance.from_user = owner
        self.instance.to_user = to_user

    def clean( self, *args, **kwargs ):
        cleaned_data = super( StartConversationForm, self ).clean( *args, **kwargs )

        # Removes all extra spaces from content string
        stripped_content = ' '.join( cleaned_data[ "content" ].split() )
        cleaned_data[ "content" ] = stripped_content

        return cleaned_data



class ReplyConversationForm( BaseModelForm ):
    """
    Form to create a message.
    """
    # The content of the initial message.
    content = forms.CharField( widget=forms.Textarea )

    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = ConversationMessage
        fields = [ "content" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):
        # The owner of the conversation (from_user)
        conversation = kwargs.pop( "conversation" )
        owner = kwargs.pop( "owner" )
        # Calls the constructor
        super( ReplyConversationForm, self ).__init__( *args, **kwargs )
        # Initialize pre-defined data.
        self.instance.conversation = conversation
        self.instance.owner = owner
        self.instance.is_read = False

    def clean( self, *args, **kwargs ):
        cleaned_data = super( ReplyConversationForm, self ).clean( *args, **kwargs )

        # Removes all extra spaces from content string
        stripped_content = ' '.join( cleaned_data[ "content" ].split() )
        cleaned_data[ "content" ] = stripped_content

        return cleaned_data
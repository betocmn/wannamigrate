from django import forms
from django.forms import TextInput, PasswordInput, RadioSelect, ModelChoiceField, ChoiceField, Select
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.forms.models import BaseInlineFormSet
from datetime import date
from django.conf import settings
from wannamigrate.core.mailer import Mailer
from wannamigrate.core.util import get_object_or_false
from wannamigrate.core.forms import BaseForm, BaseModelForm, CountryChoiceField, LanguageChoiceField
from wannamigrate.core.models import (
    Answer, AnswerCategory, Question, Language,
    Country, UserPersonal, UserLanguage, UserLanguageProficiency, UserEducation, UserEducationHistory,
    UserWork, UserWorkExperience, UserWorkOffer, UserPersonalFamily
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
# DASHBOARD - PERSONAL FORMS
#######################
class UserPersonalForm( BaseModelForm ):
    """
    Form for USER PERSONAL data
    """

    country = CountryChoiceField( required = False, label = _( "Country of Residence" ), queryset = Country.objects.order_by( 'immigration_enabled' ), empty_label = _( 'Select Country' ) )

    class Meta:
        model = UserPersonal
        fields = [ 'birth_date', 'australian_regional_immigration', 'gender', 'country', 'family_overseas' ]
        widgets = {
            'birth_date': SelectDateWidget( years = range( 1940, date.today().year - 15 ), attrs = { 'class': 'force-style', 'style': 'display: inline; width: 120px;' } ),
            'gender': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
            'australian_regional_immigration': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
            'family_overseas': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
        }

    def __init__( self, *args, **kwargs ):
        """
        Injects user to the form

        :return: Model Object
        """
        if 'user' in kwargs:
            self.user = kwargs.pop( "user" )
        super( UserPersonalForm, self ).__init__( *args, **kwargs )

    def save( self, commit = True ):
        """
        Set the request user before saving to the DB

        :return: Model Object
        """
        user_personal = super( UserPersonalForm, self ).save( commit = False )
        if hasattr( self, 'user' ):
            user_personal.user = self.user
        if commit:
            user_personal.save()
        return user_personal


class UserPersonalFamilyForm( BaseModelForm ):
    """
    Form for USER PERSONAL FAMILY data (If user has family in any other country)
    """

    country = CountryChoiceField( required = False, label = _( "In Which Country" ), queryset = Country.objects.order_by( 'name' ), empty_label = _( 'Select Country' ) )

    class Meta:
        model = UserPersonalFamily
        fields = [ 'id', 'country', 'user' ]


class BaseUserPersonalFamilyFormSet( BaseInlineFormSet ):
    """
    Formset for answers / country points
    """

    def clean( self ):
        """
        Checks that no two records have the same country.

        :return: None
        """
        if any( self.errors ):
            # Don't bother validating the formset unless each form is valid on its own
            return
        countries = []
        for form in self.forms:
            if form not in self.deleted_forms and 'country' in form.cleaned_data:
                country = form.cleaned_data['country'].id
                if country in countries:
                    raise forms.ValidationError( _( "You must choose different countries on family overseas option." ) )
                countries.append( country )

    def save( self ):
        """
        After saving the forms, it search if a family member overseas
        was entered. If yes, we need to update the field (boolean)
        on the UserPersonal model.

        :return: List of models
        """
        instances = super( BaseUserPersonalFamilyFormSet, self ).save()

        if self.has_changed():

            # iterate over forms submitted and check if a family overseas member was added
            family_overseas = False
            for form in self.forms:
                user = form.cleaned_data['user']
                if form not in self.deleted_forms:
                    if form.cleaned_data['country'].id is not None:
                        family_overseas = True
                        break

            # Update UserLanguage object
            user_personal = UserPersonal.objects.get( user = user )
            user_personal.family_overseas = family_overseas
            user_personal.save()

        return instances


#######################
# DASHBOARD - LANGUAGE FORMS
#######################
class UserLanguageForm( BaseModelForm ):
    """
    Form for USER LANGUAGE data
    """

    partner_english_level_answer = ModelChoiceField( required = False, label = _( "If you have a partner, what is his/her ENGLISH Level" ), queryset = Answer.objects.filter( question_id = settings.ID_QUESTION_PARTNER_ENGLISH ), empty_label = _( 'Select Level' ) )
    partner_french_level_answer = ModelChoiceField( required = False, label = _( "If you have a partner, what is his/her FRENCH Level" ), queryset = Answer.objects.filter( question_id = settings.ID_QUESTION_PARTNER_FRENCH ), empty_label = _( 'Select Level' ) )

    class Meta:
        model = UserLanguage
        fields = [ 'australian_community_language', 'partner_english_level_answer', 'partner_french_level_answer' ]
        widgets = {
            'gender': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
            'australian_community_language': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
        }

    def __init__( self, *args, **kwargs ):
        """
        Injects user to the form

        :return: Model Object
        """
        if 'user' in kwargs:
            self.user = kwargs.pop( "user" )
        super( UserLanguageForm, self ).__init__( *args, **kwargs )

    def save( self, commit = True ):
        """
        Set the request user before saving to the DB

        :return: Model Object
        """
        user_language = super( UserLanguageForm, self ).save( commit = False )
        if hasattr( self, 'user' ):
            user_language.user = self.user
        if commit:
            user_language.save()
        return user_language


class UserLanguageProficiencyForm( BaseModelForm ):
    """
    Form for USER LANGUAGE PROFICIENCY data (levels of foreign languages)
    """

    language = LanguageChoiceField( required = True, label = _( "Language" ), queryset = Language.objects.order_by( 'name' ), empty_label = _( 'Select Language' ) )
    language_level_answer = ModelChoiceField( required = True, label = _( "Level" ), queryset = Answer.objects.filter( question_id = settings.ID_QUESTION_LANGUAGE_LEVEL_OTHERS ), empty_label = _( 'Select Level' ) )

    class Meta:
        model = UserLanguageProficiency
        fields = [ 'id', 'language', 'language_level_answer', 'user' ]

    def __init__( self, *args, **kwargs ):
        """
        Adjust the correct answer ID if language is english or french when loading the form

        :return: Dictionary
        """
        super( UserLanguageProficiencyForm, self ).__init__( *args, **kwargs )

        # if language is english, we fix the answer ID by using a map of IDS from settings
        if hasattr( self, 'initial' ) and 'language_level_answer' in self.initial:
            if self.initial['language'] == settings.ID_LANGUAGE_ENGLISH:
                for key, value in settings.ID_ENGLISH_LEVEL_MAP.items():
                    if value == self.initial['language_level_answer']:
                        answer_id = key
                        break
                self.initial['language_level_answer'] = Answer.objects.get( pk = answer_id )

        # if language is french, we fix the answer ID by using a map of IDS from settings
        if hasattr( self, 'initial' ) and 'language_level_answer' in self.initial:
            if self.initial['language'] == settings.ID_LANGUAGE_FRENCH:
                for key, value in settings.ID_FRENCH_LEVEL_MAP.items():
                    if value == self.initial['language_level_answer']:
                        answer_id = key
                        break
                self.initial['language_level_answer'] = Answer.objects.get( pk = answer_id )


    def save( self, commit = True ):
        """
        Adjust the correct answer ID if language is english or french when saving the form

        :return: Dictionary
        """
        user_language_proficiency = super( UserLanguageProficiencyForm, self ).save( commit = False )
        #if commit:

        # if language is english, we fix the answer ID by using a map of IDS from settings
        if user_language_proficiency.language.id == settings.ID_LANGUAGE_ENGLISH:
            user_language_proficiency.language_level_answer = Answer.objects.get( pk = settings.ID_ENGLISH_LEVEL_MAP[user_language_proficiency.language_level_answer.id] )

        # if language is french, we fix the answer ID by using a map of IDS from settings
        if user_language_proficiency.language.id == settings.ID_LANGUAGE_FRENCH:
            user_language_proficiency.language_level_answer = Answer.objects.get( pk = settings.ID_FRENCH_LEVEL_MAP[user_language_proficiency.language_level_answer.id] )

        # saves model
        user_language_proficiency.save()

        return user_language_proficiency

class BaseUserLanguageProficiencyFormSet( BaseInlineFormSet ):
    """
    Formset for answers / country points
    """

    def clean( self ):
        """
        Checks that no two records have the same language.

        :return: None
        """
        if any( self.errors ):
            # Don't bother validating the formset unless each form is valid on its own
            return
        languages = []
        for form in self.forms:
            if form not in self.deleted_forms and 'language' in form.cleaned_data:
                language = form.cleaned_data['language'].id
                if language in languages:
                    raise forms.ValidationError( _( "You must choose different languages." ) )
                languages.append( language )

    def save( self ):
        """
        After saving the forms, it search if a language specific for
        Australia was entered. If yes, we need to update the field (boolean)
        on the UserLanguage model.

        :return: List of models
        """
        instances = super( BaseUserLanguageProficiencyFormSet, self ).save()

        if self.has_changed():

            # iterate over forms submitted and check if language is on the australian list
            australian_community_language = False
            for form in self.forms:
                user = form.cleaned_data['user']
                if form not in self.deleted_forms:
                    if form.cleaned_data['language'].id in settings.ID_AUSTRALIAN_COMMUNITY_LANGUAGES:
                        australian_community_language = True
                        break

            # Update UserLanguage object
            user_language = UserLanguage.objects.get( user = user )
            user_language.australian_community_language = australian_community_language
            user_language.save()

        return instances
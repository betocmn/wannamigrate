from django import forms
from django.forms import TextInput, PasswordInput, RadioSelect, ModelChoiceField, ChoiceField, Select, TypedChoiceField
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth import get_user_model
from django.utils.translation import pgettext_lazy, ugettext_lazy as _
from django.forms.models import BaseInlineFormSet
from datetime import date
from django.conf import settings
from wannamigrate.core.mailer import Mailer
from wannamigrate.core.util import get_object_or_false, get_months_duration_tuple, dbg
from wannamigrate.core.forms import BaseForm, BaseModelForm, CountryChoiceField, LanguageChoiceField
from wannamigrate.core.models import (
    Answer, Question, Language,
    Country, User, UserPersonal, UserLanguage, UserLanguageProficiency, UserEducation, UserEducationHistory,
    UserWork, UserWorkExperience, UserWorkOffer, UserPersonalFamily, Occupation, OccupationCategory
)
from wannamigrate._settings.base import LANGUAGES
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
# USER PERSONAL FORMS
#######################
class UserPersonalForm( BaseModelForm ):
    """
    Form for USER PERSONAL data
    """

    country = CountryChoiceField( required = False, label = _( "Country of Citizenship" ), queryset = Country.objects.order_by( 'immigration_enabled' ), empty_label = _( 'Select Country' ) )

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

    country = CountryChoiceField( required = True, label = _( "In Which Country" ), queryset = Country.objects.order_by( 'name' ), empty_label = _( 'Select Country' ) )

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
            user = False
            for form in self.forms:
                if 'user' in form.cleaned_data:
                    user = form.cleaned_data['user']
                    if form not in self.deleted_forms:
                        if form.cleaned_data['country'].id is not None:
                            family_overseas = True
                            break

            # Update UserLanguage object
            if user:
                user_personal = UserPersonal.objects.get( user = user )
                user_personal.family_overseas = family_overseas
                user_personal.save()

        return instances


#######################
# USER LANGUAGE FORMS
#######################
class UserLanguageForm( BaseModelForm ):
    """
    Form for USER LANGUAGE data
    """

    partner_english_level_answer = ModelChoiceField( required = False, label = _( "If you have a partner/spouse, what is his/her ENGLISH Level" ), queryset = Answer.objects.filter( question_id = settings.ID_QUESTION_PARTNER_ENGLISH ), empty_label = _( 'Select Level' ) )
    partner_french_level_answer = ModelChoiceField( required = False, label = _( "If you have a partner/spouse, what is his/her FRENCH Level" ), queryset = Answer.objects.filter( question_id = settings.ID_QUESTION_PARTNER_FRENCH ), empty_label = _( 'Select Level' ) )

    class Meta:
        model = UserLanguage
        fields = [ 'partner_english_level_answer', 'partner_french_level_answer' ]

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

    language = LanguageChoiceField( required = True, label = pgettext_lazy( "Singular", "Language" ), queryset = Language.objects.order_by( 'name' ), empty_label = _( 'Select Language' ) )
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


#######################
# USER EDUCATION FORMS
#######################
class UserEducationForm( BaseModelForm ):
    """
    Form for USER EDUCATION data
    """

    partner_education_level_answer = ModelChoiceField( required = False, label = _( "If you have a partner/spouse, what is his/her highest Degree" ), queryset = Answer.objects.filter( question_id = settings.ID_QUESTION_PARTNER_EDUCATION_DEGREE ), empty_label = _( 'Select Degree' ) )

    class Meta:
        model = UserEducation
        fields = [ 'regional_australia_study', 'partner_education_level_answer' ]
        widgets = {
            'regional_australia_study': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
        }

    def __init__( self, *args, **kwargs ):
        """
        Injects user to the form

        :return: Model Object
        """
        if 'user' in kwargs:
            self.user = kwargs.pop( "user" )
        super( UserEducationForm, self ).__init__( *args, **kwargs )

    def save( self, commit = True ):
        """
        Set the request user before saving to the DB

        :return: Model Object
        """
        user_education = super( UserEducationForm, self ).save( commit = False )
        if hasattr( self, 'user' ):
            user_education.user = self.user
        if commit:
            user_education.save()
        return user_education


class UserEducationHistoryForm( BaseModelForm ):
    """
    Form for USER EDUCATION HISTORY data (degrees of education)
    """

    YEARS_START = ( ( '', 'Select Year' ), ) + tuple( ( str( n ), str( n ) ) for n in range( 1960, date.today().year + 1 ) )
    YEARS_END = ( ( '', 'Select Year' ), ) + tuple( ( str( n ), str( n ) ) for n in range( 1960, date.today().year + 5 ) )

    education_level_answer = ModelChoiceField( required = True, label = _( "Level" ), queryset = Answer.objects.filter( question_id = settings.ID_QUESTION_EDUCATION_DEGREE ), empty_label = _( 'Select Level' ) )
    country = CountryChoiceField( required = True, label = _( "Country" ), queryset = Country.objects.order_by( 'name' ), empty_label = _( 'Select Country' ) )
    year_start = ChoiceField( required = True, label = _( "Start Year" ), choices = YEARS_START )
    year_end = ChoiceField( required = True, label = _( "End Year" ), choices = YEARS_END )

    class Meta:
        model = UserEducationHistory
        fields = [ 'id', 'school', 'year_start', 'year_end', 'country', 'education_level_answer', 'user' ]


#######################
# USER WORK FORMS
#######################
class UserWorkForm( BaseModelForm ):
    """
    Form for USER WORK data
    """

    occupation_category = ModelChoiceField( required = False, label = _( "Category" ), queryset = OccupationCategory.objects.all(), empty_label = _( 'Select Area' ) )
    occupation = ModelChoiceField( required = False, label = _( "What is your occupation" ), queryset = Occupation.objects.none() )

    class Meta:
        model = UserWork
        fields = [ 'willing_to_invest', 'canadian_startup_letter', 'australian_professional_year', 'canadian_partner_work_study_experience', 'occupation', 'partner_skills', 'work_offer' ]
        widgets = {
            'willing_to_invest': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
            'canadian_startup_letter': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
            'australian_professional_year': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
            'canadian_partner_work_study_experience': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
            'work_offer': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
            'partner_skills': RadioSelect( attrs = { 'class': 'css-checkbox' } ),
        }

    def __init__( self, *args, **kwargs ):
        """
        Injects user to the form

        :return: Model Object
        """

        if 'user' in kwargs:
            self.user = kwargs.pop( "user" )
        super( UserWorkForm, self ).__init__( *args, **kwargs )
        if self._raw_value( 'occupation_category' ) is not None and self._raw_value( 'occupation_category' ) != '':
            self.fields['occupation_category'].initial = self._raw_value( 'occupation_category' )
            self.fields['occupation'].queryset = Occupation.objects.filter( occupation_category = self._raw_value( 'occupation_category' ) )
        elif self.fields['occupation_category'].initial:
            self.fields['occupation'].queryset = Occupation.objects.filter( occupation_category = self.fields['occupation_category'].initial )
        elif self.instance and self.instance.occupation and self.instance.occupation.occupation_category_id:
            self.fields['occupation_category'].initial = self.instance.occupation.occupation_category_id
            self.fields['occupation'].queryset = Occupation.objects.filter( occupation_category_id = self.instance.occupation.occupation_category_id )

    def save( self, commit = True ):
        """
        Set the request user before saving to the DB

        :return: Model Object
        """
        user_work = super( UserWorkForm, self ).save( commit = False )
        if hasattr( self, 'user' ):
            user_work.user = self.user
        if commit:
            user_work.save()
        return user_work


class UserWorkExperienceForm( BaseModelForm ):
    """
    Form for USER WORK EXPERIENCE data (degrees of work)
    """

    country = CountryChoiceField( required = True, label = _( "Country" ), queryset = Country.objects.order_by( 'name' ), empty_label = _( 'Select Country' ) )
    months = ChoiceField( required = True, label = _( "Duration" ), choices = get_months_duration_tuple() )

    class Meta:
        model = UserWorkExperience
        fields = [ 'id', 'company', 'months', 'country', 'user' ]
        
        
class UserWorkOfferForm( BaseModelForm ):
    """
    Form for USER WORK OFFER data (If user has job offers from other countries)
    """

    country = CountryChoiceField( required = True, label = _( "From Which Country" ), queryset = Country.objects.order_by( 'name' ), empty_label = _( 'Select Country' ) )

    class Meta:
        model = UserWorkOffer
        fields = [ 'id', 'country', 'user' ]


class BaseUserWorkOfferFormSet( BaseInlineFormSet ):
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
                    raise forms.ValidationError( _( "You must choose different countries on work offers overseas." ) )
                countries.append( country )

    def save( self ):
        """
        After saving the forms, it search if a work offer overseas
        was entered. If yes, we need to update the field (boolean)
        on the UserWork model.

        :return: List of models
        """
        instances = super( BaseUserWorkOfferFormSet, self ).save()

        if self.has_changed():

            # iterate over forms submitted and check if a work offer overseas was added
            work_offer = False
            user = False
            for form in self.forms:
                if 'user' in form.cleaned_data:
                    user = form.cleaned_data['user']
                    if form not in self.deleted_forms:
                        if form.cleaned_data['country'].id is not None:
                            work_offer = True
                            break

            # Update UserLanguage object
            if user:
                user_work = UserWork.objects.get( user = user )
                user_work.work_offer = work_offer
                user_work.save()

        return instances


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

    
from django import forms
from django.forms import TextInput, SelectMultiple, HiddenInput
from django.forms.models import BaseInlineFormSet
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from wannamigrate.core.forms import BaseForm, BaseModelForm
from wannamigrate.core.mailer import Mailer
from wannamigrate.core.models import Question, Answer, CountryPoints, Country

#######################
# LOGIN / LOGOUT / MY ACCOUNT
#######################
class LoginForm( BaseForm ):
    """
    Form for LOGIN to ADMIN
    """
    email = forms.EmailField( widget = forms.TextInput( attrs = { 'placeholder':'E-mail', 'class' : 'form-control' } ) )
    password = forms.CharField( widget = forms.PasswordInput( attrs = { 'placeholder' : 'Password', 'class' : 'form-control'  } ) )


class MyAccountForm( BaseModelForm ):
    """
    Form for EDIT MY ACCOUNT
    """

    password = forms.CharField( required = False, label = "Password", widget = forms.PasswordInput( attrs = { 'class' : 'form-control'  } ) )
    confirm_password = forms.CharField( required = False, label = "Confirm Password", widget = forms.PasswordInput( attrs = { 'class' : 'form-control'  } ) )

    class Meta:
        model = get_user_model()
        fields = [ 'name', 'email' ]
        widgets = {
            'name': TextInput( attrs = { 'class': 'form-control', 'autofocus': 'true' } ),
            'email': TextInput( attrs = { 'class': 'form-control' } )
        }

    def save( self, commit = True ):
        """
        If passwords are set, they need to be set on a different way

        :return: Dictionary
        """
        user = super( MyAccountForm, self ).save( commit = False )
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
        cleaned_data = super( MyAccountForm, self ).clean()
        password = cleaned_data.get( "password" )
        confirm_password = cleaned_data.get( "confirm_password" )

        if password != confirm_password:
            raise forms.ValidationError( "Passwords do not match." )

        return cleaned_data


#######################
# ADMIN USERS
#######################
class AdminUserForm( BaseModelForm ):
    """
    Form for ADD and EDIT ADMIN USERS
    """

    class Meta:
        model = get_user_model()
        fields = [ 'name', 'email', 'is_superuser', 'is_active', 'groups' ]
        widgets = {
            'name': TextInput( attrs = { 'class': 'form-control', 'autofocus': 'true' } ),
            'email': TextInput( attrs = { 'class': 'form-control' } ),
            'groups': SelectMultiple( attrs = { 'class': 'form-control', 'style': 'height: 150px;' } )
        }

    def save( self, commit = True ):
        """
        Extra processing: Set additional default values for new users

        :return: Dictionary
        """
        user = super( AdminUserForm, self ).save( commit = False )
        user.is_admin = True
        if not user.password:
            plain_password = get_user_model().objects.make_random_password()
            user.set_password( plain_password )
        if commit:
            user.save()
            user.groups = self.cleaned_data['groups']
            if 'plain_password' in locals():
                # Sends Login Info Email
                # TODO Change this to a celery/signal background task
                Mailer.send_login_email( user.email, { 'user': user, 'plain_password': plain_password } )
        return user


#######################
# GROUPS AND PERMISSIONS
#######################
class GroupForm( BaseModelForm ):
    """
    Form for ADD and EDIT ADMIN USERS
    """

    class Meta:
        model = Group
        fields = [ 'name', 'permissions' ]
        widgets = {
            'name': TextInput( attrs = { 'class': 'form-control', 'autofocus': 'true' } ),
            'permissions': SelectMultiple( attrs = { 'class': 'form-control', 'style': 'height: 200px;' } )
        }


#######################
# IMMIGRATION RULES (QUESTION, ANSWERS AND POINTS)
#######################
class QuestionForm( BaseModelForm ):
    """
    Form for ADD and EDIT Questions
    """

    class Meta:
        model = Question
        fields = [ 'description', 'help_text' ]
        widgets = {
            'description': TextInput( attrs = { 'class': 'form-control', 'autofocus': 'true' } ),
            'help_text': TextInput( attrs = { 'class': 'form-control' } )
        }


class AnswerForm( BaseModelForm ):
    """
    Form for ADD and EDIT Answers
    """

    class Meta:
        model = Answer
        fields = [ 'id', 'description', 'question' ]
        widgets = {
            'description': TextInput( attrs = { 'class': 'form-control' } ),
            'question': HiddenInput(),
            'id': HiddenInput()
        }

    def __init__( self, *args, **kwargs ):
        self.countries = kwargs.pop( "countries" )
        self.points_per_country = kwargs.pop( "points_per_country" )
        super( AnswerForm, self ).__init__( *args, **kwargs )
        countries = self.countries
        points_per_country = self.points_per_country
        answer_id = self.instance.id
        if countries is not None:
            for country in countries:
                name = "points_%s" % ( country.id )
                if country.id in points_per_country and answer_id in points_per_country[country.id]:
                    value = points_per_country[country.id][answer_id]
                else:
                    value = ''
                self.fields[name] = forms.IntegerField( initial = value, widget = TextInput( attrs = { 'class': 'form-control points', 'maxlength': '2', 'style': 'width: 60px; float: left;' } ) )

    def save( self, commit = True ):
        """
        Extra processing: Set additional default values for new users

        :return: Dictionary
        """
        answer = super( AnswerForm, self ).save( commit = True )
        for form_element_name in self.cleaned_data:
            if 'points' in form_element_name:
                country_points = CountryPoints()
                country_points.answer_id = answer.id
                country_points.country_id = form_element_name.split( '_' )[-1] # name is similar to 'points_3' where 3 is the country ID
                country_points.points = int( self.cleaned_data[form_element_name] )
                country_points.save()

        return answer


class BaseAnswerFormSet( BaseInlineFormSet ):
    """
    Formset for answers / country points
    """

    def __init__( self, *args, **kwargs ):

        self.countries = kwargs.pop( "countries" )
        self.points_per_country = kwargs.pop( "points_per_country" )
        super( BaseAnswerFormSet, self ).__init__( *args, **kwargs )

    def _construct_form( self, *args, **kwargs ):
        # inject user in each form on the formset
        kwargs['countries'] = self.countries
        kwargs['points_per_country'] = self.points_per_country
        return super( BaseAnswerFormSet, self )._construct_form( *args, **kwargs )

    """
    def add_fields( self, form, index ):
        super( BaseAnswerFormSet, self ).add_fields( form, index )
        countries = self.countries
        points_per_country = self.points_per_country
        if countries is not None:
            for country in countries:
                name = "points_%s" % ( country.id )
                #if country.id in points_per_country and
                form.fields[name] = forms.IntegerField( initial = self.answer.id, widget = TextInput( attrs = { 'class': 'form-control', 'maxlength': '2', 'style': 'width: 60px; float: left;' } ) )
    """
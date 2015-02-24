"""
Admin FORMS

Form definitions used by views/templates from the admin app
"""

##########################
# Imports
##########################
from django import forms
from django.forms import TextInput, SelectMultiple, HiddenInput, Select, ModelMultipleChoiceField, ModelChoiceField
from django.forms.models import BaseInlineFormSet
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from wannamigrate.core.forms import BaseForm, BaseModelForm
from wannamigrate.core.models import Country
from wannamigrate.points.models import Question, Answer, CountryPoints, Occupation, OccupationCategory
from wannamigrate.qa.models import Post, PostType, Topic, PostHistory
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


#######################
# LOGIN / LOGOUT / MY ACCOUNT
#######################
class LoginForm( BaseForm ):
    """
    Form for LOGIN to ADMIN
    """
    email = forms.EmailField( widget = forms.TextInput( attrs = { 'placeholder':'E-mail', 'class': 'form-control' } ) )
    password = forms.CharField( widget = forms.PasswordInput( attrs = { 'placeholder': 'Password', 'class': 'form-control' } ) )



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
# USERS
#######################
class UserForm( BaseModelForm ):
    """
    Form for ADD and EDIT USERS
    """

    class Meta:
        model = get_user_model()
        fields = [ 'name', 'email', 'is_active' ]
        widgets = {
            'name': TextInput( attrs = { 'class': 'form-control', 'autofocus': 'true' } ),
            'email': TextInput( attrs = { 'class': 'form-control' } )
        }

    def save( self, commit = True ):
        """
        Extra processing: Set additional default values for new users

        :return: Dictionary
        """
        user = super( UserForm, self ).save( commit = False )
        user.is_admin = False
        if not user.password:
            plain_password = get_user_model().objects.make_random_password()
            user.set_password( plain_password )
        if commit:
            user.save()
        return user





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
        Extra processing

        :return: Dictionary
        """
        answer = super( AnswerForm, self ).save( commit = True )
        for form_element_name in self.cleaned_data:
            if 'points' in form_element_name:

                # data to be saved
                country_id = form_element_name.split( '_' )[-1] # name is similar to 'points_3' where 3 is the country ID
                points = int( self.cleaned_data[form_element_name] )

                # save (update or create)
                CountryPoints.objects.update_or_create(
                    answer_id = answer.id, country_id = country_id, defaults = { 'points': points }
                )

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
        # inject extra values in each form on the formset
        kwargs['countries'] = self.countries
        kwargs['points_per_country'] = self.points_per_country
        return super( BaseAnswerFormSet, self )._construct_form( *args, **kwargs )





#######################
# OCCUPATIONS
#######################
class OccupationForm( BaseModelForm ):
    """
    Form for ADD and EDIT ADMIN USERS
    """

    countries = ModelMultipleChoiceField(
        required = True, label = "Countries",
        queryset = Country.objects.filter( immigration_enabled = True ).order_by( 'name' ),
        widget = SelectMultiple( attrs = { 'class': 'form-control', 'style': 'height: 200px;' } )
    )

    occupation_category = ModelChoiceField(
        required = False, label = "Category",
        queryset = OccupationCategory.objects.order_by( 'name' ),
        widget = Select( attrs = { 'class': 'form-control' } )
    )

    class Meta:
        model = Occupation
        fields = [ 'name', 'occupation_category', 'countries' ]
        widgets = {
            'name': TextInput( attrs = { 'class': 'form-control', 'autofocus': 'true' } ),
        }





###################################
# Q&A Forms
###################################
class PostForm( BaseModelForm ):
    """
    Form to create post on admin.
    """
    
    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = Post
        fields = [ "post_type", "owner", "title", "body", "is_anonymous", "related_topics" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):
        super( PostForm, self ).__init__( *args, **kwargs )

        # Overrides the choices to the post_type field.
        self.fields[ "post_type" ].choices = PostType.objects.filter( id__in = [ settings.QA_POST_TYPE_BLOGPOST_ID, settings.QA_POST_TYPE_QUESTION_ID ] ).values_list( "id", "name" )

        # Overrides the choices to the related_topics field.
        self.fields[ "related_topics" ].choices = Topic.objects.values_list( "id", "name" )
        self.fields[ "related_topics" ].required = True

        # Overrides the id of the widget for the owner
        self.fields[ "owner" ].widget.attrs['id'] = "owner_id"



    def clean( self ):
        """ Cleans form data """
        cleaned_data = super( PostForm, self ).clean()

        # Gets form stuffs
        parent = cleaned_data.get( "parent" )
        post_type = cleaned_data.get( "post_type" )
        title = cleaned_data.get( "title" )
        body = cleaned_data.get( "body" )
        is_anonymous = cleaned_data.get( "is_anonymous" )
        related_topics = cleaned_data.get( "related_topics" )

        # Post extra-validation
        if post_type.id == settings.QA_POST_TYPE_ANSWER_ID:

            # An answer should have a body.
            if len( body ) == 0:
                self.add_error( "body", _( "You should provide a body to your answer." ) )

            if parent is None or parent.post_type.id != settings.QA_POST_TYPE_QUESTION_ID:
                self.add_error( "parent", _( "You should provide a QUESTION parent to your answer." ) )
        
        elif post_type.id == settings.QA_POST_TYPE_QUESTION_ID:
            # A question should have a title.
            if len( title ) == 0:
                self.add_error( "title", _( "You should provide a title to your question." ) )
        
        elif post_type.id == settings.QA_POST_TYPE_BLOGPOST_ID:
            # A blog post shoud have a title and a body.
            if len( title ) == 0:
                self.add_error( "title", _( "You should provide a title to your post." ) )
            if len( body ) == 0:
                self.add_error( "body", _( "You should provide a body to your post." ) )
            if is_anonymous:
                self.add_error( "is_anonymous", _( "A Blog Post can not be anonymous." ) )
        
        elif post_type.id == settings.QA_POST_TYPE_COMMENT_ID:
            # A comment should have a body
            if len( body ) == 0:
                self.add_error( "body", _( "You should provide a body to your comment." ) )
            # A comment should have a parent.
            if parent is None:
                self.add_error( "parent", _( "You should provide a parent to your comment." ) )
        
        else:
            # Nothing valid was received on the form. Invalidate the post type field.
            self.add_error( "post_type", _( "Please provide a valid post type." ) )

        # Return cleaned data
        return cleaned_data
        

    def save( self, commit = True ):
        instance = super( PostForm, self ).save( commit = False )
        instance.last_activity_date = timezone.now()
        
        if commit:
            instance.save()
            for topic in self.cleaned_data['related_topics']:
                instance.related_topics.add( topic )

        return instance



class EditPostForm( BaseModelForm ):
    """
    Form to edit qa post on admin.
    """
    
    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = Post
        fields = [ "title", "body", "is_anonymous", "related_topics" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):
        super( PostForm, self ).__init__( *args, **kwargs )

        # Overrides the choices to the related_topics field.
        self.fields[ "related_topics" ].choices = Topic.objects.values_list( "id", "name" )
        self.fields[ "related_topics" ].required = True

"""
    def clean( self ):
        cleaned_data = super( PostForm, self ).clean()

        # Gets form stuffs
        title = cleaned_data.get( "title" )
        body = cleaned_data.get( "body" )
        is_anonymous = cleaned_data.get( "is_anonymous" )
        related_topics = cleaned_data.get( "related_topics" )

        # return cleaned data
        return cleaned_data
"""     

    def save( self, commit = True ):
        instance = super( EditPostForm, self )

        # Creates a post history with previous data
        history = PostHistory()
        history.original_post_id = instance.id
        history.title = instance.title
        history.body = instance.body
        history.written_date = instance.modified_date
        history.save()

        instance.last_activity_date = timezone.now()
        
        if commit:
            instance.save()
            instance.related_topics.clear()
            for topic in self.cleaned_data['related_topics']:
                instance.related_topics.add( topic )

        return instance
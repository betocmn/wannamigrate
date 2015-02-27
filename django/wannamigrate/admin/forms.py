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
from django.db import transaction


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
class AddPostForm( BaseModelForm ):
    """
    Form to create a Question or a BlogPost.
    """
    
    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = Post
        fields = [ "post_type", "owner", "title", "body", "is_anonymous", "related_topics" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):
        super( AddPostForm, self ).__init__( *args, **kwargs )

        # Overrides the choices to the post_type field.
        self.fields[ "post_type" ].choices = PostType.objects.filter( id__in = [ settings.QA_POST_TYPE_BLOGPOST_ID, settings.QA_POST_TYPE_QUESTION_ID ] ).values_list( "id", "name" )

        # Overrides the choices to the related_topics field.
        self.fields[ "related_topics" ].choices = Topic.objects.values_list( "id", "name" )
        self.fields[ "related_topics" ].required = True

        # Overrides the id of the widget for the owner
        self.fields[ "owner" ].widget.attrs['id'] = "owner_id"


    def save( self, commit = True ):
        """
            Saves the post info taking care of add the related topics to it. 
            :param: commit Indicates wether to save the model or not
        """
        with transaction.atomic():
            instance = super( AddPostForm, self ).save( commit = False )
            instance.last_activity_date = timezone.now()
            
            if commit:
                instance.save()
                for topic in self.cleaned_data['related_topics']:
                    instance.related_topics.add( topic )

            return instance



class AddAnswerForm( BaseModelForm ):
    """
        Form to create an Answer or a Comment.
    """
    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = Post
        fields = [ "owner", "body", "is_anonymous", "parent", "post_type" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):

        # Removes the parent param from kwargs.
        parent = kwargs.pop( "parent" )

        # Defines which post_type I should use according to parent's type.
        if parent.post_type.id == settings.QA_POST_TYPE_QUESTION_ID:
            post_type = PostType.objects.get( pk = settings.QA_POST_TYPE_ANSWER_ID )
        elif parent.post_type.id in [ settings.QA_POST_TYPE_BLOGPOST_ID, settings.QA_POST_TYPE_ANSWER_ID ]:
            post_type = PostType.objects.get( pk = settings.QA_POST_TYPE_COMMENT_ID )
        else:
            raise ValidationError( "Cannot add an answer to a comment." )

        
        # Initialize data
        super( AddAnswerForm, self ).__init__( *args, **kwargs )

        # Sets the parent field to a hidden input and sets its value.
        self.fields[ "parent" ].widget = forms.HiddenInput()
        self.fields[ "parent" ].initial = parent

        # Sets the post_type field to a hidden input and sets its value.
        self.fields[ "post_type" ].widget = forms.HiddenInput()
        self.fields[ "post_type" ].initial = post_type

        # Sets the ID of the owner field widget.
        self.fields[ "owner" ].widget.attrs['id'] = "owner_id"



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
        super( EditPostForm, self ).__init__( *args, **kwargs )

        # Overrides the choices to the related_topics field.
        self.fields[ "related_topics" ].choices = Topic.objects.values_list( "id", "name" )
        self.fields[ "related_topics" ].required = True


    def save( self, commit = True ):
        with transaction.atomic():
            instance = super( EditPostForm, self ).save( commit = False )
            previous_data = Post.objects.get( pk = instance.id )

            if commit:

                # Verifies if the title or body changed to create a post history.
                if previous_data.title != instance.title or previous_data.body != instance.body:
                    # Creates a post history with previous data
                    history = PostHistory()
                    history.original_post_id = previous_data.id
                    history.title = previous_data.title
                    history.body = previous_data.body
                    # As a PostHistory will always be created when the post be edited(modified),
                    # the modified date represents the date of creation of the post edition.
                    history.written_date = previous_data.modified_date
                    history.save()
                
                instance.last_activity_date = timezone.now()
                instance.save()
                instance.related_topics.clear()
                for topic in self.cleaned_data['related_topics']:
                    instance.related_topics.add( topic )

            return instance


# Topics
class AddTopicForm( BaseModelForm ):
    """
    Form to create or edit a Topic.
    """
    
    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = Topic
        fields = [ "name" ]
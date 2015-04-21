"""
QA FORMS

Here you can include base forms that will be used as parents of application
forms.

Also you can create custom form fields or methods

"""

##########################
# Imports
##########################
from django.forms import TextInput, SelectMultiple, HiddenInput, Select, ModelMultipleChoiceField, ModelChoiceField
from wannamigrate.core.forms import BaseForm, BaseModelForm
from wannamigrate.qa.models import Post, PostType, Topic, PostHistory
from django.conf import settings
from django.utils import timezone
from django.db import transaction
from django.utils.translation import ugettext as _
from wannamigrate.core.models import User




###################################
# Q&A Forms
###################################
class AddQuestionForm( BaseModelForm ):
    """
    Form to create a Question on qa site.
    """

    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = Post
        fields = [ "title", "is_anonymous", "related_topics" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):

        # Extracts arguments from kwargs
        owner = kwargs.pop( "owner" )

        # Calls the constructor
        super( AddQuestionForm, self ).__init__( *args, **kwargs )

        # Initialize pre-defined data.
        self.instance.post_type = PostType.objects.get( pk = settings.QA_POST_TYPE_QUESTION_ID )
        self.instance.owner = owner

        # Overrides the choices to the related_topics field.
        self.fields[ "related_topics" ].choices = Topic.objects.values_list( "id", "name" )
        self.fields[ "related_topics" ].required = True
        self.fields[ "is_anonymous" ].widget.attrs[ "class" ] = "checkbox"





    def save( self, commit = True ):
        """
            Saves the post info taking care of add the related topics to it.
            :param: commit Indicates wether to save the model or not
        """
        with transaction.atomic():
            instance = super( AddQuestionForm, self ).save( commit = False )
            # instance.post_type__id = settings.QA_POST_TYPE_QUESTION_ID

            # TODO: Set the type and the owner of the post

            instance.last_activity_date = timezone.now()

            if commit:
                instance.save()
                for topic in self.cleaned_data['related_topics']:
                    instance.related_topics.add( topic )

            return instance



class AddAnswerForm( BaseModelForm ):
    """
    Form to create a Answer on qa site.
    """

    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = Post
        fields = [ "body", "is_anonymous" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):

        # Extracts arguments from kwargs
        owner = kwargs.pop( "owner" )

        # Calls the constructor
        super( AddAnswerForm, self ).__init__( *args, **kwargs )

        # Initialize pre-defined data.
        self.instance.post_type = PostType.objects.get( pk = settings.QA_POST_TYPE_ANSWER_ID )
        self.instance.owner = owner

        # Overrides the IS_ANONYMOUS widget
        self.fields[ "is_anonymous" ].widget.attrs[ "class" ] = "checkbox"
        self.fields[ "body" ].widget.attrs[ "class" ] = "text-coments"
        self.fields[ "body" ].widget.attrs[ "placeholder" ] = _( "Write your answer" ) + "..."


    def save( self, commit = True ):
        """
            Saves the post info taking care of add the related topics to it.
            :param: commit Indicates wether to save the model or not
        """
        with transaction.atomic():
            instance = super( AddQuestionForm, self ).save( commit = False )
            instance.parent.last_activity_date = timezone.now()

            if commit:
                instance.save()
                instance.parent.save()

            return instance

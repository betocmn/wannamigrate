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
from wannamigrate.qa.models import Question, Topic, Answer
from django.conf import settings
from django.utils import timezone
from django.db import transaction
from django.utils.translation import ugettext as _
from wannamigrate.core.models import User
from wannamigrate.qa.wm_editor import WMEditorParser



###################################
# Q&A Forms
###################################
class AddQuestionForm( BaseModelForm ):
    """
    Form to create a Question on qa site.
    """

    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = Question
        fields = [ "title", "is_anonymous", "related_topics" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):

        # Extracts arguments from kwargs
        owner = kwargs.pop( "owner" )

        # Calls the constructor
        super( AddQuestionForm, self ).__init__( *args, **kwargs )

        # Initialize pre-defined data.
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
            if commit:
                instance = super( AddQuestionForm, self ).save()
                for topic in self.cleaned_data['related_topics']:
                    instance.related_topics.add( topic )

            return instance



class AddAnswerForm( BaseModelForm ):
    """
    Form to create a Answer on qa site.
    """

    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = Answer
        fields = [ "body", "is_anonymous" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):

        # Extracts arguments from kwargs
        owner = kwargs.pop( "owner" )
        question = kwargs.pop( "question" )

        # Calls the constructor
        super( AddAnswerForm, self ).__init__( *args, **kwargs )

        # Initialize pre-defined data.
        self.instance.owner = owner
        self.instance.question = question

        # Overrides the IS_ANONYMOUS widget
        self.fields[ "is_anonymous" ].widget.attrs[ "class" ] = "checkbox"
        self.fields[ "body" ].widget.attrs[ "class" ] = "text-coments"
        self.fields[ "body" ].widget.attrs[ "placeholder" ] = _( "Write your answer" ) + "..."

    def clean( self, *args, **kwargs ):
        cleaned_data = super( AddAnswerForm, self ).clean( *args, **kwargs )

        if "body" in cleaned_data:
            body = cleaned_data[ 'body' ]

            parser = WMEditorParser( convert_charrefs = True )
            parser.feed( body )
            parser.close()

            if not parser.is_valid():
                parser_errors = parser.get_errors()
                for e in parser_errors:
                    self.add_error( 'body', e )

        return cleaned_data
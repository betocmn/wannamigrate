"""
QA FORMS

Here you can include base forms that will be used as parents of application
forms.

Also you can create custom form fields or methods

"""

##########################
# Imports
##########################
from django import forms
from wannamigrate.core.models import Country
from wannamigrate.core.forms import BaseForm, BaseModelForm
from wannamigrate.qa.models import Question, BlogPost, Topic, Answer, TopicTranslation
from django.conf import settings
from django.utils import timezone
from django.db import transaction
from django.utils.translation import ugettext as _
from wannamigrate.core.models import User, Language
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
        fields = [ "title", "is_anonymous", "related_topics", "language" ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):
        # Extracts the owner from args
        owner = kwargs.pop( "owner" )
        # Extracts the language from args
        language = kwargs.pop( "language" )

        # Calls the constructor
        super( AddQuestionForm, self ).__init__( *args, **kwargs )

        # Overrides the choices to the related_topics field.
        self.fields[ "title" ].widget = forms.Textarea()
        self.fields[ "title" ].widget.attrs[ "placeholder" ] = _( "Type your question here..." )

        # Get topics relative to the language passed.
        self.fields[ "related_topics" ].choices = TopicTranslation.objects.filter( language = language ).values_list( "topic_id", "name" )
        self.fields[ "related_topics" ].required = True
        self.fields[ "related_topics" ].widget.attrs[ "placeholder" ] = _( "Ex: Brazil, Canada, Student visa, Work visa, General immigration" ) + "..."
        # Set the class of the is_anonymous widget
        self.fields[ "is_anonymous" ].widget.attrs[ "class" ] = "checkbox"

        # Gets the languages options and translates them
        languages = Language.objects.filter( code__in = [ x[0] for x in settings.LANGUAGES ] ).values_list( "id", "name" )
        translated = [ ( x[0], _( x[1] ) ) for x in languages ]
        self.fields[ "language" ].choices = languages
        self.fields[ "language" ].widget.attrs[ "class" ] = "default-select"

        # Sets the owner of the question
        self.instance.owner = owner
        # Sets the default value for language field.
        self.initial[ "language" ] = language


    def clean( self, *args, **kwargs ):
        cleaned_data = super( AddQuestionForm, self ).clean( *args, **kwargs )

        # The user should select at least Canada or Australia as topic.
        if "related_topics" in cleaned_data:
            # country_topic_selected = Topic.objects.filter( id__in = cleaned_data[ "related_topics" ] ).exclude( country__isnull = True ).exists()
            immigration_enabled_countries = Country.objects.filter( immigration_enabled = True ).values_list( "id", flat = True )
            immigration_enabled_topic_selected = Topic.objects.filter( id__in = cleaned_data[ "related_topics" ], country__id__in = immigration_enabled_countries  ).exists()
            if not immigration_enabled_topic_selected:
                self.add_error( 'related_topics', _( "Select at least one country with immigration enabled as topic. Ex: Canada, Australia." ) )

        return cleaned_data

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


class AddBlogPostForm( BaseModelForm ):
    """
    Form to create a Question on qa site.
    """

    class Meta:
        """ Meta class describing the model and the fields required on this form. """
        model = BlogPost
        fields = [ "title", "body", "is_anonymous", "related_topics", "language"  ]

    # Initalizing the form
    def __init__( self, *args, **kwargs ):
        # Extracts the owner from args
        owner = kwargs.pop( "owner" )
        # Extracts the language from args
        language = kwargs.pop( "language" )

        # Calls the constructor
        super( AddBlogPostForm, self ).__init__( *args, **kwargs )

        # Overrides the choices to the related_topics field.
        self.fields[ "title" ].widget = forms.Textarea()
        self.fields[ "title" ].widget.attrs[ "placeholder" ] = _( "Ex: How to take your pet to Canada" ) + "..."
        self.fields[ "related_topics" ].choices = TopicTranslation.objects.filter( language = language ).values_list( "topic_id", "name" )
        self.fields[ "body" ].required = True
        self.fields[ "body" ].widget.attrs[ "placeholder" ] = _( "Ex: The first step is" ) + "..."
        self.fields[ "related_topics" ].required = True
        self.fields[ "related_topics" ].widget.attrs[ "placeholder" ] = _( "Ex: Brazil, Canada, Student visa, Work visa, General immigration" ) + "..."
        self.fields[ "is_anonymous" ].widget.attrs[ "class" ] = "checkbox"

        # Gets the languages options and translates them
        languages = Language.objects.filter( code__in = [ x[0] for x in settings.LANGUAGES ] ).values_list( "id", "name" )
        translated = [ ( x[0], _( x[1] ) ) for x in languages ]
        self.fields[ "language" ].choices = languages
        self.fields[ "language" ].widget.attrs[ "class" ] = "default-select"

        # Sets the owner of the question
        self.instance.owner = owner
        # Sets the default value for language field.
        self.initial[ "language" ] = language


    def clean( self, *args, **kwargs ):
        cleaned_data = super( AddBlogPostForm, self ).clean( *args, **kwargs )

        # The user should select one country as topic
        if "related_topics" in cleaned_data:
            country_topic_selected = Topic.objects.filter( id__in = cleaned_data[ "related_topics" ] ).exclude( country__isnull = True ).exists()
            if not country_topic_selected:
                self.add_error( 'related_topics', _( "Select at least one country as topic." ) )

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

    def save( self, commit = True ):
        """
            Saves the post info taking care of add the related topics to it.
            :param: commit Indicates wether to save the model or not
        """
        with transaction.atomic():
            if commit:
                instance = super( AddBlogPostForm, self ).save()
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
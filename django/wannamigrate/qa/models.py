"""
Questions and Answers model classes.


"""

####################
# Imports
####################
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from wannamigrate.core.models import BaseModel, User, Country, Goal, Language
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models import Prefetch, Count
from django.db import transaction
from django.utils import timezone
from django.template.defaultfilters import slugify
import itertools
import math



##########################
# Classes definitions
##########################
class BaseContent( BaseModel ):
    # The owner of the content.
    owner = models.ForeignKey( User )
    # The owner don't want to be visible.
    is_anonymous = models.BooleanField( default = False )

    # META CLASS.
    class Meta:
        abstract = True


class FavoritableContent( models.Model ):
    # The readers of this content.
    readers = models.ManyToManyField( User, related_name = "favourite_%(class)s" )
    # The total number of readers of this content.
    total_readers = models.PositiveIntegerField( default = 0 )

    # META CLASS.
    class Meta:
        abstract = True



class FollowableContent( models.Model ):
    # The followers of the content.
    followers = models.ManyToManyField( User, related_name = "following_%(class)s" )
    # The total number of followers of this content.
    total_followers = models.PositiveIntegerField( default = 0 )

    # META CLASS.
    class Meta:
        abstract = True


class IndexableContentManager( models.Manager ):
    def get_listing( self, *args, **kwargs ):
        # If you're seeing this errors, you should create a Custom Manager that inherits from
        # IndexableContentManager, override the method get_listing and also override the
        # objects manager on your IndexableContent model.
        raise Exception( "[IndexableContentManager] Abstract method not implemented." )



class QuestionsManager( IndexableContentManager ):
    def get_listing( self, *args, **kwargs ):
        # Extracts arguments
        related_topics_ids = kwargs.pop( "related_topics_ids", None )
        related_countries_ids = kwargs.pop( "related_countries_ids", None )  # The ids of the related countries
        related_goals_ids = kwargs.pop( "related_goals_ids", None )  # The ids of the related goals
        language_ids = kwargs.pop( "language_ids", None )

        # Apply filters
        if related_topics_ids:  # BY TOPIC
            self = self.filter( related_topics__in = related_topics_ids )
        if related_countries_ids:   # BY RELATED COUNTRIES
            self = self.filter( related_topics__country__id__in = related_countries_ids )
        if related_goals_ids:   # BY RELATED GOALS
            self = self.filter( related_topics__related_goals__id__in = related_goals_ids )
        if language_ids:    # BY LANGUAGE
            self = self.filter( language__in = language_ids )


        self = self.prefetch_related(
            "related_topics",
            Prefetch(
                "answers",
                queryset=Answer.objects.order_by( "-total_upvotes", "total_downvotes", "-created_date" )
            ),
        )

        return self.distinct().order_by( '-last_activity_date' )



class BlogPostsManager( IndexableContentManager ):
    def get_listing( self, *args, **kwargs ):
        # Extracts arguments
        related_topics_ids = kwargs.pop( "related_topics_ids", None )
        related_countries_ids = kwargs.pop( "related_countries_ids", None )  # The ids of the related countries
        related_goals_ids = kwargs.pop( "related_goals_ids", None )  # The ids of the related goals
        language_ids = kwargs.pop( "language_ids", None )

        # Apply filters
        if related_topics_ids:  # BY TOPIC
            self = self.filter( related_topics__in = related_topics_ids )
        if related_countries_ids:   # BY RELATED COUNTRIES
            self = self.filter( related_topics__country__id__in = related_countries_ids )
        if related_goals_ids:   # BY RELATED GOALS
            self = self.filter( related_topics__related_goals__id__in = related_goals_ids )
        if language_ids:    # BY LANGUAGE
            self = self.filter( language__in = language_ids )


        self = self.prefetch_related(
            "related_topics", "owner",
        )

        return self.distinct().order_by( '-last_activity_date' )



class IndexableContent( models.Model ):
    # The title of the content.
    title = models.CharField( max_length = 200 )
    # The slug of the title
    slug = models.SlugField( max_length = 200, unique = True )
    # The body of the content.
    body = models.TextField( default = "" )
    # The language of the content
    language = models.ForeignKey( Language, related_name = "related_%(class)s" )
    # The last activity on the post (answer, edition, etc).
    last_activity_date = models.DateTimeField()
    # The topics related to this content.
    related_topics = models.ManyToManyField( "Topic", related_name = "related_%(class)s" )
    # The total number of views of this content.
    total_views = models.PositiveIntegerField( default = 0 )
    # Overrides the object's manager
    objects = IndexableContentManager()

    # META CLASS.
    class Meta:
        abstract = True

    def generate_slug( self ):
        # Calculates the slug handling repetition
        max_length = self._meta.get_field( 'slug' ).max_length
        self.slug = orig = slugify( self.title )[:max_length]

        for x in itertools.count(1):
            if not self.__class__.objects.filter( slug = self.slug ).exists():
                break
            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            self.slug = "{0}-{1}".format( orig[ : max_length - len( str( x ) ) - 1 ], x )

    def save( self, *args, **kwargs ):

        # Sets the last activity date of the content
        if "update_lad" in kwargs:
            update_lad = kwargs.pop( "update_lad" )
            if update_lad is True:
                self.last_activity_date = timezone.now()
        else:
            self.last_activity_date = timezone.now()


        if not self.slug:
            self.generate_slug()

        super( IndexableContent, self ).save( *args, **kwargs )



class VotableContent( models.Model ):
    # The total number of upvotes of this content.
    total_upvotes = models.PositiveIntegerField( default = 0 )
    # The total number of downvotes of this content.
    total_downvotes = models.PositiveIntegerField( default = 0 )
    # The total number of reports of this content.
    total_reports = models.PositiveIntegerField( default = 0 )
    # The votes related to this content.
    votes = GenericRelation( "Vote" )

    # META CLASS.
    class Meta:
        abstract = True



class CommentableContent( models.Model ):
    # The total number of comments of this content.
    total_comments = models.PositiveIntegerField( default = 0 )
    # The comments related to this content.
    comments = GenericRelation( "Comment" )

    # META CLASS.
    class Meta:
        abstract = True


class BlogPost( BaseContent, IndexableContent, FollowableContent, VotableContent, CommentableContent ):
    # Overrides the object's manager
    objects = BlogPostsManager()

    # META CLASS
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_blogpost", "[ADMIN] Can add blogpost" ),
            ( "admin_edit_blogpost", "[ADMIN] Can edit blogpost" ),
            ( "admin_delete_blogpost", "[ADMIN] Can delete blogpost" ),
            ( "admin_view_blogpost", "[ADMIN] Can view blogpost" ),
            ( "admin_list_blogpost", "[ADMIN] Can list blogpost" ),
        )


class Question( BaseContent, IndexableContent, FollowableContent, VotableContent, CommentableContent ):
    # The total number of answers of this question.
    total_answers = models.PositiveIntegerField( default = 0 )
    # Overrides the object's manager
    objects = QuestionsManager()

    # META CLASS
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_question", "[ADMIN] Can add question" ),
            ( "admin_edit_question", "[ADMIN] Can edit question" ),
            ( "admin_delete_question", "[ADMIN] Can delete question" ),
            ( "admin_view_question", "[ADMIN] Can view question" ),
            ( "admin_list_question", "[ADMIN] Can list question" ),
        )


class QuestionHistory( BaseModel ):
    parent = models.ForeignKey( "Question", related_name = "edition_history" )
    title = models.CharField( max_length = 200 )
    body = models.TextField( default = "" )
    parent_created_date = models.DateTimeField()

    # META CLASS
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_question_history", "[ADMIN] Can add question history" ),
            ( "admin_edit_question_history", "[ADMIN] Can edit question history" ),
            ( "admin_delete_question_history", "[ADMIN] Can delete question history" ),
            ( "admin_view_question_history", "[ADMIN] Can view question history" ),
            ( "admin_list_question_history", "[ADMIN] Can list question history" ),
        )


class BlogPostHistory( BaseModel ):
    parent = models.ForeignKey( "BlogPost", related_name = "edition_history" )
    title = models.CharField( max_length = 200 )
    body = models.TextField( default = "" )
    parent_created_date = models.DateTimeField()

    # META CLASS
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_blogpost_history", "[ADMIN] Can add blogpost history" ),
            ( "admin_edit_blogpost_history", "[ADMIN] Can edit blogpost history" ),
            ( "admin_delete_blogpost_history", "[ADMIN] Can delete blogpost history" ),
            ( "admin_view_blogpost_history", "[ADMIN] Can view blogpost history" ),
            ( "admin_list_blogpost_history", "[ADMIN] Can list blogpost history" ),
        )

class Answer( BaseContent, VotableContent, CommentableContent  ):
    # votes, comments
    # The question that the answer belongs to.
    question = models.ForeignKey( "Question", related_name = "answers" )
    # The body of the answer.
    body = models.TextField( default = "" )
    
    # META CLASS
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_answer", "[ADMIN] Can add answer" ),
            ( "admin_edit_answer", "[ADMIN] Can edit answer" ),
            ( "admin_delete_answer", "[ADMIN] Can delete answer" ),
            ( "admin_view_answer", "[ADMIN] Can view answer" ),
            ( "admin_list_answer", "[ADMIN] Can list answer" ),
        )

    def save( self, *args, **kwargs ):
        with transaction.atomic():
            super( Answer, self ).save( *args, **kwargs )
            self.question.total_answers += 1
            self.question.last_activity_date = timezone.now()
            self.question.save()

    def delete( self, *args, **kwargs ):
        with transaction.atomic():
            super( Answer, self ).delete( *args, **kwargs )
            self.question.total_answers -= 1
            self.question.save()




class Comment( BaseContent, VotableContent, CommentableContent  ):
    # votes, comments
    # The body of the comment.
    body = models.TextField( default = "" )
    # The content that this comment belongs to.
    content_type = models.ForeignKey( ContentType, default = None )
    object_id = models.PositiveIntegerField( default = 0 )
    content_object = GenericForeignKey( 'content_type', 'object_id' )

    # META CLASS
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_comment", "[ADMIN] Can add comment" ),
            ( "admin_edit_comment", "[ADMIN] Can edit comment" ),
            ( "admin_delete_comment", "[ADMIN] Can delete comment" ),
            ( "admin_view_comment", "[ADMIN] Can view comment" ),
            ( "admin_list_comment", "[ADMIN] Can list comment" ),
        )



class TopicTranslation( BaseModel ):
    """
    A translation to a topic.
    """

    # The translated name of the topic
    name = models.CharField( max_length = 100 )
    # The translated slug of the title
    slug = models.SlugField( max_length = 100, unique = False )
    # The topic
    topic = models.ForeignKey( "Topic", related_name = "translations" )
    # The language
    language = models.ForeignKey( Language, related_name = "topics_translations" )

    # META Options: Sets the possible permissions required by this model.
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_topic_translation", "[ADMIN] Can add topic translation" ),
            ( "admin_edit_topic_translation", "[ADMIN] Can edit topic translation" ),
            ( "admin_delete_topic_translation", "[ADMIN] Can delete topic translation" ),
            ( "admin_view_topic_translation", "[ADMIN] Can view topic translation" ),
            ( "admin_list_topic_translation", "[ADMIN] Can list topic translation" ),
        )

    def save( self, *args, **kwargs ):
        if not self.slug:
            # Calculates the slug handling repetition
            max_length = self._meta.get_field( 'slug' ).max_length
            self.slug = orig = slugify( self.name )[:max_length]

            for x in itertools.count(1):
                if not self.__class__.objects.filter( slug = self.slug, language = self.language ).exists():
                    break
                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                self.slug = "{0}-{1}".format( orig[ : max_length - len( str( x ) ) - 1 ], x )

        super( TopicTranslation, self ).save( *args, **kwargs )


    def __str__(self):
        return self.name



class Topic( BaseModel ):
    """
    Topic class. This class represents topics.
    """

    # The name of the topic
    name = models.CharField( max_length = 100 )
    # The slug of the title
    slug = models.SlugField( max_length = 100, unique = True )
    # Users following this topic
    followers = models.ManyToManyField( User, related_name = "following_topics" )
    # The countries related to this topic
    country = models.ForeignKey( Country, related_name = "topic", null = True, blank = True )
    # The goals related to this topic
    related_goals = models.ManyToManyField( Goal, related_name = "related_topics", null = True, blank = True )

    # META Options: Sets the possible permissions required by this model.
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_topic", "[ADMIN] Can add topic" ),
            ( "admin_edit_topic", "[ADMIN] Can edit topic" ),
            ( "admin_delete_topic", "[ADMIN] Can delete topic" ),
            ( "admin_view_topic", "[ADMIN] Can view topic" ),
            ( "admin_list_topic", "[ADMIN] Can list topic" ),
        )

    def save( self, *args, **kwargs ):
        if not self.slug:
            # Calculates the slug handling repetition
            max_length = self._meta.get_field( 'slug' ).max_length
            self.slug = orig = slugify( self.name )[:max_length]

            for x in itertools.count(1):
                if not self.__class__.objects.filter( slug = self.slug ).exists():
                    break
                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                self.slug = "{0}-{1}".format( orig[ : max_length - len( str( x ) ) - 1 ], x )

        super( Topic, self ).save( *args, **kwargs )

    def __str__(self):
        return self.name




class Vote( BaseModel ):
    """
    Vote class. This class represents a vote.
    """
    # The user that voted.
    user = models.ForeignKey( User )
    # The type of this vote.
    vote_type = models.ForeignKey( "VoteType" )
    # The content that this vote belongs to.
    content_type = models.ForeignKey( ContentType, default = None )
    object_id = models.PositiveIntegerField( default = 0 )
    content_object = GenericForeignKey( 'content_type', 'object_id' )

    # META Options: Sets the possible permissions required by this model.
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_vote", "[ADMIN] Can add vote" ),
            ( "admin_edit_vote", "[ADMIN] Can edit vote" ),
            ( "admin_delete_vote", "[ADMIN] Can delete vote" ),
            ( "admin_view_vote", "[ADMIN] Can view vote" ),
            ( "admin_list_vote", "[ADMIN] Can list vote" ),
        )



class VoteType( BaseModel ):
    """
        Vote Type class. This class represents the type of a vote.
    """
    # The name of this Vote Type
    name = models.CharField( max_length = 255 )

    # META Options: Sets the possible permissions required by this model.
    class Meta:
        default_permissions = []    # Not listed

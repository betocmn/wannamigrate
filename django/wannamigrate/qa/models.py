"""
Questions and Answers model classes.


"""

####################
# Imports
####################
from django.db import models
from wannamigrate.core.models import (
    BaseModel, User, Country, Goal
)
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError
from wannamigrate.qa.wm_editor import WMEditorParser
from django.db.models import Prefetch, Count
import math



##########################
# Classes definitions
##########################
class Post( BaseModel ):
    """
    Post Class. This class can represent a question, an answer, a comment or an blog post. 
    """

    # The parent of this post (doesn't apply if it's a question or a blog post)
    parent = models.ForeignKey( "Post", null = True, related_name = "answers" )
    # The id of the owner of this post.
    owner = models.ForeignKey( User )
    # The type of this post.
    post_type = models.ForeignKey( "PostType" ) 
    # The title of this post (only apply to questions and blog posts)
    title = models.CharField( max_length = 255, default = "", blank = True )
    # The content of this post.
    body = models.TextField( default = "", blank = True )
    # Indicates if the post is anonymous or not.
    is_anonymous = models.BooleanField( default = False )
    # The number of upvotes of an answer
    upvotes_count = models.IntegerField( default = 0 )
    # The number of visualizations of this post
    views_count = models.PositiveIntegerField( default = 0 )
    # The number of answers to this post
    answers_count = models.PositiveIntegerField( default = 0 )
    # The number of visualizations of this post
    followers_count = models.PositiveIntegerField( default = 0 )
    # The date of the last acitivity on this post (new answers, editions, etc)
    last_activity_date = models.DateTimeField( null = True )
    # Users following this post
    followers = models.ManyToManyField( User, related_name = "following_posts" )
    # Users that added this post to their reading list.
    readers = models.ManyToManyField( User, related_name = "reading_list" )
    # The topics related to this post
    related_topics = models.ManyToManyField( "Topic", related_name = "related_posts" )

    # META Options: Sets the possible permissions required by this model.
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_post", "[ADMIN] Can add post" ),
            ( "admin_edit_post", "[ADMIN] Can edit post" ),
            ( "admin_delete_post", "[ADMIN] Can delete post" ),
            ( "admin_view_post", "[ADMIN] Can view post" ),
            ( "admin_list_post", "[ADMIN] Can list posts" ),
        )

    # Class methods
    def __str__( self ):
        return self.title if len( self.title ) else self.body

    def clean( self ):
        errors = {}
        

        # Post extra-validation
        if self.post_type.id == settings.QA_POST_TYPE_ANSWER_ID:
            # Checks if a valid parent was provided
            if self.parent is None or self.parent.post_type.id != settings.QA_POST_TYPE_QUESTION_ID:
                errors.setdefault( "parent", [] ).append( _( "You should provide a QUESTION parent to your answer." ) )

            # Instantiates the parser and feed with body content.
            wm_editor = WMEditorParser( convert_charrefs = True )    
            wm_editor.feed( self.body )
            wm_editor.close()

            # Clean the body content
            self.body = wm_editor.cleaned_data()    

            # Checks if a valid body was provided
            if not wm_editor.is_valid():
                errors.setdefault( "body", [] ).append( _( "Invalid markup. Try again." ) )
                
            if wm_editor.is_empty():
                errors.setdefault( "body", [] ).append( _( "You should provide a body to your answer." ) )
        
        elif self.post_type.id == settings.QA_POST_TYPE_QUESTION_ID:
            # A question should have a title.
            if len( self.title ) == 0:
                errors.setdefault( "title", [] ).append( _( "You should provide a title to your question." ) )
        
        elif self.post_type.id == settings.QA_POST_TYPE_BLOGPOST_ID:
            # A blog post shoud have a title and a body.
            if len( self.title ) == 0:
                errors.setdefault( "title", [] ).append( _( "You should provide a title to your post." ) )
            if self.is_anonymous:
                errors.setdefault( "is_anonymous", [] ).append( _( "A Blog Post can not be anonymous." ) )

            # Instantiates the parser and feed with body content.
            wm_editor = WMEditorParser( convert_charrefs = True )    
            wm_editor.feed( self.body )
            wm_editor.close()

            # Clean the body content
            self.body = wm_editor.cleaned_data()    

            # Checks if a valid body was provided
            if not wm_editor.is_valid():
                errors.setdefault( "body", [] ).append( _( "Invalid markup. Try again." ) )
                
            if wm_editor.is_empty():
                errors.setdefault( "body", [] ).append( _( "You should provide a body to your answer." ) )
            
        
        elif self.post_type.id == settings.QA_POST_TYPE_COMMENT_ID:
            # A comment should have a parent.
            if self.parent is None:
                errors.setdefault( "parent", [] ).append( _( "You should provide a parent to your comment." ) )

            # Instantiates the parser and feed with body content.
            wm_editor = WMEditorParser( convert_charrefs = True )    
            wm_editor.feed( self.body )
            wm_editor.close()

            # Clean the body content
            self.body = wm_editor.cleaned_data()    

            # Checks if a valid body was provided
            if not wm_editor.is_valid():
                errors.setdefault( "body", [] ).append( _( "Invalid markup. Try again." ) )
                
            if wm_editor.is_empty():
                errors.setdefault( "body", [] ).append( _( "You should provide a body to your answer." ) )

        else:
            # Nothing valid was received on the form. Invalidate the post type field.
            errors.setdefault( "post_type", [] ).append( _( "Please provide a valid post type." ) )

        if len( errors ) > 0:
            raise ValidationError( errors )

    # Static Methods
    @staticmethod
    def get_ranked( *args, post_type_id=None, related_countries_ids=None, related_goals_ids=None, results_per_step=5, **kwargs ):
        """
        Query used to search for posts sorted
        by relevance.  The relevance is calculated with
        the following:

        1- Related topics
        :param: args A list of named arguments to extract for ranking.
        :return: Post objects
        """

        # Extracts arguments
        topic_id = kwargs.pop( "topic_id", None )
        post_type_id = post_type_id
        related_countries_ids = related_countries_ids  # The ids of the related countries
        related_goals_ids = related_goals_ids  # The ids of the related goals
        results_per_step = results_per_step
        step = kwargs.pop( "step", 0 )



        limit_from = step * results_per_step
        limit_to = step * results_per_step + results_per_step


        posts = Post.objects

        # Filters by topic
        if ( topic_id ):
            posts = posts.filter( related_topics = topic_id )

        # Filters by situation
        if ( related_countries_ids ):
            posts = posts.filter( related_topics__related_countries__id__in = related_countries_ids )
        if ( related_goals_ids ):
            posts = posts.filter( related_topics__related_goals__id__in = related_goals_ids )

        posts = posts.prefetch_related( "related_topics",
            Prefetch(
                "answers",
                queryset=Post.objects.order_by( "-upvotes_count" )
            )
        )

        # Filters by post type
        if ( post_type_id ):
            posts = posts.filter(
                post_type__id = post_type_id
            )
        else:
            posts = posts.filter(
                post_type__id__in = [ settings.QA_POST_TYPE_BLOGPOST_ID, settings.QA_POST_TYPE_QUESTION_ID ],
            )


        return posts.distinct().order_by( '-last_activity_date' )[limit_from:limit_to].all()



class PostType( BaseModel ):
    """ 
    Post Type class. This class defines the types of a post. 
    """
    
    # The name of the post type
    name = models.CharField( max_length = 50 )

    # META Options: Sets the possible permissions required by this model.
    class Meta:
        default_permissions = []    # Not listed



class PostHistory( BaseModel ):
    """
    Post History class. It keeps the history of edition of the posts.
    """
    
    # The post that originated this post history.
    original_post = models.ForeignKey( "Post" )
    # The title of this post (only apply to questions and blog posts)
    title = models.CharField( max_length = 255, default = "", blank = True )
    # The content of this post.
    body = models.TextField( default = "", blank = True )
    # The date when the post was created
    written_date = models.DateTimeField()

    # META Options: Sets the possible permissions required by this model.
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_post_history", "[ADMIN] Can add post history" ),
            ( "admin_edit_post_history", "[ADMIN] Can edit post history" ),
            ( "admin_delete_post_history", "[ADMIN] Can delete post history" ),
            ( "admin_view_post_history", "[ADMIN] Can view post history" ),
            ( "admin_list_post_history", "[ADMIN] Can list post history" ),
        )



class Topic( BaseModel ):
    """
    Topic class. This class represents topics.
    """

    # The name of the topic
    name = models.CharField( max_length = 255 )
    # Users following this topic
    followers = models.ManyToManyField( User, related_name = "following_topics" )
    # The countries related to this topic
    related_countries = models.ManyToManyField( Country, related_name = "related_topics" )
    # The goals related to this topic
    related_goals = models.ManyToManyField( Goal, related_name = "related_topics" )

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



class Vote( BaseModel ):
    """
    Vote class. This class represents a vote.
    """

    # The post that this vote is related to.
    post = models.ForeignKey( "Post", related_name = "votes" )
    # The user that voted.
    user = models.ForeignKey( User )
    # The type of this vote.
    vote_type = models.ForeignKey( "VoteType" )

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

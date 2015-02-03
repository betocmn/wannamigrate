"""
Questions and Answers model classes.


"""

####################
# Imports
####################
from django.db import models
from wannamigrate.core.models import BaseModel
from wannamigrate.core.models import User
from django.utils.translation import ugettext_lazy as _



##########################
# Classes definitions
##########################
class Post( BaseModel ):
    """
    Post Class. This class can represent a question, an answer, a comment or an blog post. 
    """

    # The parent of this post (doesn't apply if it's a question or a blog post)
    parent = models.ForeignKey( "Post", null = True )
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
    # The number of visualizations of this post
    views_count = models.PositiveIntegerField( default = 0 )
    # The date of the last acitivity on this post (new answers, editions, etc)
    last_activity_date = models.DateTimeField()
    # Users following this post
    followers = models.ManyToManyField( User, related_name = "following_posts" )
    # Users that added this post to their reading list.
    readers = models.ManyToManyField( User, related_name = "reading_list" )
    # The topics related to this post
    related_topics = models.ManyToManyField( "Topic", related_name = "related_posts" )

class PostType( BaseModel ):
    """ 
    Post Type class. This class defines the types of a post. 
    """
    
    # The name of the post type
    name = models.CharField( max_length = 50 )



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
    # The date of the last acitivity on this post (new answers, editions, etc)
    written_date = models.DateTimeField()



class Topic( BaseModel ):
    """
    Topic class. This class represents topics.
    """

    # The name of the topic
    name = models.CharField( max_length = 255 )
    # Users following this topic
    followers = models.ManyToManyField( User, related_name = "following_topics" )



class Vote( BaseModel ):
    """
    Vote class. This class represents a vote.
    """

    # The post that this vote is related to.
    post = models.ForeignKey( "Post" )
    # The type of this vote.
    vote_type = models.ForeignKey( "VoteType" )



class VoteType( BaseModel ):
    """
        Vote Type class. This class represents the type of a vote.
    """

    # The name of this Vote Type
    name = models.CharField( max_length = 255 )

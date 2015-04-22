"""
URLs for QA app

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.qa import views
from django.conf import settings





##########################
# URL Patterns
##########################
urlpatterns = patterns('',
    # Posts
    url( r'^knowledge', views.list_posts, name = "list_posts" ),
    url( r'^posts$', views.list_posts, { "post_type_id" : settings.QA_POST_TYPE_BLOGPOST_ID }, name = "list_blogposts" ),
    url( r'^questions$', views.list_posts, { "post_type_id" : settings.QA_POST_TYPE_QUESTION_ID }, name = "list_questions" ),
    url( r'^question/add$', views.add_question, name = "add_question" ),
    url( r'^post/view/(?P<post_id>\d+)', views.view_post, name = "view_post" ),

    # Topics
    url( r'^topics/', views.list_topics, name = "list_topics" ),
    url( r'^browse_topic/(?P<topic_id>\d+)', views.list_posts, name = "browse_topic" ),


    # AJAX URL's
    url( r'^x/post/follow/(?P<post_id>\d+)', views.set_following_post, { "follow" : True }, name = "ajax_follow_post" ),
    url( r'^x/post/unfollow/(?P<post_id>\d+)', views.set_following_post, { "follow" : False }, name = "ajax_unfollow_post" ),
    url( r'^x/post/upvote/(?P<post_id>\d+)', views.set_upvote_post, { "upvote" : True }, name = "ajax_upvote_post" ),
    url( r'^x/post/downvote/(?P<post_id>\d+)', views.set_upvote_post, { "upvote" : False }, name = "ajax_downvote_post" ),



)
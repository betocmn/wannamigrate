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
from wannamigrate.qa.models import Question, BlogPost




##########################
# URL Patterns
##########################
urlpatterns = patterns('',
    # Posts
    url( r'^knowledge', views.list_posts, name = "list_posts" ),
    url( r'^posts$', views.list_posts, { "post_type_id" : settings.QA_POST_TYPE_BLOGPOST_ID }, name = "list_blogposts" ),
    url( r'^questions$', views.list_questions, name = "list_questions" ),
    url( r'^add/question$', views.add_question, name = "add_question" ),
    url( r'^question/(?P<slug>[-\w]+)/$', views.view_question, name = "view_question" ),
    url( r'^post/view/(?P<post_id>\d+)', views.view_post, name = "view_post" ),

    # Topics
    url( r'^topics/', views.list_topics, name = "list_topics" ),
    url( r'^browse_topic/(?P<topic_id>\d+)', views.list_posts, name = "browse_topic" ),


    # AJAX URL's
    # Follow / Unfollow
    url( r'^x/follow/question/(?P<slug>[-\w]+)/$', views.follow, { "followable_instance" : Question }, name = "ajax_follow_question" ),
    url( r'^x/unfollow/question/(?P<slug>[-\w]+)/$', views.unfollow, { "followable_instance" : Question }, name = "ajax_unfollow_question" ),
    url( r'^x/follow/blogpost/(?P<slug>[-\w]+)/$', views.follow, { "followable_instance" : BlogPost }, name = "ajax_follow_blogpost" ),
    url( r'^x/unfollow/blogpost/(?P<slug>[-\w]+)/$', views.unfollow, { "followable_instance" : BlogPost }, name = "ajax_unfollow_blogpost" ),

    # Load More
    url( r'^x/load/questions/$', views.ajax_load_questions, name = "ajax_load_questions" ),


    url( r'^x/post/follow/(?P<post_id>\d+)', views.set_following_post, { "follow" : True }, name = "ajax_follow_post" ),
    url( r'^x/post/unfollow/(?P<post_id>\d+)', views.set_following_post, { "follow" : False }, name = "ajax_unfollow_post" ),
    url( r'^x/post/upvote/(?P<post_id>\d+)', views.set_upvote_post, { "upvote" : True }, name = "ajax_upvote_post" ),
    url( r'^x/post/downvote/(?P<post_id>\d+)', views.set_upvote_post, { "upvote" : False }, name = "ajax_downvote_post" ),
    url( r'^x/get_topics', views.ajax_get_topics, name = "ajax_get_topics" ),
    url( r'^x/topic/follow/(?P<topic_id>\d+)', views.ajax_set_following_topic, { "follow" : True }, name = "ajax_follow_topic" ),
    url( r'^x/topic/unfollow/(?P<topic_id>\d+)', views.ajax_set_following_topic, { "follow" : False }, name = "ajax_unfollow_topic" ),



)
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
from wannamigrate.qa.models import Question, BlogPost, Answer




##########################
# URL Patterns
##########################
urlpatterns = patterns('',
    # ALL
    url( r'^knowledge', views.list_all, name = "list_all" ),

    # Questions
    url( r'^questions$', views.list_questions, name = "list_questions" ),
    url( r'^add/question$', views.add_question, name = "add_question" ),
    url( r'^question/(?P<slug>[-\w]+)/$', views.view_question, name = "view_question" ),

    # Blogposts
    url( r'^blogposts', views.list_blogposts, name = "list_blogposts" ),
    url( r'^add/blogpost', views.add_blogpost, name = "add_blogpost" ),
    url( r'^blogpost/(?P<slug>[-\w]+)/$', views.view_blogpost, name = "view_blogpost" ),

    # Topics
    url( r'^topics/', views.list_topics, name = "list_topics" ),
    url( r'^topic/(?P<slug>[-\w]+)/$', views.view_topic, name = "view_topic" ),

    # AJAX Follow Content (Toggle)
    url( r'^x/follow/question/(?P<id>\d+)/$', views.ajax_toggle_follow_content, { "followable_instance" : Question }, name = "ajax_follow_question" ),
    url( r'^x/follow/blogpost/(?P<id>\d+)/$', views.ajax_toggle_follow_content, { "followable_instance" : BlogPost }, name = "ajax_follow_blogpost" ),

    # AJAX Upvote Content (Toggle)
    url( r'^x/upvote/question/(?P<id>\d+)/$', views.ajax_toggle_upvote_content, { "votable_instance" : Question }, name = "ajax_upvote_question" ),
    url( r'^x/upvote/blogpost/(?P<id>\d+)/$', views.ajax_toggle_upvote_content, { "votable_instance" : BlogPost }, name = "ajax_upvote_blogpost" ),
    url( r'^x/upvote/answer/(?P<id>\d+)/$', views.ajax_toggle_upvote_content, { "votable_instance" : Answer }, name = "ajax_upvote_answer" ),

    # AJAX Downvote Content (Toggle)
    url( r'^x/downvote/question/(?P<id>\d+)/$', views.ajax_toggle_downvote_content, { "votable_instance" : Question }, name = "ajax_downvote_question" ),
    url( r'^x/downvote/blogpost/(?P<id>\d+)/$', views.ajax_toggle_downvote_content, { "votable_instance" : BlogPost }, name = "ajax_downvote_blogpost" ),
    url( r'^x/downvote/answer/(?P<id>\d+)/$', views.ajax_toggle_downvote_content, { "votable_instance" : Answer }, name = "ajax_downvote_answer" ),

    # AJAX load questions
    url( r'^x/load/questions/$', views.ajax_load_questions, name = "ajax_load_questions" ),
    url( r'^x/load/blogposts/$', views.ajax_load_blogposts, name = "ajax_load_blogposts" ),
    url( r'^x/load/all/$', views.ajax_load_all, name = "ajax_load_all" ),


    url( r'^x/get/topics', views.ajax_get_topics, name = "ajax_get_topics" ),
    url( r'^x/topic/follow/(?P<topic_id>\d+)', views.ajax_follow_topic, name = "ajax_follow_topic" ),
    url( r'^x/topic/unfollow/(?P<topic_id>\d+)', views.ajax_unfollow_topic, name = "ajax_unfollow_topic" ),



)
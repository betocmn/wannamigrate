"""
URLs for QA app

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.qa.admin import views






##########################
# URL Patterns
##########################
urlpatterns = patterns('',

    # Questions
    url( r'^questions$', views.list_questions, name = "list_questions" ),
    url( r'^posts/add$', views.add_post, name = "add_post" ),
    url( r'^posts/answer/(?P<parent_id>\d+)$', views.add_answer, name = "add_answer" ),
    url( r'^view/question/(?P<id>\d+)$', views.view_question, name = "view_question" ),
    url( r'^edit/question/(?P<id>\d+)$', views.edit_question, name = "edit_question" ),
    url( r'^delete/question/(?P<id>\d+)$', views.delete_question, name = "delete_question" ),

    # BlogPosts
    url( r'^blogposts$', views.list_blogposts, name = "list_blogposts" ),
    url( r'^view/blogpost/(?P<id>\d+)$', views.view_blogpost, name = "view_blogpost" ),
    url( r'^edit/blogpost/(?P<id>\d+)$', views.edit_blogpost, name = "edit_blogpost" ),
    url( r'^delete/blogpost/(?P<id>\d+)$', views.delete_blogpost, name = "delete_blogpost" ),

    # Topics
    url( r'^topics$', views.list_topic, name = "list_topic" ),
    url( r'^topics/add$', views.add_topic, name = "add_topic" ),
    url( r'^topics/view/(?P<topic_id>\d+)$', views.view_topic, name = "view_topic" ),
    url( r'^topics/edit/(?P<topic_id>\d+)$', views.edit_topic, name = "edit_topic" ),
    url( r'^topics/delete/(?P<topic_id>\d+)$', views.delete_topic, name = "delete_topic" ),

    # Topics Translations
    url( r'^topics_translations$', views.list_topic_translation, name = "list_topic_translation" ),
    url( r'^topic_translation/add$', views.add_topic_translation, name = "add_topic_translation" ),
    url( r'^topic_translation/add/(?P<topic_id>\d+)$', views.add_topic_translation, name = "add_topic_translation" ),
    url( r'^topic_translation/view/(?P<id>\d+)$', views.view_topic_translation, name = "view_topic_translation" ),
    url( r'^topic_translation/edit/(?P<id>\d+)$', views.edit_topic_translation, name = "edit_topic_translation" ),
    url( r'^topic_translation/delete/(?P<id>\d+)$', views.delete_topic_translation, name = "delete_topic_translation" ),

)
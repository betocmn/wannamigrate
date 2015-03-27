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
    url( r'^post/view/(?P<post_id>\d)', views.view_post, name = "view_post" ),


)
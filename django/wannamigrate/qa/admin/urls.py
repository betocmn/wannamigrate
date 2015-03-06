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

    # Posts
    url( r'^posts$', views.list_post, name = "list_post" ),
    url( r'^posts/reported$', views.list_post, { "reported" : True }, name = "list_reported_post" ),
    url( r'^posts/add$', views.add_post, name = "add_post" ),
    url( r'^posts/answer/(?P<parent_id>\d+)$', views.add_answer, name = "add_answer" ),
    url( r'^posts/view/(?P<post_id>\d+)$', views.view_post, name = "view_post" ),
    url( r'^posts/edit/(?P<post_id>\d+)$', views.edit_post, name = "edit_post" ),
    url( r'^posts/delete/(?P<post_id>\d+)$', views.delete_post, name = "delete_post" ),

    # Topics
    url( r'^topics$', views.list_topic, name = "list_topic" ),
    url( r'^topics/add$', views.add_topic, name = "add_topic" ),
    url( r'^topics/view/(?P<topic_id>\d+)$', views.view_topic, name = "view_topic" ),
    url( r'^topics/edit/(?P<topic_id>\d+)$', views.edit_topic, name = "edit_topic" ),
    url( r'^topics/delete/(?P<topic_id>\d+)$', views.delete_topic, name = "delete_topic" ),

)
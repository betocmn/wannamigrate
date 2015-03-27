"""
URLs for QA app

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.qa import views





##########################
# URL Patterns
##########################
urlpatterns = patterns('',
    # Posts
    url( r'^posts$', views.list_posts, name = "list_posts" ),
    url( r'^question/add$', views.add_question, name = "add_question" ),
    url( r'^post/view/(?P<post_id>\d)', views.view_post, name = "view_post" ),


)
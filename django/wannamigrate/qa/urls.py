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
    url( r'^posts$', views.list_post, name = "list_post" ),


)
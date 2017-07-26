"""
URLs routes (mapping to actions on views)

https://docs.djangoproject.com/en/1.9/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import url
from . import views


##########################
# URL Patterns
##########################
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<chapter_slug>[-\w]+)/$', views.chapter_details, name='chapter_details'),

]

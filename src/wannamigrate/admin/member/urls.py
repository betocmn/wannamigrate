"""
URLs for admin app

https://docs.djangoproject.com/en/1.9/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import url, include
from . import views


##########################
# URL Patterns
##########################
urlpatterns = [

    url(r'^$', views.list, name='list'),
    url(r'^list_json/$', views.list_json, name='list_json'),
    url(r'^add/$', views.add, name='add'),
    url(r'^details/(?P<member_id>\d+)$', views.details, name='details'),
    url(r'^edit/(?P<member_id>\d+)$', views.edit, name='edit'),
    url(r'^delete/(?P<member_id>\d+)$', views.delete, name='delete'),
    url(r'^search_json/$', views.search_json, name='search_json'),

]

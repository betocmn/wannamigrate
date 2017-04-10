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

    url(r'^$', views.index, name='index'),
    url(r'^my_account/$', views.my_account, name='my_account'),
    url(r'^edit_my_account/$', views.edit_my_account, name='edit_my_account'),
    url(r'^logout/$', views.logout, name='logout'),

]

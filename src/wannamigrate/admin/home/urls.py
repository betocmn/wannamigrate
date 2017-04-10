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

    url(r'^$', views.index, namespace="home"),
    url(r'^restricted/$', views.restricted, namespace='restricted'),

]

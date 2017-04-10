"""
URLs routes (mapping to actions on views)

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

    url(r'^\/(?P<slug>[-\w]+)/$', views.take, name='take'),
    url(r'^\/(?P<slug>[-\w]+)/result/$', views.result, name='result'),

]

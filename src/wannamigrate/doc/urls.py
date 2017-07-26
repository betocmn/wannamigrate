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
    url(r'^download/(?P<doc_id>\d+)$', views.download, name='download'),

]

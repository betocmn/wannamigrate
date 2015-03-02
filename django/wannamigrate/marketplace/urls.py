"""
URLs for marketplace app

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.marketplace import views




##########################
# URL Patterns
##########################
urlpatterns = patterns('',

    # View professional details
    url( r'^professional/(?P<user_id>\d+)/(?P<name>[a-z_\-]+)$', views.view_professional, name='view_professional' ),

)
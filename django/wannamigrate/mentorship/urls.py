"""
URLs for mentorship app

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.mentorship import views




##########################
# URL Patterns
##########################
urlpatterns = patterns('',

    # Landing-Page
    url( r'^$', views.landing, name = 'landing' ),

    # About
    url( r'^about/$', views.about, name = 'about' ),

    # FAQ
    url( r'^faq/$', views.faq, name = 'faq' ),

    # APPLY
    url( r'^apply/$', views.apply, name = 'apply' ),

)
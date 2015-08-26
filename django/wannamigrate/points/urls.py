"""
URLs for points app

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.points import views




##########################
# URL Patterns
##########################
urlpatterns = patterns('',

    # Dashboard
    url( r'^$', views.dashboard, name = 'dashboard' ),

    # Edit User Data
    url( r'^edit_personal/$', views.edit_personal, name = 'edit_personal' ),
    url( r'^edit_language/$', views.edit_language, name = 'edit_language' ),
    url( r'^edit_education/$', views.edit_education, name = 'edit_education' ),
    url( r'^edit_work/$', views.edit_work, name = 'edit_work' ),
    url( r'^calculate_points/$', views.calculate_points, name = 'calculate_points' ),
    url( r'^occupations_html/$', views.get_occupations_html, name = 'get_occupations_html' ),

    # Help Pages
    url( r'^(?P<country_name>[a-z_\-]+)/situation/$', views.situation, name = 'situation' ),
    url( r'^(?P<country_name>[a-z_\-]+)/professional-help/$', views.professional_help, name = 'professional_help' ),

)
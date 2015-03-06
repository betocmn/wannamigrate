"""
URLs for ADMIN panel of POINTS app

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.points.admin import views






##########################
# URL Patterns
##########################
urlpatterns = patterns('',

    # Immigration Rules (Questions, answers and points)
    url( r'^immigration_rules/$', views.question_list, name='immigration_rules' ),
    url( r'^immigration_rules/json/$', views.question_list_json, name='immigration_rule_json' ),
    url( r'^immigration_rules/add/$', views.question_add, name='immigration_rule_add' ),
    url( r'^immigration_rules/details/(?P<question_id>\d+)$', views.question_details, name='immigration_rule_details' ),
    url( r'^immigration_rules/edit/(?P<question_id>\d+)$', views.question_edit, name='immigration_rule_edit' ),
    url( r'^immigration_rules/delete/(?P<question_id>\d+)$', views.question_delete, name='immigration_rule_delete' ),

    # Occupations
    url( r'^occupations/$', views.occupation_list, name='occupations' ),
    url( r'^occupations/json/$', views.occupation_list_json, name='occupation_json' ),
    url( r'^occupations/add/$', views.occupation_add, name='occupation_add' ),
    url( r'^occupations/details/(?P<occupation_id>\d+)$', views.occupation_details, name='occupation_details' ),
    url( r'^occupations/edit/(?P<occupation_id>\d+)$', views.occupation_edit, name='occupation_edit' ),
    url( r'^occupations/delete/(?P<occupation_id>\d+)$', views.occupation_delete, name='occupation_delete' ),

)
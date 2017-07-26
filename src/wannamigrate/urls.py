""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import include, url


##########################
# URL Patterns
##########################
# Include all desired apps that will have URLs
urlpatterns = [

    url(r'^admin', include('wannamigrate.admin.urls', namespace="admin")),
    url(r'^(?P<country_slug>[-\w]+)/quiz/', include('wannamigrate.quiz.urls', namespace="quiz")),
    url(r'^(?P<country_slug>[-\w]+)/stories/', include('wannamigrate.story.urls',
                                                       namespace="story")),
    url(r'^(?P<country_slug>[-\w]+)/guide/', include('wannamigrate.guide.urls', namespace="guide")),
    url(r'^(?P<country_slug>[-\w]+)/tasks/', include('wannamigrate.task.urls', namespace="task")),
    url(r'^(?P<country_slug>[-\w]+)/docs/', include('wannamigrate.doc.urls', namespace="doc")),
    url(r'^(?P<country_slug>[-\w]+)/discussion/', include('wannamigrate.discussion.urls',
                                                          namespace="discussion")),
    url(r'^', include('wannamigrate.landing.urls', namespace="landing")),
    url(r'^', include('wannamigrate.company.urls', namespace="company")),
    url(r'^', include('wannamigrate.order.urls', namespace="order")),
    url(r'^', include('wannamigrate.member.urls', namespace="member")),

]

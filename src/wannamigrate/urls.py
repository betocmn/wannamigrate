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
    url(r'^immigration-quiz', include('wannamigrate.quiz.urls', namespace="quiz")),
    url(r'^stories', include('wannamigrate.story.urls', namespace="story")),
    url(r'^guide', include('wannamigrate.guide.urls', namespace="guide")),
    url(r'^tasks', include('wannamigrate.task.urls', namespace="task")),
    url(r'^docs', include('wannamigrate.doc.urls', namespace="doc")),
    url(r'^', include('wannamigrate.landing.urls', namespace="landing")),
    url(r'^', include('wannamigrate.company.urls', namespace="company")),
    url(r'^', include('wannamigrate.order.urls', namespace="order")),
    url(r'^', include('wannamigrate.member.urls', namespace="member")),

]

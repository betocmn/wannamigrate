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

    url(r'^', include('wannamigrate.landing.urls', namespace="landing")),
    url(r'^', include('wannamigrate.member.urls', namespace="member")),

]

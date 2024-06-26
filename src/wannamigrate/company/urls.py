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

    url(r'^about/$', views.about, name='about'),
    url(r'^how-it-works/$', views.how_it_works, name='how_it_works'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^privacy/$', views.privacy, name='privacy'),

]

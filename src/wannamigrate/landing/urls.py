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

    # Home-Page
    url(r'^$', views.home, name='home'),

]

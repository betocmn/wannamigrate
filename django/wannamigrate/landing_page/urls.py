from django.conf.urls import patterns, url
from wannamigrate.landing_page import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
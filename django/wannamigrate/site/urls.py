from django.conf.urls import patterns, url
from wannamigrate.site import views

urlpatterns = patterns('',
   
    # Home and Login
    url( r'^$', views.home, name='home' ),
    url( r'^login/$', views.login, name='login' ),
    url( r'^logout/$', views.logout, name='logout' ),

    # Contact Us
    url( r'^contact/$', views.contact, name='contact' ),

     # Dashboard
    url( r'^dashboard/$', views.dashboard, name='dashboard' ),

)
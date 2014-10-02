from django.conf.urls import patterns, url
from wannamigrate.site import views

urlpatterns = patterns('',
   
    # Home, Login, Personal Data                    
    url( r'^$', views.home, name='home' ),
    url( r'^login/$', views.login, name='login' ),
    url( r'^logout/$', views.logout, name='logout' ),
    url( r'^contact/$', views.contact, name='contact' ),
    url( r'^dashboard/$', views.dashboard, name='dashboard' ),
    url( r'^facebook_auth/$', views.facebook_auth, name='facebook_auth' ),

)
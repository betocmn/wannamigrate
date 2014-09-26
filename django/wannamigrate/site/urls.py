from django.conf.urls import patterns, url
from wannamigrate.site import views

urlpatterns = patterns('',
   
    # Home, Login, Personal Data                    
    url( r'^$', views.home_index, name='home' ),
    url( r'^login/$', views.login, name='login' ),
    url( r'^logout/$', views.logout, name='logout' ),
    url( r'^contact/$', views.contact, name='contact' ),
    url( r'^linkedin_auth/$', views.linkedin_auth, name='linkedin_auth' ),
    url( r'^facebook_auth/$', views.facebook_auth, name='facebook_auth' ),

)
from django.conf.urls import patterns, url
from wannamigrate.site import views

urlpatterns = patterns('',
   
    # Home, Login, Personal Data                    
    url( r'^$', views.home_index, name='home' ),
    url( r'^login/$', views.login_index, name='login' ),
    url( r'^logout/$', views.login_logout, name='logout' ),
    url( r'^contact/$', views.contact, name='contact' ),

)
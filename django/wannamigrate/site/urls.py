from django.conf.urls import patterns, url
from wannamigrate.site import views

urlpatterns = patterns('',
   
    # Home and Login
    url( r'^$', views.home, name = 'home' ),
    url( r'^login/$', views.login, name = 'login' ),
    url( r'^signup/$', views.signup, name = 'signup' ),
    url( r'^logout/$', views.logout, name = 'logout' ),
    url( r'^recover_password/$', views.recover_password, name = 'recover_password' ),
    url( r'^reset_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.reset_password, name = 'reset_password' ),

    # How it Works
    url( r'^tour/$', views.tour, name = 'tour' ),

    # Contact Us
    url( r'^contact/$', views.contact, name = 'contact' ),

    # My Account
    url( r'^account/$', views.account, name = 'account' ),

     # Dashboard
    url( r'^dashboard/$', views.dashboard, name = 'dashboard' ),

)
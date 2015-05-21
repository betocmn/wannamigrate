"""
URLs for site app

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.site import views




##########################
# URL Patterns
##########################
urlpatterns = patterns('',
   
    # Home and Login
    url( r'^$', views.home, name = 'home' ),
    url( r'^((?P<static>static)?)$', views.home, name = 'home' ),
    url( r'^login/$', views.login, name = 'login' ),
    url( r'^signup/$', views.signup, name = 'signup' ),
    url( r'^logout/$', views.logout, name = 'logout' ),
    url( r'^recover_password/$', views.recover_password, name = 'recover_password' ),
    url( r'^reset_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.reset_password, name = 'reset_password' ),

    # Terms, Conditions and Privacy
    url( r'^terms/$', views.terms, name = 'terms' ),
    url( r'^privacy/$', views.privacy, name = 'privacy' ),

    # How it Works
    url( r'^tour/$', views.tour, name = 'tour' ),

    # Contact Us
    url( r'^contact/$', views.contact, name = 'contact' ),

    # My Account
    url( r'^view_account/$', views.view_account, name = 'view_account' ),
    url( r'^edit_account_info/$', views.edit_account_info, name = 'edit_account_info' ),
    url( r'^edit_account_password/$', views.edit_account_password, name = 'edit_account_password' ),
    url( r'^edit_account_avatar/$', views.edit_account_avatar, name = 'edit_account_avatar' ),

    # Dashboard
    url( r'^dashboard/$', views.dashboard, name = 'dashboard' ),

    # Set language
    url( r'^setlang/(?P<language_code>[a-z_\-]+)/$', views.setlang, name = 'setlang' ),    

    # Exceptions
    url( r'^not_supported/$', views.not_supported, name = 'not_supported' ),
    url( r'^maintenance/$', views.maintenance, name = 'maintenance' ),

)
from django.conf.urls import patterns, url
from wannamigrate.site import views

urlpatterns = patterns('',
   
    # Home and Login
    url( r'^$', views.home, name = 'home' ),
    url( r'^older-browsers$', views.home_older_browsers, name = 'home_older_browsers' ),
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
    url( r'^view_account/$', views.view_account, name = 'view_account' ),
    url( r'^edit_account/$', views.edit_account, name = 'edit_account' ),

    # Dashboard
    url( r'^dashboard/$', views.dashboard, name = 'dashboard' ),

    # Edit User Data
    url( r'^edit_personal/$', views.edit_personal, name = 'edit_personal' ),
    url( r'^edit_language/$', views.edit_language, name = 'edit_language' ),
    url( r'^edit_education/$', views.edit_education, name = 'edit_education' ),
    url( r'^edit_work/$', views.edit_work, name = 'edit_work' ),
    url( r'^calculate_points/$', views.calculate_points, name = 'calculate_points' ),
    url( r'^occupations_html/$', views.get_occupations_html, name = 'get_occupations_html' ),

    # Help Pages
    url( r'^(?P<country_name>[a-z_\-]+)/situation/$', views.situation, name = 'situation' ),
    url( r'^(?P<country_name>[a-z_\-]+)/visa-application/$', views.visa_application, name = 'visa_application' ),
    url( r'^(?P<country_name>[a-z_\-]+)/moving/$', views.moving, name = 'moving' ),

    # Set language
    url( r'^setlang/(?P<language_code>[a-z_\-]+)/$', views.setlang, name = 'setlang' ),    

)
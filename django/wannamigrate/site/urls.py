"""
URLs for site app

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.site import views
from django.conf import settings




##########################
# URL Patterns
##########################
urlpatterns = patterns('',
   
    # Home and Login
    url( r'^$', views.home, name = 'home' ),
    url( r'^login/$', views.login, name = 'login' ),
    url( r'^signup/$', views.signup, name = 'signup' ),
    url( r'^(?P<type>[a-z_\-]+)/signup/$', views.signup, name = 'signup' ),
    url( r'^logout/$', views.logout, name = 'logout' ),
    url( r'^recover_password/$', views.recover_password, name = 'recover_password' ),
    url( r'^reset_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.reset_password, name = 'reset_password' ),

    # Terms, Conditions and Privacy
    url( r'^terms/$', views.terms, name = 'terms' ),
    url( r'^privacy/$', views.privacy, name = 'privacy' ),

    # How it Works
    url( r'^how-it-works/$', views.how_it_works, name = 'how_it_works' ),

    # Service providers
    url( r'^service-providers/$', views.service_providers, name = 'service_providers' ),

    # Contact Us
    url( r'^contact/$', views.contact, name = 'contact' ),

    # Tools
    url( r'^tools/$', views.tools, name = 'tools' ),

    # My Account
    url( r'^account/$', views.account, name = 'account' ),
    url( r'^contracts/$', views.contracts, name = 'contracts' ),
    url( r'^edit_account/$', views.edit_account, name = 'edit_account' ),
    url( r'^edit_password/$', views.edit_password, name = 'edit_password' ),
    url( r'^upload_avatar/$', views.upload_avatar, name = 'upload_avatar' ),

    # Messages
    url( r'^start/conversation$', views.start_conversation, name = 'start_conversation' ),
    url( r'^conversation/(?P<id>\d+)/$', views.view_conversation, name = 'view_conversation' ),
    url( r'^conversations/$', views.list_conversations, name = 'list_conversations' ),
    url( r'^conversations/sent$', views.list_conversations, { "conversation_status" : settings.CORE_CONVERSATION_STATUS_OUTBOX_ID }, name = 'list_conversations_sent' ),
    url( r'^conversations/archive$', views.list_conversations, { "conversation_status" : settings.CORE_CONVERSATION_STATUS_ARCHIVE_ID }, name = 'list_conversations_archive' ),

    # Dashboard
    url( r'^dashboard/$', views.dashboard, name = 'dashboard' ),

    # Change Situation
    url( r'^change-situation/$', views.change_situation, name = 'change_situation' ),

    # Set language
    url( r'^set_lang/(?P<language_code>[a-z_\-]+)/$', views.set_lang, name = 'set_lang' ),

    # AJAX - List more posts
    url( r'^load/posts/', views.load_posts, name = "load_posts" ),
    #url( r'^load/posts/(?P<results_per_page>\d+)/(?P<page>\d+)/', views.load_posts, name = "load_posts" ),

)
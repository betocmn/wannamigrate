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
    url( r'^robots.txt$', views.robots, name = 'robots' ),
    url( r'^terms/$', views.terms, name = 'terms' ),
    url( r'^privacy/$', views.privacy, name = 'privacy' ),

    # How it Works
    url( r'^how-it-works/$', views.how_it_works, name = 'how_it_works' ),

    # Service providers
    url( r'^service-providers/$', views.service_providers, name = 'service_providers' ),

    # Contact Us
    url( r'^contact/$', views.contact, name = 'contact' ),

    # Guides (Step-by-step)
    url( r'^step-by-step/(?P<country_name>[a-z_\-]+)/$', views.guide, name = 'guide' ),

    # Premium
    url( r'^premium/$', views.premium, name = 'premium' ),
    url( r'^tools/$', views.tools, name = 'tools' ),

    # My Account
    url( r'^account/$', views.account, name = 'account' ),
    url( r'^notifications/$', views.notifications, name = 'notifications' ),
    url( r'^contracts/$', views.contracts, name = 'contracts' ),
    url( r'^edit_account/$', views.edit_account, name = 'edit_account' ),
    url( r'^edit_password/$', views.edit_password, name = 'edit_password' ),
    url( r'^upload_avatar/$', views.upload_avatar, name = 'upload_avatar' ),

    # Messages
    url( r'^start/conversation/(?P<to_user_slug>[-\w]+)/$', views.start_conversation, name = 'start_conversation' ),
    url( r'^conversation/(?P<id>\d+)/$', views.view_conversation, name = 'view_conversation' ),
    url( r'^conversations/$', views.list_conversations, { "conversation_status_id" : settings.CORE_CONVERSATION_STATUS_INBOX_ID }, name = 'list_conversations' ),
    url( r'^conversations/sent$', views.list_conversations, { "conversation_status_id" : settings.CORE_CONVERSATION_STATUS_OUTBOX_ID }, name = 'list_conversations_sent' ),
    url( r'^conversations/archive$', views.list_conversations, { "conversation_status_id" : settings.CORE_CONVERSATION_STATUS_ARCHIVE_ID }, name = 'list_conversations_archive' ),

    # Dashboard
    url( r'^site/dashboard/$', views.dashboard, name = 'dashboard' ),

    # Change Situation
    url( r'^change-situation/$', views.change_situation, name = 'change_situation' ),

    # Set language
    url( r'^set_lang/(?P<language_code>[a-z_\-]+)/$', views.set_lang, name = 'set_lang' ),

    # AJAX Notifications
    url( r'^x/consume/notifications/$', views.ajax_consume_notifications, name = "ajax_consume_notifications" ),

    # User's Profile
    url( r'^(?P<slug>[-\w]+)/$', views.user_profile, name = 'user_profile' ),

    # Profile ajax
    url( r'^x/follow/user/(?P<slug>[-\w]+)$', views.ajax_toggle_follow_user, name = "ajax_toggle_follow_user" ),
    url( r'^x/get/questions/(?P<slug>[-\w]+)$', views.ajax_get_user_questions, name = "ajax_get_user_questions" ),
    url( r'^x/get/posts/(?P<slug>[-\w]+)$', views.ajax_get_user_posts, name = "ajax_get_user_posts" ),
    url( r'^x/get/answers/(?P<slug>[-\w]+)$', views.ajax_get_user_answers, name = "ajax_get_user_answers" ),
    url( r'^x/get/followers/(?P<slug>[-\w]+)$', views.ajax_get_user_followers, name = "ajax_get_user_followers" ),
    url( r'^x/get/following/(?P<slug>[-\w]+)$', views.ajax_get_user_following, name = "ajax_get_user_following" ),
)
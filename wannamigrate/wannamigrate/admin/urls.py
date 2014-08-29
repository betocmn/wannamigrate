from django.conf.urls import patterns, url
from wannamigrate.admin import views

urlpatterns = patterns('',
   
    # Home, Login, Personal Data                    
    url( r'^$', views.home_index, name='home' ),
    url( r'^login/$', views.login_index, name='login' ),
    url( r'^logout/$', views.login_logout, name='logout' ),
    url( r'^my_account/$', views.login_my_account, name='my_account' ),
    url( r'^edit_my_account/$', views.login_edit_my_account, name='edit_my_account' ),
    
    # Admin Users
    url( r'^admin_users/$', views.admin_user_list, name='admin_users' ),
    url( r'^admin_users/json/$', views.admin_user_list_json, name='admin_user_json' ),
    url( r'^admin_users/add/$', views.admin_user_add, name='admin_user_add' ),
    url( r'^admin_users/details/(?P<user_id>\d+)$', views.admin_user_details, name='admin_user_details' ),
    url( r'^admin_users/edit/(?P<user_id>\d+)$', views.admin_user_edit, name='admin_user_edit' ),
    url( r'^admin_users/delete/(?P<user_id>\d+)$', views.admin_user_delete, name='admin_user_delete' ),
    
    # Groups
    url( r'^groups/$', views.group_list, name='groups' ),
    url( r'^groups/json/$', views.group_list_json, name='group_json' ),
    url( r'^groups/add/$', views.group_add, name='group_add' ),
    url( r'^groups/details/(?P<group_id>\d+)$', views.group_details, name='group_details' ),
    url( r'^groups/edit/(?P<group_id>\d+)$', views.group_edit, name='group_edit' ),
    url( r'^groups/delete/(?P<group_id>\d+)$', views.group_delete, name='group_delete' ),

)
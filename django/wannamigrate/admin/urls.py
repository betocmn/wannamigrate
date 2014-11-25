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

    # Immigration Rules (Questions, answers and points)
    url( r'^immigration_rules/$', views.question_list, name='immigration_rules' ),
    url( r'^immigration_rules/json/$', views.question_list_json, name='immigration_rule_json' ),
    url( r'^immigration_rules/add/$', views.question_add, name='immigration_rule_add' ),
    url( r'^immigration_rules/details/(?P<question_id>\d+)$', views.question_details, name='immigration_rule_details' ),
    url( r'^immigration_rules/edit/(?P<question_id>\d+)$', views.question_edit, name='immigration_rule_edit' ),
    url( r'^immigration_rules/delete/(?P<question_id>\d+)$', views.question_delete, name='immigration_rule_delete' ),
    
    # Occupations
    url( r'^occupations/$', views.occupation_list, name='occupations' ),
    url( r'^occupations/json/$', views.occupation_list_json, name='occupation_json' ),
    url( r'^occupations/add/$', views.occupation_add, name='occupation_add' ),
    url( r'^occupations/details/(?P<occupation_id>\d+)$', views.occupation_details, name='occupation_details' ),
    url( r'^occupations/edit/(?P<occupation_id>\d+)$', views.occupation_edit, name='occupation_edit' ),
    url( r'^occupations/delete/(?P<occupation_id>\d+)$', views.occupation_delete, name='occupation_delete' ),

)
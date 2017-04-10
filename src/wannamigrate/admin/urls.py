"""
URLs for admin app

https://docs.djangoproject.com/en/1.9/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import url, include
from wannamigrate.admin.home.views import index, restricted


##########################
# URL Patterns
##########################
urlpatterns = [

    # Admin Users
    url(r'^\/admin_users/', include('wannamigrate.admin.admin_user.urls',
                                    namespace="admin_user")),
    # Groups
    url(r'^\/groups/', include('wannamigrate.admin.group.urls', namespace="group")),

    # Home
    url(r'^$', index, name='home'),
    url(r'^\/$', index, name='home'),
    url(r'^\/restricted/$', restricted, name='restricted'),

    # Login / My Account
    url(r'^\/login/', include('wannamigrate.admin.login.urls', namespace="login")),

    # Members
    url(r'^\/members/', include('wannamigrate.admin.member.urls', namespace="member")),

    # Quiz
    url(r'^\/quiz/', include('wannamigrate.admin.quiz.urls', namespace="quiz")),


]

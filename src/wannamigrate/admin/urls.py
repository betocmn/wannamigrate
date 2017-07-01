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

    # Chapters
    url(r'^\/chapters/', include('wannamigrate.admin.chapter.urls', namespace="chapter")),

    # Documents
    url(r'^\/docs/', include('wannamigrate.admin.doc.urls', namespace="doc")),

    # Document Groups
    url(r'^\/doc_groups/', include('wannamigrate.admin.doc_group.urls', namespace="doc_group")),

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

    # Orders
    url(r'^\/orders/', include('wannamigrate.admin.order.urls', namespace="order")),

    # Posts
    url(r'^\/posts/', include('wannamigrate.admin.post.urls', namespace="post")),

    # Promo Codes
    url(r'^\/promo_codes/', include('wannamigrate.admin.promo_code.urls',
        namespace="promo_code")),

    # Quiz
    url(r'^\/quiz/', include('wannamigrate.admin.quiz.urls', namespace="quiz")),

    # Sections
    url(r'^\/sections/', include('wannamigrate.admin.section.urls', namespace="section")),

    # Subscriptions
    url(r'^\/subscriptions/', include('wannamigrate.admin.subscription.urls',
        namespace="subscription")),

]

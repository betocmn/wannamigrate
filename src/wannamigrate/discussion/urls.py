"""
URLs routes (mapping to actions on views)

https://docs.djangoproject.com/en/1.9/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import url
from . import views


##########################
# URL Patterns
##########################
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^update/$', views.update, name='update'),
    url(r'^update-reply/(?P<discussion_reply_id>\d+)/$', views.update_reply, name='update_reply'),
    url(r'^upvote/$', views.upvote, name='upvote'),
    url(r'^(?P<user_slug>[-\w]+)/$', views.thread, name='thread'),

]

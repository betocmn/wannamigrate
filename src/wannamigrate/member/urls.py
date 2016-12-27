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

    # Signup and Login
    url(r'^signup/$', views.signup, name='signup'),

    """
    url(r'^login/$', views.login, name='login'),
    url(r'^login-facebook/$', views.login_facebook, name='login_facebook'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^recover-password/$', views.recover_password, name='recover_password'),
    url(
        r'^reset-password/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.reset_password, name='reset_password'
    ),
    """

]

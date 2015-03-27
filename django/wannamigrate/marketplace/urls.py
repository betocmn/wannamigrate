"""
URLs for marketplace app

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.marketplace import views




##########################
# URL Patterns
##########################
urlpatterns = patterns('',

    # View professional details
    url( r'^(?P<user_id>\d+)/(?P<name>[a-z_\-]+)$', views.profile, name = 'profile' ),

    # List professionals
    url( r'^professionals/$', views.professionals, name = 'professionals' ),

    # Payment Page
    url( r'^payment/(?P<user_id>\d+)/(?P<service_type_id>\d+)$', views.payment, name = 'payment' ),

    # Order Confirmation Page
    url( r'^confirmation/(?P<order_id>\d+)$', views.confirmation, name = 'confirmation' ),


)
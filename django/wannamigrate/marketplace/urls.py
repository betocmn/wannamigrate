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
    url( r'^payment/$', views.payment, name = 'payment' ),

    # Order Confirmation Page
    url( r'^confirmation/$', views.confirmation, name = 'confirmation' ),

    # Download Order page
    url( r'^order/download/(?P<order_id_64>[0-9A-Za-z_\-]+)/(?P<user_id_64>[0-9A-Za-z_\-]+)/(?P<product_id_64>[0-9A-Za-z_\-]+)/(?P<external_code_64>[0-9A-Za-z_\-]+)/$', views.order_download, name = 'order_download' ),

)
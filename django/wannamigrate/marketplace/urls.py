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

    # E-books
    url( r'^ebooks/$', views.ebook, name = 'ebook' ),

    # Course IELTS
    url( r'^course/ielts/$', views.ielts, name = 'ielts' ),

    # International CV
    url( r'^international-cv/$', views.international_cv, name = 'international_cv' ),

    # Payment Page
    url( r'^payment/$', views.payment, name = 'payment' ),

    # Promo Discount (ajax)
    url( r'^promo_discount/$', views.get_promo_discount, name = 'get_promo_discount' ),

    # Order Confirmation Page
    url( r'^confirmation/$', views.confirmation, name = 'confirmation' ),

    # Update order status
    url( r'^payment_api_created/$', views.payment_api_created, name = 'payment_api_created' ),
    url( r'^payment_api_updated/$', views.payment_api_updated, name = 'payment_api_updated' ),

    # Download Order page
    url( r'^order/download/(?P<order_id_64>[0-9A-Za-z_\-]+)/(?P<user_id_64>[0-9A-Za-z_\-]+)/(?P<product_id_64>[0-9A-Za-z_\-]+)/(?P<external_code_64>[0-9A-Za-z_\-]+)/$', views.order_download, name = 'order_download' ),

)
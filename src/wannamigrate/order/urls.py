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

    # Home-Page
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^get-promo-info/$', views.get_promo_info, name='get_promo_info'),
    url(r'^process-payment/$', views.process_payment, name='process_payment'),
    url(r'^thank-you/$', views.thank_you, name='thank_you'),

]

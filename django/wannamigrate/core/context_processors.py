"""
Custom TEMPLATE CONTEXT PROCESSORS to be used by
https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS

If you need a global template variable (just like a constant) you can set the function here
and include on TEMPLATE_CONTEXT_PROCESSORS on settings.

"""

##########################
# Imports
##########################
from django.conf import settings





##########################
# Function definitions
##########################
def add_prod_setting( request ):
    return { 'is_prod': settings.IS_PROD }

def add_base_url( request ):
    protocol = 'https://' if request.is_secure else 'http://'
    url = protocol + request.get_host()
    return { 'base_url': url }
from django.conf import settings    

def add_prod_setting( request ):
    return { 'is_prod': settings.IS_PROD }
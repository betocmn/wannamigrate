"""
Base URLs for all apps

https://docs.djangoproject.com/en/1.7/topics/http/urls/
"""

##########################
# Imports
##########################
from django.conf.urls import url, patterns, include
from django.conf import settings
from django.conf.urls.static import static





##########################
# URL Patterns
##########################
# Include all desired apps that will have URLs
urlpatterns = patterns('',
    url( r'^admin/', include( 'wannamigrate.admin.urls', namespace = "admin" ) ),
    url( r'^', include( 'wannamigrate.site.urls', namespace = "site" ) ),
    url( r'^', include( 'wannamigrate.points.urls', namespace = "points" ) ),
    url( r'^', include( 'wannamigrate.marketplace.urls', namespace = "marketplace" ) ),
    url( '', include( 'social.apps.django_app.urls', namespace = "social" ) ),
) + static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )





##########################
# URLs USED BY DEBUG BAR
##########################
if settings.DEBUG:
    pass
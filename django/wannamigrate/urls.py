from django.conf.urls import url, patterns, include
from django.conf import settings
from django.conf.urls.static import static

# Include all desired apps that will have URLs
urlpatterns = patterns('',
    url( r'^admin/', include( 'wannamigrate.admin.urls', namespace = "admin" ) ),
    url( r'^', include( 'wannamigrate.site.urls', namespace = "site" ) ),
    url( '', include( 'social.apps.django_app.urls', namespace = "social" ) ),
) + static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )

# Used by the debug toolbar app
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url( r'^__debug__/', include( debug_toolbar.urls ) ),
    )

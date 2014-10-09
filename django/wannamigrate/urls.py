from django.conf.urls import url, patterns, include
from django.conf import settings

# Include all desired apps that will have URLs
urlpatterns = patterns('',
    url( r'^', include( 'wannamigrate.landing_page.urls', namespace = "landing_page" ) ),
    url( r'^admin/', include( 'wannamigrate.admin.urls', namespace = "admin" ) ),
    url( r'^site/', include( 'wannamigrate.site.urls', namespace = "site" ) ),
    url( '', include( 'social.apps.django_app.urls', namespace = "social" ) ),

)

# Used by the debug toolbar app
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url( r'^__debug__/', include( debug_toolbar.urls ) ),
    )

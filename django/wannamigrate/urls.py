from django.conf.urls import url, patterns, include
from django.conf import settings

urlpatterns = patterns('',
    url(r'^', include( 'wannamigrate.landing_page.urls', namespace="landing_page" ) ),
    url(r'^admin/', include( 'wannamigrate.admin.urls', namespace="admin" ) ),
    url(r'^site/', include( 'wannamigrate.site.urls', namespace="site" ) ),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

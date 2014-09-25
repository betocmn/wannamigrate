from django.conf.urls import url, patterns, include
from django.conf import settings

urlpatterns = patterns('',
    url(r'^', include( 'wannamigrate.landing_page.urls', namespace="landing_page" ) ),
    url(r'^admin/', include( 'wannamigrate.admin.urls', namespace="admin" ) ),
    url(r'^site/', include( 'wannamigrate.site.urls', namespace="site" ) ),

    # Facebook urls
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
)

#if settings.DEBUG:
    #import debug_toolbar
    #urlpatterns += patterns('',
        #url(r'^__debug__/', include(debug_toolbar.urls)),
   # )
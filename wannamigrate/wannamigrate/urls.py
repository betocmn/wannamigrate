from django.conf.urls import url, patterns, include
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include( 'wannamigrate.admin.urls', namespace="admin" ) ),
)

#if settings.DEBUG:
    #import debug_toolbar
    #urlpatterns += patterns('',
        #url(r'^__debug__/', include(debug_toolbar.urls)),
   # )
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wannamigrate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    # Redirects the / to the landing page app urls.
    url(r'^$', include( "wannamigrate.landing_page.urls" ) ),
)

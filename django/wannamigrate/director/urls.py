##########################
# Imports
##########################
from django.conf.urls import patterns, url
from wannamigrate.director import views





##########################
# URL Patterns
##########################
# Include all desired apps that will have URLs
urlpatterns = patterns( '',
    url( r'^director/$', views.dashboard, name = 'dashboard' ),
    url( r'^director/(?P<mission_hash>\w+)/(?P<objective_hash>\w+)/$', views.view, name = 'view' ),
)
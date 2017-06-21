"""
Applications configurations file.

Here you can change settings for app name, path, label, verbose_name, you can import
extra modules, etc...

Check documentation on: https://docs.djangoproject.com/en/1.9/ref/applications/
"""

##########################
# Imports
##########################
from django.apps import AppConfig


##########################
# Classes definitions
##########################
class GuideConfig(AppConfig):
 
    name = 'wannamigrate.guide'
    verbose_name = 'Guide'
 
    def ready(self):
 
        # imports signal handlers
        import wannamigrate.guide.signals

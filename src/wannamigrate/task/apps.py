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
class TaskConfig(AppConfig):
 
    name = 'wannamigrate.task'
    verbose_name = 'Task'
 
    def ready(self):
 
        # imports signal handlers
        import wannamigrate.task.signals

############################
# Imports
############################
from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os






# set the default Django settings module for the 'celery' program.
# We check if there' a local settings file, if so, we are in dev
BASE_DIR = os.path.dirname( __file__ )
settings_file_path = os.path.join( BASE_DIR, 'wannamigrate', '_settings', 'local.py' )
if os.path.isfile( settings_file_path ):
    settings_file = 'wannamigrate._settings.local'
else:
    settings_file = 'wannamigrate._settings.prod'
os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', settings_file )


app = Celery('wannamigrate')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
"""
With signal you can pretty much setup state actions before
or after some action occurs.

Django includes a “signal dispatcher” which helps allow
decoupled applications get notified when actions occur elsewhere in the framework

Read more on: https://docs.djangoproject.com/en/1.9/topics/signals/
"""

##########################
# Imports
##########################
import itertools
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save, post_save
from stdimage.utils import pre_delete_delete_callback, pre_save_delete_callback
from wannamigrate.quiz.models import QuizQuestion


##########################
# Signals setup
##########################
# StrImage (3rd party) signal do delete images (https://github.com/codingjoe/django-stdimage)
post_delete.connect(pre_delete_delete_callback, sender=QuizQuestion)
pre_save.connect(pre_save_delete_callback, sender=QuizQuestion)


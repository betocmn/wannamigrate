from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from stdimage.utils import pre_delete_delete_callback, pre_save_delete_callback
from wannamigrate.core.models import UserLoginHistory, UserPersonal


# StrImage (3rd party) signal do delete images (https://github.com/codingjoe/django-stdimage)
post_delete.connect( pre_delete_delete_callback, sender = UserPersonal )
pre_save.connect( pre_save_delete_callback, sender = UserPersonal )

@receiver( user_logged_in )
def register_login( sender, request, user, **kwargs ):
    """
    Saves user's login date in the database
    """
    user_login_history = UserLoginHistory()
    user_login_history.user = user
    user_login_history.is_logout = False
    user_login_history.save()

@receiver( user_logged_out )
def register_logout( sender, request, user, **kwargs ):
    """
    Saves user's logout date in the database
    """
    user_login_history = UserLoginHistory()
    user_login_history.user = user
    user_login_history.is_logout = True
    user_login_history.save()
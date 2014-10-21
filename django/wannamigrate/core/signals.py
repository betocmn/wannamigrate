from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from wannamigrate.core.models import UserLoginHistory

@receiver( user_logged_in )
def register_login( sender, request, user, **kwargs ):
    user_login_history = UserLoginHistory()
    user_login_history.user = user
    user_login_history.is_logout = False
    user_login_history.save()

@receiver( user_logged_out )
def register_logout( sender, request, user, **kwargs ):
    user_login_history = UserLoginHistory()
    user_login_history.user = user
    user_login_history.is_logout = True
    user_login_history.save()
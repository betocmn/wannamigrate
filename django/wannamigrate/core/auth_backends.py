"""
Custom AUTH Backend to enable the "Login as user"
Feature on Admin

"""
##########################
# Imports
##########################
from django.contrib.auth.models import User, check_password
from django.contrib.auth import get_user_model





##########################
# Class definitions
##########################
class AdminBackend( object ):
    """
    Authenticate against data

    Use the login name, and a hash of the password. For example:

    username = 'admin'
    password = 'sha1$4e987$afbcf42e21bd417fb71db8c66b321e9fc33051de'
    """

    def authenticate( self, username = None, password_hash = None, id = None, **kwargs ):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get( UserModel.USERNAME_FIELD )
        try:
            user = UserModel._default_manager.get_by_natural_key( username )
            if user.id == id and user.password == password_hash:
                return user
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password( password_hash )

    def get_user( self, user_id ):
        UserModel = get_user_model()
        try:
            return UserModel._default_manager.get( pk = user_id )
        except UserModel.DoesNotExist:
            return None
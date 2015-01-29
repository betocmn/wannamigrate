"""
This class is a command line for manage.py that will
take a file_path of a csv file with user emails and import
into the user database.
"""

##########################
# Imports
##########################
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from wannamigrate.core.forms import BaseForm, BaseModelForm
import csv





##########################
# Classes definitions
##########################
class UserForm( BaseModelForm ):
    """
    Form to ADD USERS
    """

    class Meta:
        model = get_user_model()
        fields = [ 'name', 'email' ]


    def save( self, commit = True ):
        """
        Save users

        :return: Dictionary
        """
        user = super( UserForm, self ).save( commit = False )
        user.is_admin = False
        user.is_active = True
        if not user.password:
            plain_password = get_user_model().objects.make_random_password()
            user.set_password( plain_password )
        if commit:
            user.save()
        return user



class Command( BaseCommand ):
    """
    Command class to run in the command line
    """

    args = '<file_name file_name ...>'
    help = 'Dumps csv values into users table'

    def handle( self, *args, **options ):

        users_created = 0
        for file_name in args:

            with open( file_name, newline = '' ) as csv_file:
                spam_reader = csv.reader( csv_file, dialect = 'excel' )

                for row in spam_reader:

                    # creates form with user information from this row
                    form_data = { 'name': '' }
                    form_data['email'] = row[0]
                    if len( row ) > 1 and row[1] is not None:
                        form_data['name'] = row[1]
                    form = UserForm( data = form_data )

                    # Validates it and saves it
                    if form.is_valid():
                        user = form.save()
                        users_created += 1

        # Return Success message
        self.stdout.write( str( users_created ) + ' user(s) created!' )
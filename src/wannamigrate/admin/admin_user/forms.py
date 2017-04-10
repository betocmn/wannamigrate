"""
Admin Users FORMS

Form definitions used by views/templates from this app
"""

##########################
# Imports
##########################
from django.contrib.auth import get_user_model
from django.forms import CharField, PasswordInput
from wannamigrate.core.forms import BaseModelForm


#######################
# ADMIN USERS
#######################
class AdminUserForm(BaseModelForm):
    """
    Form for ADD and EDIT ADMIN USERS
    """

    password = CharField(
        required=False, label="Password", widget=PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = get_user_model()
        fields = get_user_model().get_presentation_fields('raw')
        exclude = ['slug', 'is_admin', 'is_superuser', 'preferred_timezone', 'preferred_language']

    def save(self, commit=True):
        """
        If passwords are set, they need to be set on a different way

        :return: Dictionary
        """
        user = super(AdminUserForm, self).save(commit=False)
        user.is_admin = True
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
            user.groups = self.cleaned_data['groups']
        return user

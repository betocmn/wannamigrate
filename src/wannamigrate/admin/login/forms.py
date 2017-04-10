"""
Admin FORMS

Form definitions used by views/templates from the admin app
"""

##########################
# Imports
##########################
from django import forms
from django.contrib.auth import get_user_model
from wannamigrate.core.forms import (
    BaseForm, BaseModelForm
)


#######################
# LOGIN / LOGOUT / MY ACCOUNT
#######################
class LoginForm(BaseForm):
    """
    Form for LOGIN to ADMIN
    """
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )


class MyAccountForm(BaseModelForm):
    """
    Form for EDIT MY ACCOUNT
    """

    password = forms.CharField(
        required=False, label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(
        required=False, label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = get_user_model()
        fields = get_user_model().get_presentation_fields('raw')
        exclude = ['groups', 'slug', 'is_active', 'is_admin', 'is_superuser']

    def save(self, commit=True):
        """
        If passwords are set, they need to be set on a different way

        :return: Dictionary
        """
        user = super(MyAccountForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    def clean(self):
        """
        Extra validation for fields that depends on other fields

        :return: Dictionary
        """
        cleaned_data = super(MyAccountForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def get_fieldsets(self):
        """
        Overwrites default fieldsets

        :return: Dictionary
        """
        return [
            {
                'title': 'Account Settings',
                'fields': [
                    'name', 'email', 'preferred_language', 'preferred_timezone',
                    'password', 'confirm_password'
                ]
            }
        ]

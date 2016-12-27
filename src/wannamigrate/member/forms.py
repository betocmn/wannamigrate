"""
Product FORMS

Form definitions used by views/templates from the product app
"""

##########################
# Imports
##########################
from django.forms import (
    EmailField, CharField, PasswordInput, ValidationError,
    DateField, TextInput, EmailInput
)
from django.contrib.auth import get_user_model
from wannamigrate.core.forms import BaseForm
from wannamigrate.member.models import Member
from wannamigrate.core.util import get_object_or_false


#######################
# FORM Classes
#######################
class LoginForm(BaseForm):
    """
    Form for regular email/password login
    """
    login_email = EmailField(required=True, label="E-mail", widget=EmailInput(
        attrs={'placeholder': 'E-mail', 'class': 'form-control'}
    ))
    login_password = CharField(required=True, label="Password", widget=PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}
    ))


class PasswordRecoveryForm(BaseForm):
    """
    Form for RECOVER PASSWORD
    """
    email = EmailField(required=True, label="E-mail", widget=EmailInput(
        attrs={'placeholder': 'E-mail', 'class': 'form-control'}
    ))


class PasswordResetForm(BaseForm):
    """
    Form to set a new password

    """
    password = CharField(required=True, label="Password", widget=PasswordInput(
        attrs={'placeholder': 'New Password', 'class': 'form-control'}
    ))
    password_confirmation = CharField(required=True, label="Confirm Password", widget=PasswordInput(
        attrs={'placeholder': 'Confirm New Password', 'class': 'form-control'}
    ))

    def clean(self):
        """
        Extra validation for fields that depends on other fields

        :return: Dictionary
        """
        cleaned_data = super(PasswordResetForm, self).clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        if password != password_confirmation:
            raise ValidationError("The two passwords do not match.")
        return cleaned_data


class SignupForm(BaseForm):
    """
    Form for SIGNUP
    """

    birth_date = DateField(
        required=True, label="Date of Birth", input_formats=['%d/%m/%Y', ],
        widget=TextInput(
            attrs={'placeholder': 'Date of Birth', 'class': 'form-control'}
        )
    )
    email = EmailField(required=True, label="Email", widget=EmailInput(
        attrs={'placeholder': 'E-mail', 'class': 'form-control'}
    ))
    first_name = CharField(required=True, label="First Name", max_length=60, widget=TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control'}
    ))
    last_name = CharField(required=True, label="Last Name", max_length=60, widget=TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control'}
    ))
    password = CharField(required=True, label="Password", widget=PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}
    ))

    def save(self, commit=True):
        """
        Saves user using the 'create_user' manager method.

        If it's an existing user, we only allow the operation if he has never set a password

        :return: Dictionary
        """

        # Saves User
        current_email = self.cleaned_data["email"]
        user = get_object_or_false(get_user_model(), email=current_email)
        if user:
            user.email = self.cleaned_data["email"]
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.set_password(self.cleaned_data["password"])
            user.has_updated_password = True
            user.save()
        else:
            user = get_user_model().objects.create_user(
                self.cleaned_data["email"],
                first_name=self.cleaned_data["first_name"],
                last_name=self.cleaned_data["last_name"],
                password=self.cleaned_data["password"],
            )

        # Saves Member
        member, created = Member.objects.get_or_create(user=user)
        member.birth_date = self.cleaned_data["birth_date"]
        member.save()
        return member

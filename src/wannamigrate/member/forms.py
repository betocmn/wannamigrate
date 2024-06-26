"""
Product FORMS

Form definitions used by views/templates from the product app
"""

##########################
# Imports
##########################
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.forms import (
    EmailField, CharField, PasswordInput, ValidationError, RadioSelect,
    ModelChoiceField, TextInput, EmailInput, ChoiceField
)
from django.conf import settings
from wannamigrate.core.forms import BaseForm
from wannamigrate.member.models import Member
from wannamigrate.core.util import get_object_or_false
from wannamigrate.core.models import Country


#######################
# FORM Classes
#######################
class LoginForm(BaseForm):
    """
    Form for regular email/password login
    """
    email = EmailField(required=True, label=_('E-mail'), widget=EmailInput(
        attrs={'placeholder': _('elon.musk@me.com')}
    ))
    password = CharField(required=True, label=_('Password'), widget=PasswordInput(
        attrs={'placeholder': _('**********')}
    ))


class PasswordRecoveryForm(BaseForm):
    """
    Form for RECOVER PASSWORD
    """
    email = EmailField(required=True, label=_('E-mail'), widget=EmailInput(
        attrs={'placeholder': _('elon.musk@me.com')}
    ))


class PasswordResetForm(BaseForm):
    """
    Form to set a new password

    """
    password = CharField(required=True, label=_('New Password'), widget=PasswordInput(
        attrs={'placeholder': _('New Password')}
    ))
    password_confirmation = CharField(required=True, label=_('Confirm New Password'), widget=PasswordInput(
        attrs={'placeholder': _('Confirm New Password')}
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
            raise ValidationError(_("The two passwords do not match."))
        return cleaned_data


class SignupForm(BaseForm):
    """
    Form for SIGNUP
    """

    first_name = CharField(required=True, label=_('First Name'), max_length=60, widget=TextInput(
        attrs={'placeholder': _('Elon')}
    ))
    last_name = CharField(required=True, label=_('Last Name'), max_length=60, widget=TextInput(
        attrs={'placeholder': _('Musk')}
    ))
    country = ModelChoiceField(
        required=True, label=_('Country of Birth'), empty_label=_('Where are you from?'),
        queryset=Country.objects.order_by('name'),
    )
    email = EmailField(required=True, label=_('E-mail'), widget=EmailInput(
        attrs={'placeholder': _('elon.musk@me.com')}
    ))
    password = CharField(required=True, label=_('Password'), widget=PasswordInput(
        attrs={'placeholder': _('Create a strong password')}
    ))
    gender = ChoiceField(
        required=True, label=_('Gender'), choices=settings.GENDER_CHOICES, widget=RadioSelect()
    )

    def clean(self):
        """
        Extra validation to validate birth date and existing users

        :return: Dictionary
        """

        cleaned_data = super(SignupForm, self).clean()

        # If existing user, must have never set password
        user = get_object_or_false(get_user_model(), email=cleaned_data.get("email", '').lower())
        if user and user.has_updated_password:
            raise ValidationError("Sorry, you have already signed-up. Please proceed to login.")

        return cleaned_data

    def save(self, commit=True):
        """
        Saves user using the 'create_user' manager method.

        If it's an existing user, we only allow the operation if he has never set a password

        :return: Dictionary
        """

        # Saves User
        user = get_object_or_false(get_user_model(), email=self.cleaned_data["email"].lower())
        if user and not user.has_updated_password:
            user.email = self.cleaned_data["email"]
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.set_password(self.cleaned_data["password"])
            user.has_updated_password = True
            user.save()
        else:
            if user:
                user.email = self.cleaned_data["email"].lower()
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
        member.country = self.cleaned_data["country"]
        member.gender = self.cleaned_data["gender"]
        member.save()
        return member

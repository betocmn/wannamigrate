"""
Product FORMS

Form definitions used by views/templates from the product app
"""

##########################
# Imports
##########################
from django.contrib.auth import get_user_model
from django.forms import EmailField, ValidationError
from django.forms.widgets import EmailInput
from wannamigrate.core.forms import BaseForm
from wannamigrate.member.models import Member
from wannamigrate.core.util import get_object_or_false


#######################
# FORM Classes
#######################
class SignupQuizForm(BaseForm):
    """
    Form for SIGNUP
    """

    email = EmailField(required=True, label="Email", widget=EmailInput(
        attrs={'class': 'form-control'}
    ))

    def __init__(self, *args, **kwargs):
        """
        Injects member attribute to store possible existing member

        :return: Dictionary
        """
        super(SignupQuizForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        Extra validation to validate birth date and existing users

        :return: Dictionary
        """

        cleaned_data = super(SignupQuizForm, self).clean()

        # If existing user, must have never set password
        email = cleaned_data.get("email", None)
        if email:
            user = get_object_or_false(get_user_model(), email=email.lower())
            if user and user.has_updated_password:
                raise ValidationError("Sorry, you have already signed-up. Please proceed to login.")

        return cleaned_data

    def save(self):
        """
        Saves user using the 'create_user' manager method.

        If it's an existing user, we only allow the operation if he has never set a password

        :return: Dictionary
        """

        # Saves User
        current_email = self.cleaned_data["email"].lower()
        user = get_object_or_false(get_user_model(), email=current_email)
        if user:
            member = get_object_or_false(Member, user_id=user.id)
            return member
        else:
            user = get_user_model().objects.create_user(
                current_email,
            )
            member = Member()
            member.user = user
            member.save()
            return member

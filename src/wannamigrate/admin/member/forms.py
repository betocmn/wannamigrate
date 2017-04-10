"""
Admin FORMS

Form definitions used by views/templates from the admin app
"""

##########################
# Imports
##########################
from django import forms
from django.conf import settings
from django.forms import (
    TextInput, SelectMultiple, HiddenInput, Select, ModelMultipleChoiceField, ModelChoiceField,
    DateInput
)
from django.contrib.auth import get_user_model
from wannamigrate.core.forms import (
    BaseModelForm
)
from wannamigrate.member.models import Member


#######################
# MEMBERS
#######################
class MemberForm(BaseModelForm):
    """
    Form for adding and editing members
    """

    birth_date = forms.DateField(label='Birth Date', required=False,
                                 widget=DateInput(format='%d/%m/%Y'),
                                 input_formats=['%d/%m/%Y'])

    class Meta:
        model = Member
        fields = Member.get_presentation_fields('raw')
        exclude = ['referral_code', 'points', 'points_redeemed']

    def __init__(self, *args, **kwargs):
        """
        Injects user to the form

        :return: Model Object
        """
        if 'user' in kwargs:
            self.user = kwargs.pop("user")
        super(MemberForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Set the request user before saving to the DB

        :return: Model Object
        """
        member = super(MemberForm, self).save(commit=False)
        if hasattr(self, 'user'):
            member.user = self.user
        if commit:
            member.country_id = settings.DB_ID_COUNTRY_AUSTRALIA
            member.save()
        return member


class UserForm(BaseModelForm):
    """
    Form for adding and editing users
    """

    class Meta:
        model = get_user_model()
        fields = get_user_model().get_presentation_fields('raw')
        exclude = ['is_admin', 'is_superuser', 'groups', 'password', 'slug']

    def save(self, commit=True):
        """
        Extra processing: Set additional default values for new users

        :return: Dictionary
        """
        user = super(UserForm, self).save(commit=False)
        if commit:
            user.save()
        return user

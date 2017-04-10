"""
Admin FORMS

Form definitions used by views/templates from the admin app
"""

##########################
# Imports
##########################
from django.forms import (
    TextInput, SelectMultiple, HiddenInput, Select, ModelMultipleChoiceField, ModelChoiceField,
    DateInput
)
from django.contrib.auth.models import Group
from wannamigrate.core.forms import BaseModelForm


#######################
# GROUPS AND PERMISSIONS
#######################
class GroupForm(BaseModelForm):
    """
    Form for ADD and EDIT ADMIN USERS
    """

    class Meta:
        model = Group
        fields = ['name', 'permissions']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'autofocus': 'true'}),
            'permissions': SelectMultiple(attrs={'class': 'form-control', 'style': 'height: 200px;'})
        }

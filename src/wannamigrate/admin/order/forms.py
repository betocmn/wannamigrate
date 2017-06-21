"""
Admin FORMS

Form definitions used by views/templates from the admin app
"""

##########################
# Imports
##########################
from django import forms
from django.db.models import F
from django.conf import settings
from django.forms import ModelChoiceField
from wannamigrate.core.forms import (
    BaseModelForm, BaseForm, ModelChoiceFlexibleField
)
from wannamigrate.order.models import OrderItem, Order, Product
from wannamigrate.member.models import Member
from wannamigrate.core.util import get_object_or_false


#######################
# FORM DEFINITIONS
#######################
class AddOrderForm(BaseModelForm):
    """
    Form for ADD and EDIT FRUITS
    """

    member = ModelChoiceFlexibleField(
        Member, required=True, label='Search for Member', empty_label='Search for Member',
        queryset=Member.objects.none()
    )

    class Meta:
        model = Order
        fields = ['member', 'staff_notes']

    def __init__(self, *args, **kwargs):
        """
        Make first name and last name required

        :return: Dictionary
        """
        super(AddOrderForm, self).__init__(*args, **kwargs)
        self.fields['staff_notes'].required = True
        if self.instance and hasattr(self.instance, 'member'):
            self.fields['member'].queryset = Member.objects.select_related('user').filter(
                pk=self.instance.member.id
            )
        elif hasattr(self, 'data') and 'member' in self.data:
            self.fields['member'].queryset = Member.objects.select_related('user').filter(
                pk=self.data['member']
            )


class OrderItemForm(BaseModelForm):
    """
    Formset for badge rules
    """

    product = ModelChoiceField(
        required=True, label='Product', empty_label='Select Product',
        queryset=Product.objects.all()
    )

    class Meta:
        model = OrderItem
        fields = ['product']


class EditOrderForm(BaseModelForm):
    """
    Form to EDIT ORDER
    """

    class Meta:
        model = Order
        fields = ['order_status', 'staff_notes']

    def __init__(self, *args, **kwargs):
        """
        Makes staff notes required
        """
        super(EditOrderForm, self).__init__(*args, **kwargs)
        self.fields['staff_notes'].required = True


class ProductModelChoiceField(forms.ModelChoiceField):
    """
    Custom product model field to display more complete text on dropdown
    """

    def label_from_instance(self, obj):
        return obj.name

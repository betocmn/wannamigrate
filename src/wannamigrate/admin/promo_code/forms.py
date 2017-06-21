"""
Admin FORMS

Form definitions used by views/templates from the admin app
"""

##########################
# Imports
##########################
from django.forms import TextInput, ValidationError, DateField, DateInput, Select
from wannamigrate.core.forms import (
    BaseModelForm
)
from wannamigrate.order.models import PromoCode


#######################
# FRUITS
#######################
class PromoCodeForm(BaseModelForm):
    """
    Form for ADD and EDIT FRUITS
    """

    expiry_date = DateField(label='Expiry Date', widget=DateInput(format='%d/%m/%Y'),
                            input_formats=['%d/%m/%Y'])

    class Meta:
        model = PromoCode
        fields = PromoCode.get_presentation_fields('raw')
        exclude = ['usage_count']
        widgets = {
            'discount_percentage': TextInput(),
            'discount_value': TextInput(),
            'usage_limit': Select(choices=(
                ('', 'No Limitation'),
                (1, '1x'),
                (2, '2x'),
                (3, '3x'),
                (4, '4x'),
                (5, '5x'),
                (6, '6x'),
                (7, '7x'),
                (8, '8x'),
                (9, '9x'),
                (10, '10x'),
                (20, '20x'),
                (30, '30x'),
                (40, '40x'),
                (50, '50x'),
                (60, '60x'),
                (70, '70x'),
                (80, '80x'),
                (90, '90x'),
                (100, '100x'),
                (200, '200x'),
            ))
        }

    def clean(self):
        """
        Extra validation for fields that depends on other fields

        :return: Dictionary
        """
        cleaned_data = super(PromoCodeForm, self).clean()

        # Validates discount (only one is required, value or percentage)
        discount_value = cleaned_data.get("discount_value")
        discount_percentage = cleaned_data.get("discount_percentage")
        if discount_value and discount_percentage:
            raise ValidationError("You need to set only discount value or discount %")
        if not discount_value and not discount_percentage:
            raise ValidationError("You need to set either discount value or discount %")

        # Convert promo code name to uppercase
        cleaned_data['name'] = cleaned_data.get("name").upper()

        return cleaned_data

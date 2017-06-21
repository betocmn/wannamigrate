"""
Admin FORMS

Form definitions used by views/templates from the admin app
"""

##########################
# Imports
##########################
from django.forms import DateTimeField, DateInput
from wannamigrate.core.forms import (
    BaseModelForm
)
from wannamigrate.order.models import Subscription


#######################
# FORM DEFINITIONS
#######################
class SubscriptionForm(BaseModelForm):
    """
    Form to EDIT SUBSCRIPTIONS
    """

    expiry_date = DateTimeField(label='Expiry Date', widget=DateInput(format='%d/%m/%Y'),
                                input_formats=['%d/%m/%Y'], required=False)

    class Meta:
        model = Subscription
        fields = Subscription.get_presentation_fields('raw')


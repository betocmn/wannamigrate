"""
Admin FORMS

Form definitions used by views/templates from the admin app
"""

##########################
# Imports
##########################
from wannamigrate.core.forms import (
    BaseModelForm
)
from wannamigrate.doc.models import Doc


#######################
# FRUITS
#######################
class DocForm(BaseModelForm):
    """
    Form for ADD and EDIT FRUITS
    """

    class Meta:
        model = Doc
        fields = Doc.get_presentation_fields('raw')

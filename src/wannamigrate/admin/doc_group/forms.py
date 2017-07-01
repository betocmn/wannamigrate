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
from wannamigrate.doc.models import DocGroup


#######################
# FRUITS
#######################
class DocGroupForm(BaseModelForm):
    """
    Form for ADD and EDIT FRUITS
    """

    class Meta:
        model = DocGroup
        fields = DocGroup.get_presentation_fields('raw')
        exclude = ['slug']

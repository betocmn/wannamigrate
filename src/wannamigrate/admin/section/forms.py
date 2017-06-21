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
from wannamigrate.guide.models import Section


#######################
# FRUITS
#######################
class SectionForm(BaseModelForm):
    """
    Form for ADD and EDIT FRUITS
    """

    class Meta:
        model = Section
        fields = Section.get_presentation_fields('raw')

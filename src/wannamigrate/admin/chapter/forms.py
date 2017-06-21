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
from wannamigrate.guide.models import Chapter


#######################
# FRUITS
#######################
class ChapterForm(BaseModelForm):
    """
    Form for ADD and EDIT FRUITS
    """

    class Meta:
        model = Chapter
        fields = Chapter.get_presentation_fields('raw')
        exclude = ['slug']

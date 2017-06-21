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
from wannamigrate.story.models import Post


#######################
# FRUITS
#######################
class PostForm(BaseModelForm):
    """
    Form for ADD and EDIT FRUITS
    """

    class Meta:
        model = Post
        fields = Post.get_presentation_fields('raw')
        exclude = ['slug']

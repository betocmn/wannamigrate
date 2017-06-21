"""
Quiz model classes.

Magic to discover the customer's wine tastes
"""

##########################
# Imports
##########################
from stdimage.models import StdImageField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.models import BaseModel
from wannamigrate.core.util import CustomUploadToAutoSlugClassNameDir


##########################
# Classes definitions
##########################
class Post(BaseModel):
    """
    Questions
    """

    # Model Attributes
    country = models.ForeignKey("core.Country", verbose_name=_("country"))
    title = models.CharField(_("title"), max_length=200)
    description = models.CharField(_("description"), max_length=180)
    html_content = models.TextField(_("html content"))
    is_enabled = models.BooleanField(_("is enabled"), default=True)
    image = StdImageField(
        _("image"), blank=True, null=True,
        upload_to=CustomUploadToAutoSlugClassNameDir(populate_from='title'),
        variations={
            'large': (800, 600),
            'small': (400, 200),
            'thumbnail': (50, 50, True),
        }
    )
    slug = models.SlugField(max_length=200, unique=True)

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Quiz Question',
            'fields': [
                'country', 'title', 'slug', 'is_enabled', 'image', 'description', 'html_content'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_post", "ADMIN: Can add post"),
            ("admin_change_post", "ADMIN: Can change post"),
            ("admin_delete_post", "ADMIN: Can delete post"),
            ("admin_view_post", "ADMIN: Can view posts")
    )

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.title))

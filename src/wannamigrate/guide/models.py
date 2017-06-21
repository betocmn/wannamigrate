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
class Chapter(BaseModel):
    """
    Questions
    """

    # Model Attributes
    country = models.ForeignKey("core.Country", verbose_name=_("country"))
    title = models.CharField(_("title"), max_length=200)
    is_enabled = models.BooleanField(_("is enabled"), default=True)
    slug = models.SlugField(max_length=200, unique=True)
    sort_order = models.PositiveSmallIntegerField(_("sort order"), default=1)

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Chapter Details',
            'fields': [
                'country', 'title', 'slug', 'is_enabled', 'sort_order'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_chapter", "ADMIN: Can add chapter"),
            ("admin_change_chapter", "ADMIN: Can change chapter"),
            ("admin_delete_chapter", "ADMIN: Can delete chapter"),
            ("admin_view_chapter", "ADMIN: Can view chapters")
    )

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.title))


class Section(BaseModel):
    """
    Questions
    """

    # Model Attributes
    chapter = models.ForeignKey("Chapter", verbose_name=_("chapter"))
    title = models.CharField(_("title"), max_length=200)
    html_content = models.TextField(_("html content"))
    is_enabled = models.BooleanField(_("is enabled"), default=True)
    image = StdImageField(
        _("image"), blank=True, null=True,
        upload_to=CustomUploadToAutoSlugClassNameDir(populate_from='title'),
        variations={
            'large': (1400, 1000),
            'medium': (800, 600),
            'small': (400, 200),
            'thumbnail': (50, 50, True),
        }
    )
    sort_order = models.PositiveSmallIntegerField(_("sort order"), default=1)

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Section Details',
            'fields': [
                'chapter', 'title', 'is_enabled', 'image', 'html_content', 'sort_order'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_section", "ADMIN: Can add section"),
            ("admin_change_section", "ADMIN: Can change section"),
            ("admin_delete_section", "ADMIN: Can delete section"),
            ("admin_view_section", "ADMIN: Can view sections")
    )

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.title))

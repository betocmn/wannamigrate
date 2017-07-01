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
class DocGroup(BaseModel):
    """
    Questions
    """

    # Model Attributes
    country = models.ForeignKey("core.Country", verbose_name=_("country"))
    name = models.CharField(_("name"), max_length=100)
    is_enabled = models.BooleanField(_("is enabled"), default=True)
    sort_order = models.PositiveSmallIntegerField(_("sort order"), default=1)

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Chapter Details',
            'fields': [
                'country', 'name', 'is_enabled', 'sort_order'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_doc_group", "ADMIN: Can add doc_group"),
            ("admin_change_doc_group", "ADMIN: Can change doc_group"),
            ("admin_delete_doc_group", "ADMIN: Can delete doc_group"),
            ("admin_view_doc_group", "ADMIN: Can view doc_groups")
    )

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.name))


class Doc(BaseModel):
    """
    Questions
    """

    # Model Attributes
    doc_group = models.ForeignKey("DocGroup", verbose_name=_("doc group"))
    name = models.CharField(_("name"), max_length=200)
    is_enabled = models.BooleanField(_("is enabled"), default=True)
    file = models.FileField(upload_to=CustomUploadToAutoSlugClassNameDir(populate_from='name'))
    sort_order = models.PositiveSmallIntegerField(_("sort order"), default=1)

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Doc Details',
            'fields': [
                'doc_group', 'name', 'is_enabled', 'file', 'sort_order'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_doc", "ADMIN: Can add doc"),
            ("admin_change_doc", "ADMIN: Can change doc"),
            ("admin_delete_doc", "ADMIN: Can delete doc"),
            ("admin_view_doc", "ADMIN: Can view docs")
    )

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.name))

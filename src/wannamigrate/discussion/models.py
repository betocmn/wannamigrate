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
class Discussion(BaseModel):
    """
    Discussion
    """

    # Model Attributes
    country = models.ForeignKey("core.Country", verbose_name=_("country"))
    member = models.ForeignKey("member.Member", verbose_name=_("member"))
    description = models.TextField(_("description"))
    total_views = models.PositiveSmallIntegerField(_("total views"), default=0)
    total_replies = models.PositiveSmallIntegerField(_("total replies"), default=0)
    content_modified_date = models.DateTimeField(_('modified date'))

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Discussion Details',
            'fields': [
                'country', 'member', 'description', 'total_views',
                'content_modified_date'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_discussion", "ADMIN: Can add discussion"),
            ("admin_change_discussion", "ADMIN: Can change discussion"),
            ("admin_delete_discussion", "ADMIN: Can delete discussion"),
            ("admin_view_discussion", "ADMIN: Can view discussions")
        )

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.id))


class DiscussionReply(BaseModel):
    """
    DiscussionReply
    """

    # Model Attributes
    discussion = models.ForeignKey("Discussion", verbose_name=_("discussion"))
    member = models.ForeignKey("member.Member", verbose_name=_("member"))
    description = models.TextField(_("description"))
    total_upvotes = models.PositiveSmallIntegerField(_("total upvotes"), default=0)

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Discussion Reply',
            'fields': [
                'discussion', 'member', 'description', 'total_upvotes'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_discussion_reply", "ADMIN: Can add discussion reply"),
            ("admin_change_discussion_reply", "ADMIN: Can change discussion reply"),
            ("admin_delete_discussion_reply", "ADMIN: Can delete discussion reply"),
            ("admin_view_discussion_reply", "ADMIN: Can view discussion replies")
        )

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.id))


class DiscussionReplyUpvote(BaseModel):
    """
    DiscussionReplyUpvote
    """

    # Model Attributes
    discussion_reply = models.ForeignKey("DiscussionReply", verbose_name=_("discussion reply"))
    member = models.ForeignKey("member.Member", verbose_name=_("member"))

    # META Options
    class Meta:
        default_permissions = []

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.member))

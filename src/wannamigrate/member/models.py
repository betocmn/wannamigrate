"""
Member model classes.

"""

##########################
# Imports
##########################
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from stdimage.models import StdImageField
from wannamigrate.core.models import BaseModel
from wannamigrate.core.util import CustomUploadToAutoSlugClassNameDir


##########################
# Classes definitions
##########################
class Member(BaseModel):
    """
    Member Model.
    """

    # Model Attributes (DB fields)
    user = models.ForeignKey("core.User", verbose_name=_("user"), related_name="member")
    country = models.ForeignKey("core.Country", verbose_name=_("country"), null=True, blank=True)
    gender = models.CharField(
        _("gender"), max_length=1, choices=settings.GENDER_CHOICES,
        blank=True, null=True, default=None
    )
    avatar = StdImageField(
        _("photo"),
        upload_to=CustomUploadToAutoSlugClassNameDir(populate_from='user'),
        variations={
            'large': (600, 400),
            'thumbnail': (100, 100, True),
            'medium': (300, 200),
        },
        null=True, blank=True
    )
    birth_date = models.DateField(_("date of birth"), blank=True, null=True)
    is_newsletter_subscribed = models.BooleanField(_("subscribed to newsletter"), default=True)
    payment_api_customer_uuid = models.CharField(
        _("payment API Customer UUID"), max_length=100, blank=True, null=True
    )
    staff_notes = models.TextField(_("staff notes"), blank=True, null=True)
    referral_code = models.CharField(_("referral code"), max_length=30, null=True, blank=True)
    quiz_answers = models.ManyToManyField("quiz.QuizAnswer")

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Member Information',
            'fields': [
                'avatar', 'country', 'gender', 'birth_date',
                'is_newsletter_subscribed', 'payment_api_customer_uuid', 'referral_code',
                'staff_notes', 'quiz_answers'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_member", "ADMIN: Can add member"),
            ("admin_change_member", "ADMIN: Can change member"),
            ("admin_delete_member", "ADMIN: Can delete member"),
            ("admin_view_member", "ADMIN: Can view members")
        )

    # Method definitions
    def __str__(self):
        user = self.user
        return '%s - %s' % (user.get_full_name(), user.email)


class PaymentMethod(BaseModel):
    """
    Payment Type - "stripe", "paypal", etc..
    """

    # Model Attributes
    member = models.ForeignKey('member.Member', verbose_name=_('member'))
    payment_type = models.ForeignKey('order.PaymentType', verbose_name=_('payment type'))
    payment_api_method_uuid = models.CharField(_("API Payment uuid"), max_length=200)
    is_default = models.BooleanField(_("is default"), default=True)
    card_brand = models.CharField(_("card brand"), max_length=20, null=True, blank=True)
    card_last4 = models.CharField(_("card last4"), max_length=4, null=True, blank=True)
    card_expiry_month = models.PositiveSmallIntegerField(_("card exp month"), null=True,
                                                         blank=True)
    card_expiry_year = models.PositiveSmallIntegerField(_("card exp year"), null=True, blank=True)

    # META Options
    class Meta:
        default_permissions = []
        ordering = ['-is_default']

    # Method definitions
    def __str__(self):
        return '%s %s' % (self.payment_type.name, self.identifier)

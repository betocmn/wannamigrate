"""
Order Models

Models used to manage all payment transactions
"""

##########################
# Imports
##########################
from django.db import models
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.models import BaseModel


##########################
# Class Definitions
##########################
class PaymentType(BaseModel):
    """
    Payment Type - "stripe", "paypal", etc..
    """

    # Model Attributes
    name = models.CharField(_("name"), max_length=45)

    # META Options
    class Meta:
        default_permissions = []

    # Method definitions
    def __str__(self):
        return '%s' % self.name


class Product(BaseModel):
    """
    Product Model - Generic entity to represent a good that can be bought.
    """

    # Model Attributes
    name = models.CharField(_("name"), max_length=200)
    price = models.DecimalField(_("price ($)"), max_digits=7, decimal_places=2)

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Product Information',
            'fields': [
                'name', 'price'
            ]
        },
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_product", "ADMIN: Can add product"),
            ("admin_change_product", "ADMIN: Can change product"),
            ("admin_delete_product", "ADMIN: Can delete product"),
            ("admin_view_product", "ADMIN: Can view products")
        )

    # Method Definitions
    def __str__(self):
        """
        String representation of this model
        :return: String
        """
        return '%s' % self.name


class Order(BaseModel):
    """
    Order model - Show me the money
    """

    # Model Attributes
    member = models.ForeignKey("member.Member", verbose_name=_("member"))
    subscription = models.ForeignKey('Subscription', verbose_name=_("subscription"))
    payment_type = models.ForeignKey("PaymentType", verbose_name=_("payment type"))
    order_status = models.ForeignKey("OrderStatus", verbose_name=_("order status"))
    gross_total = models.DecimalField(_("gross total"), max_digits=7, decimal_places=2)
    net_total = models.DecimalField(_("net total"), max_digits=7, decimal_places=2)
    gst = models.DecimalField(_("GST"), max_digits=7, decimal_places=2)
    discount = models.DecimalField(
        _("discount"), max_digits=7, decimal_places=2, blank=True, null=True
    )
    discount_code = models.CharField(_("discount code"), max_length=40, blank=True, null=True)
    payment_fees = models.DecimalField(
        _("payment fees"), max_digits=7, decimal_places=2, blank=True, null=True
    )
    payment_api_transaction_uuid = models.CharField(
        _("payment API Transaction UUID"), max_length=100, blank=True, null=True
    )
    client_notes = models.TextField(_("client notes"), null=True, blank=True)
    staff_notes = models.TextField(_("staff notes"), null=True, blank=True)

    # Fields organised for crud operations
    fieldsets = [
        {
            "title": "Notes",
            "fields": [
                "client_notes", "staff_notes"
            ]
        },
        {
            "title": "Order Details",
            "fields": [
                "member", "created_date", "order_status",
                "gross_total", "net_total", "gst", "discount", "discount_code",
                "payment_fees",  "payment_type", "payment_api_transaction_uuid"

            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        ordering = ['-modified_date']
        permissions = (
            ("admin_change_order", "ADMIN: Can change order"),
            ("admin_view_order", "ADMIN: Can view orders"),
            ("admin_swap_wines", "ADMIN: Can swap subscription wines")
        )

    # Method definitions
    def __str__(self):
        return '%s' % self.id


class OrderHistory(BaseModel):
    """
    Order History - all payment transactions made for one order (api communication)
    """

    # Model Attributes
    order = models.ForeignKey(Order, verbose_name=_("order"))
    order_status = models.ForeignKey("OrderStatus", verbose_name=_("order status"))
    payment_api_transaction_uuid = models.CharField(
        _("payment api transaction uuid"), max_length=100, blank=True, null=True
    )
    full_api_response = models.TextField(_("full API response"), blank=True, null=True)

    # META Options
    class Meta:
        default_permissions = []
        ordering = ['-created_date']


class OrderItem(BaseModel):
    """
    Order Item
    """

    # Model Attributes
    order = models.ForeignKey(Order, verbose_name=_("order"))
    product = models.ForeignKey("Product", verbose_name=_("product"))
    product_name = models.CharField(_("product name"), max_length=200)
    product_price = models.DecimalField(_("product price ($)"), max_digits=7, decimal_places=2)

    # META Options
    class Meta:
        default_permissions = []


class OrderStatus(BaseModel):
    """
    Order Status - "awaiting payment", "payment approved", etc..
    """

    # Model Attributes
    name = models.CharField(_("name"), max_length=45)

    # META Options
    class Meta:
        default_permissions = []

    # Method definitions
    def __str__(self):
        return '%s' % self.name


class PromoCode(BaseModel):
    """
    PROMO code Model - Discount for orders
    """

    # Model Attributes
    name = models.CharField(_("code"), max_length=30, unique=True)
    discount_percentage = models.DecimalField(
        _("discount %"), max_digits=7, decimal_places=2, blank=True, null=True
    )
    discount_value = models.DecimalField(
        _("discount $"), max_digits=7, decimal_places=2, blank=True, null=True
    )
    expiry_date = models.DateField(_("expiry date"))
    is_enabled = models.BooleanField(_("is enabled"), default=True)
    usage_limit = models.PositiveSmallIntegerField(_("usage limit"), blank=True, null=True)
    usage_count = models.PositiveIntegerField(_("usage count"), default=0)

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Promo Code Information',
            'fields': [
                'name', 'discount_percentage', 'discount_value', 'expiry_date', 'is_enabled',
                'usage_limit', 'usage_count'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_promo_code", "ADMIN: Can add promo code"),
            ("admin_change_promo_code", "ADMIN: Can change promo code"),
            ("admin_delete_promo_code", "ADMIN: Can delete promo code"),
            ("admin_view_promo_code", "ADMIN: Can view promo code")
        )

    # Method definitions
    def __str__(self):
        return '%s' % (_(self.name))


class Subscription(BaseModel):
    """
    Subscription model
    """

    # Model Attributes
    member = models.OneToOneField('member.Member', verbose_name=_('member'))
    subscription_status = models.ForeignKey('SubscriptionStatus',
                                            verbose_name=_('subscription status'))
    expiry_date = models.DateTimeField(_('expiry date'), blank=True, null=True)

    # Fields organised for crud operations
    fieldsets = [
        {
            "title": "Subscriptions Details",
            "fields": [
                "member", "subscription_status", "expiry_date"
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_subscription", "ADMIN: Can add subscription"),
            ("admin_change_subscription", "ADMIN: Can change subscription"),
            ("admin_delete_subscription", "ADMIN: Can delete subscription"),
            ("admin_view_subscription", "ADMIN: Can view subscription")
        )

    # Method definitions
    def __str__(self):
        return 'ID: %s | Status %s' % (
            self.id, self.subscription_status.name
        )


class SubscriptionStatus(BaseModel):
    """
    Subscription Status - 'never activated', 'active', 'expired', 'cancelled'
    """

    # Model Attributes
    name = models.CharField(_("name"), max_length=45)

    # META Options
    class Meta:
        default_permissions = []

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.name))

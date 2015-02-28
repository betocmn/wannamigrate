"""
Marketplace Models

Models used by our marketplace app, such as Service, Order, etc..
"""

##########################
# Imports
##########################
from django.db import models
from django.db.models import Prefetch, Count
from wannamigrate.core.models import (
    BaseModel, Country
)
from django.utils.translation import ugettext_lazy as _




##########################
# Class Definitions
##########################
class Order( BaseModel ):
    """
    Order model - Payment of a request of service
    """

    # Model Attributes
    user = models.ForeignKey( 'core.User', verbose_name = _( 'user' ) )
    promo_code = models.ForeignKey( 'PromoCode', verbose_name = _( 'promo code' ), blank = True, null = True )
    order_status = models.ForeignKey( 'OrderStatus', verbose_name = _( 'order status' ) )
    service = models.ForeignKey( 'Service', verbose_name = _( 'service' ) )
    history = models.ManyToManyField( 'OrderStatus', through = 'OrderHistory', related_name = 'history' )
    gross_total = models.DecimalField( _( "gross total" ), max_digits = 5, decimal_places = 2 )
    net_total = models.DecimalField( _( "net total" ), max_digits = 5, decimal_places = 2 )
    discount = models.DecimalField( _( "discount" ), max_digits = 5, decimal_places = 2 )
    fees = models.DecimalField( _( "fees" ), max_digits = 5, decimal_places = 2 )
    installments = models.SmallIntegerField( _( "installments" ), default = 1 )
    external_code = models.CharField( _( "external code" ), max_length = 100 )

    # META Options
    class Meta:
        default_permissions = []



class OrderHistory( BaseModel ):
    """
    Order History - all payment transactions made for one order (api communication)
    """

    # Model Attributes
    order = models.ForeignKey( Order, verbose_name = _( 'order' ) )
    order_status = models.ForeignKey( 'OrderStatus', verbose_name = _( 'order status' ) )
    transaction_code = models.CharField( _( "transaction code" ), max_length = 100 )
    payment_code = models.CharField( _( "payment code" ), max_length = 100 )
    message = models.TextField( _( "message" ), blank = True, null = True )

    # META Options
    class Meta:
        default_permissions = []



class OrderStatus( BaseModel ):
    """
    Order Status - 'awaiting payment', 'payment approved', etc..
    """

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 45 )

    # META Options
    class Meta:
        default_permissions = []



class Provider( BaseModel ):
    """
    Provider - The professional or company that will provide services
    """

    # Model Attributes
    user = models.ForeignKey( 'core.User', verbose_name = _( 'user' ) )
    review_score = models.DecimalField( _( "discount" ), max_digits = 5, decimal_places = 2, default = 0 )
    regulator = models.ForeignKey( 'Regulator', verbose_name = _( 'regulator' ) )
    display_name = models.CharField( _( "name" ), max_length = 80 )
    headline = models.CharField( _( "headline" ), max_length = 150 )
    description = models.TextField( _( "description" ) )
    skype_username = models.CharField( _( "skype ID" ), max_length = 100, blank = True, null = True )
    paypal_email = models.EmailField( _( "paypal email" ), blank = True, null = True )
    website = models.URLField( _( "website" ), blank = True, null = True )

    # Many to many relations
    languages = models.ManyToManyField( 'core.Language' ) # Languages this provider can give service in
    countries = models.ManyToManyField( 'core.Country' ) # countries this provider support
    service_types = models.ManyToManyField( 'ServiceType', through = 'Provider_ServiceTypes', related_name = 'service_types' )

    # META Options
    class Meta:
        default_permissions = []

    # Class Methods
    @staticmethod
    def get_listing( country_id, limit_from, limit_to  ):
        """
        Query used to search for service providers sorted
        by relevance.  The relevance is calculated with
        the following:

        1- Support for the destination country (Required)
        2- Higher review Average Score
        3- Higher number of contracts
        4- Higher number of answers
        5- Most recent last login date

        :param: country_id
        :param: limit_from
        :param: limit_to
        :return: Objects
        """

        providers = Provider.objects.select_related(
            'user', 'user__userpersonal', 'user__userstats'
        ).prefetch_related(
            Prefetch(
                'service_types',
                queryset = ServiceType.objects
                    .select_related( 'service_type_category' )
                    .only( 'service_type_category', 'name' )
                    .order_by( 'service_type_category__name' )
            )
        ).filter(
            countries = country_id,
        ).only(
            'id', 'display_name', 'user', 'headline', 'review_score'
        ).order_by(
            '-user__userstats__total_reviews', '-user__userstats__total_contracts',
            '-user__userstats__total_answers', '-user__last_login'
        )[limit_from:limit_to]

        return providers



class Provider_ServiceTypes( BaseModel ):
    """
    A many-to-many relation from the provider and service_type models
    """

    # Model Attributes
    service_type = models.ForeignKey( 'ServiceType', verbose_name = _( 'service type' ) )
    provider = models.ForeignKey( 'Provider', verbose_name = _( 'provider' ) )
    is_top = models.BooleanField( _( "is top service" ), default = False )

    # META Options
    class Meta:
        default_permissions = []
        unique_together = ( "service_type", "provider" )



class PromoCode( BaseModel ):
    """
    PROMO code Model - Discount for orders
    """

    # Model Attributes
    name = models.CharField( _( "code" ), max_length = 15 )
    discount = models.DecimalField( _( "discount" ), max_digits = 5, decimal_places = 2 )
    expiry_date = models.DateField( _( 'date' ) )

    # META Options
    class Meta:
        default_permissions = []



class Regulator( BaseModel ):
    """
    Regulator Model - That organization that regulates some immigration related occupation
    """

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 80 )
    website = models.URLField( _( "website" ), blank = True, null = True )

    # META Options
    class Meta:
        default_permissions = []



class Review( BaseModel ):
    """
    User Reviews - comments and score given by other users (mostly to service providers)
    """

    # Model Attributes
    from_user = models.ForeignKey( 'core.User', related_name = 'review_from_user', verbose_name = _( 'from user' ) )
    to_user = models.ForeignKey( 'core.User', related_name = 'review_to_user', verbose_name = _( 'to user' ) )
    score = models.SmallIntegerField( _( "review score" ), default = 0 )
    comment = models.TextField( _( "comment" ) )

    # META Options
    class Meta:
        default_permissions = []



class Service( BaseModel ):
    """
    Service model - Mentoring service
    """

    # Model Attributes
    from_user = models.ForeignKey( 'core.User', related_name = 'service_from_user', verbose_name = _( 'from user' ) )
    to_user = models.ForeignKey( 'core.User', related_name = 'service_to_user', verbose_name = _( 'to user' ) )
    service_type = models.ForeignKey( 'ServiceType', verbose_name = _( 'service type' ) )
    service_status = models.ForeignKey( 'ServiceStatus', verbose_name = _( 'service status' ) )
    service_price = models.DecimalField( _( "service price" ), max_digits = 5, decimal_places = 2 )
    history = models.ManyToManyField( 'ServiceStatus', through = 'ServiceHistory', related_name = 'history' )

    # META Options
    class Meta:
        default_permissions = []



class ServiceHistory( BaseModel ):
    """
    Service History - all changes in status of a booked service
    """

    # Model Attributes
    service = models.ForeignKey( Service, verbose_name = _( 'service' ) )
    service_status = models.ForeignKey( 'ServiceStatus', verbose_name = _( 'service status' ) )
    user = models.ForeignKey( 'core.User', verbose_name = _( 'changed by user' ) )

    # META Options
    class Meta:
        default_permissions = []



class ServiceStatus( BaseModel ):
    """
    Service Status - 'requested', 'confirmed', 'cancelled', etc..
    """

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 45 )

    # META Options
    class Meta:
        default_permissions = []



class ServiceType( BaseModel ):
    """
    Service Type - 'skype service', 'file review', 'full immigration consultancy', etc..
    """

    # Model Attributes
    service_type_category = models.ForeignKey( 'ServiceTypeCategory', verbose_name = _( 'category' ) )
    name = models.CharField( _( "name" ), max_length = 60 )
    description = models.TextField( _( "description" ) )

    # META Options
    class Meta:
        default_permissions = []



class ServiceTypeCategory( BaseModel ):
    """
    Service Type Category - A parent group for service types. ("Immigration Consultancy", "Translation", "Headhunting", etc..)
    """

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 40 )

    # META Options
    class Meta:
        default_permissions = []


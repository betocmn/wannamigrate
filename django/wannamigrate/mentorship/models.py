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
from django.conf import settings




##########################
# Class Definitions
##########################
class Applicant( BaseModel ):
    """
    Applicant model - professionals applying to get the service
    """

    # Model Attributes
    user = models.ForeignKey( 'core.User', verbose_name = _( 'user' ) )
    linkedin_url = models.URLField( _( "boleto url" ), blank = True, null = True )
    about = models.TextField( _( "goal" ) )

    # META Options
    class Meta:
        default_permissions = []
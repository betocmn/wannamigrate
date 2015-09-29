##############
# Imports
##############
from django.db import models
from wannamigrate.core.models import BaseModel, User
from django.utils.translation import ugettext_lazy as _





##################
# Definitions
##################
class IframeContent( BaseModel ):
    """
    This class represents a simple HTML Content.
    """
    # The html code of this content.
    url = models.CharField( max_length = 300 )


    class Meta:
        app_label = "director"




class IframeContentUserProgress( BaseModel ):
    """
    Relates users and IframeContents
    """
    iframe = models.ForeignKey( "IframeContent"  )
    user = models.ForeignKey( User )
    progress = models.IntegerField()


    class Meta:
        unique_together = ( "iframe", "user" )
        app_label = "director"
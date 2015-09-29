##############
# Imports
##############
from django.db import models
from wannamigrate.core.models import BaseModel, User
from django.utils.translation import ugettext_lazy as _





##################
# Definitions
##################
class HtmlContent( BaseModel ):
    """
    This class represents a simple HTML Content.
    """
    # The html code of this content.
    html = models.TextField()


    class Meta:
        app_label = "director"



class HtmlContentUserProgress( BaseModel ):
    """
    Relates users and HtmlContents
    """
    html = models.ForeignKey( "HtmlContent"  )
    user = models.ForeignKey( User )
    progress = models.IntegerField()


    class Meta:
        unique_together = ( "html", "user" )
        app_label = "director"

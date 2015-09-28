##############
# Imports
##############
from django.db import models
from wannamigrate.core.models import BaseModel, User
from django.utils.translation import ugettext_lazy as _





##################
# Definitions
##################
class RedirectContent( BaseModel ):
    """
    This class represents a simple HTML Content.
    """
    # The html code of this content.
    url = models.CharField( max_length = 300 )
    progress_url = models.CharField( max_length = 300, blank = True, default = '' )
    blank = models.BooleanField( default = True )


    class Meta:
        app_label = "director"




class RedirectContentUserProgress( BaseModel ):
    """
    Relates users and HtmlContents
    """
    redirect_content = models.ForeignKey( "RedirectContent"  )
    user = models.ForeignKey( User )
    progress = models.IntegerField()


    class Meta:
        unique_together = ( "redirect_content", "user" )
        app_label = "director"

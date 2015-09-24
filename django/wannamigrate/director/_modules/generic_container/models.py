##############
# Imports
##############
from django.db import models
from wannamigrate.core.models import BaseModel, User
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType





##################
# Definitions
##################
class GenericContainer( BaseModel ):
    """
    This class represents a simple HTML Content.
    """
    # The layout to display
    layout = models.CharField( max_length = 200 )


    class Meta:
        app_label = "director"



class GenericContainerContent( BaseModel ):
    """
    Relates users and HtmlContents
    """
    container = models.ForeignKey( "GenericContainer", related_name = "contents" )
    order = models.IntegerField()
    # The content of the objective (a generic foreign key)
    content_type = models.ForeignKey( ContentType )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey( 'content_type', 'object_id' )
    # The module of the content
    content_module = models.CharField( max_length = 200 )


    class Meta:
        app_label = "director"

##############
# Imports
##############
from django.db import models
from wannamigrate.core.models import BaseModel, User
from django.utils.translation import ugettext_lazy as _





##################
# Definitions
##################
class FormContent( BaseModel ):
    """
    This class represents a simple HTML Content.
    """
    # The html code of this content.
    question = models.CharField( max_length = 300 )


    class Meta:
        app_label = "director"




class FormContentChoice( BaseModel ):
    """
    The choices of the Form.
    """
    form = models.ForeignKey( "FormContent", related_name = "choices" )
    text = models.CharField( max_length = 200 )
    progress_amount = models.IntegerField()


    class Meta:
        app_label = "director"



class FormContentUserChoice( BaseModel ):
    """
    Relates users, forms and choices
    """
    form = models.ForeignKey( "FormContent"  )
    user = models.ForeignKey( User )
    choice = models.ForeignKey( "FormContentChoice" )


    class Meta:
        unique_together = ( "user", "form" )
        app_label = "director"
##########################
# Imports
##########################
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from wannamigrate.core.models import BaseModel, Situation
from django.utils.translation import ugettext_lazy as _





class Mission( BaseModel ):
    """
    This class defines a mission. A mission is a part
    of a situation to achieve the imigration goal.
    A situation can have many missions, and missions
    are composed by objectives.
    """
    # The title of the mission (Ex: Visa type, English Skills).
    title = models.CharField( max_length = 200 )
    # The objectives of this mission.
    objectives = models.ManyToManyField( "Objective", through = "MissionsObjectives", related_name = "missions" )
    # The situations of this mission
    situations = models.ManyToManyField( Situation, through = "SituationsMissions", related_name = "missions" )


    # The str representation of this object
    def __str__( self ):
        return _( self.title )




class Objective( BaseModel ):
    """
    This class defines an objective, that is part of a mission.
    The objectives describes something that the user should
    do (watch, listen, answer) in order to complete itself.
    """
    # The title of the objective (Ex: Defining your visa type).
    title = models.CharField( max_length = 250 )
    # The description of the objective (Ex: Browse your possibilities and see what
    # better to you... ).
    description = models.TextField()

    # The content of the objective (a generic foreign key)
    content_type = models.ForeignKey( ContentType )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey( 'content_type', 'object_id' )
    # The module of the content
    content_module = models.CharField( max_length = 200 )



    # The str representation of this object
    def __str__( self ):
        return _( self.title )




class MissionsObjectives( BaseModel ):
    """
    Relational object. It relates Missions and Objectives.
    """
    # The mission
    mission = models.ForeignKey( "Mission" )
    # The objective
    objective = models.ForeignKey( "Objective" )
    # The order of the objective on the mission
    order = models.PositiveSmallIntegerField()
    # Indicates if this step is optional
    optional = models.BooleanField( default = False )


    class Meta:
        unique_together = ( ( "mission", "objective" ), ( "mission", "order" ), )


    # The str representation of this object
    def __str__( self ):
        return str( self.mission ) + ' ' + str( self.objective ) + ' ' + str( self.order ) + "(optional)" if self.optional else "(required)"




class SituationsMissions( BaseModel ):
    """
    Relational object. It relates Missions and Situations.
    """
    # The objective
    situation = models.ForeignKey( Situation )
    # The mission
    mission = models.ForeignKey( "Mission" )
    # The order of the mission on the situation
    order = models.PositiveSmallIntegerField()


    class Meta:
        unique_together = ( ( "situation", "mission" ), ( "situation", "order" ), )


    # The str representation of this object
    def __str__( self ):
        return str( self.situation ) + ' ' + str( self.mission ) + ' ' + str( self.order )







"""
#############################################
# Loads all the models from the modules
# inside _modules folder.
#############################################
import importlib
import os
search_path = os.path.dirname( os.path.abspath( __file__ ) ) + '/' + "_modules"
modules_to_load = [x for x in os.listdir( search_path ) ]
package = '.'.join( [__package__, "_modules" ] )
for module in modules_to_load:
    abs_package = '.'.join( [ package, module, "models" ] )
    importlib.__import__( abs_package )
"""
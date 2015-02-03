"""
    QA Unit tests.
"""

########################
# Imports
########################
from django.test import TestCase
from wannamigrate.qa.models import Post




#######################
# Testing classes
#######################
class ModelingTester( TestCase ):
    """ 
        This class provides tests units to the database modeling.
    """

    def setUp( self ):
        """
            Creates the enviroment for the tests.
        """


    def tearDown( self ):
        """
            Undo the changes made by the setUp method. 
        """


    def test_integrity_correctness( self ):
        """
            Tests the relations of the QA models, ensuring that everything is ok.
            Testing examples: 
                - A question cannot have parents. 
                - A Comment and an Answer cannot have title.
                - etc
        """
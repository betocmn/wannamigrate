"""
    QA Unit tests.
    Remember that the tests creates a new table on the database, so the database user should have 
    CREATE DATABASE privilegies.
"""

########################
# Imports
########################
from django.conf import settings
from django.test import TestCase
from wannamigrate.qa.models import Post




#######################
# Testing classes
#######################
class ModelingTest( TestCase ):
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


    def test_constants_definitions( self ):
        """
            Tests if the required constants of the QA app was defined.
        """

        # Checks Post, Question, Answer and Comment id constants
        self.assertIsNotNone( settings.QA_POST_TYPE_BLOGPOST_ID )
        self.assertIsNotNone( settings.QA_POST_TYPE_QUESTION_ID )
        self.assertIsNotNone( settings.QA_POST_TYPE_ANSWER_ID )
        self.assertIsNotNone( settings.QA_POST_TYPE_COMMENT_ID )


    def test_integrity_correctness( self ):
        """
            Tests the relations of the QA models, ensuring that everything is ok.
            Testing examples: 
                - A question cannot have parents. 
                - A Comment and an Answer cannot have title.
                - etc
        """

        # A question should not have a parent
        result = Post.objects.filter( post_type = settings.QA_POST_TYPE_QUESTION_ID, parent__isnull = False )
        self.assertEqual( len( result ), 0 )

        # A comment should not have a title
        result = Post.objects.filter( post_type = settings.QA_POST_TYPE_COMMENT_ID, title != "" )
        self.assertEqual( len( result ), 0 )

        # An answer should not have a title
        result = Post.objects.filter( post_type = settings.QA_POST_TYPE_ANSWER_ID, title != "" )
        self.assertEqual( len( result ), 0 )
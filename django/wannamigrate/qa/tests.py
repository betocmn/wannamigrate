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
from wannamigrate.qa.models import Post, PostType, Topic, Vote, VoteType
from wannamigrate.core.models import User
from datetime import datetime



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

        # Checks Upvote, downvote and report id constants
        self.assertIsNotNone( settings.QA_VOTE_TYPE_UPVOTE )
        self.assertIsNotNone( settings.QA_VOTE_TYPE_DOWNVOTE )
        self.assertIsNotNone( settings.QA_VOTE_TYPE_REPORT )


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

        # A blogpost should not have a parent
        result = Post.objects.filter( post_type = settings.QA_POST_TYPE_BLOGPOST_ID, parent__isnull = False )
        self.assertEqual( len( result ), 0 )

        # A comment should not have a title
        result = Post.objects.filter( post_type = settings.QA_POST_TYPE_COMMENT_ID ).exclude( title = "" )
        self.assertEqual( len( result ), 0 )

        # Any comment should have a parent
        result = Post.objects.filter( post_type = settings.QA_POST_TYPE_COMMENT_ID, parent__isnull = True )
        self.assertEqual( len( result ), 0 )

        # An answer should not have a title
        result = Post.objects.filter( post_type = settings.QA_POST_TYPE_ANSWER_ID ).exclude( title = "" )
        self.assertEqual( len( result ), 0 )

        # Any answer should have a parent
        result = Post.objects.filter( post_type = settings.QA_POST_TYPE_ANSWER_ID, parent__isnull = True )
        self.assertEqual( len( result ), 0 )


    def test_content_creation( self ):

        # Creates some users
        u1 = User( name = "test1", email = "test1@hotmail.com" )
        u1.save()

        u2 = User( name = "test2", email = "test2@hotmail.com" )
        u2.save()

        # Creates a post type 
        pt_question = PostType( id = settings.QA_POST_TYPE_QUESTION_ID, name = "Question" )
        pt_question.save()

        pt_answer = PostType( id = settings.QA_POST_TYPE_ANSWER_ID, name = "Answer" )
        pt_answer.save()

        # Creates a question
        q = Post( title = "How can I go to Canada?", owner = u1, post_type = pt_question, 
                    last_activity_date = datetime.now() )
        q.readers.add( u2 )
        q.save()

        # Creates an answer to the question
        a = Post( body = "You need to define what visa is more suitable for you and apply for it on the Canadian government site."
                    parent = q, owner = u2, post_type = pt_answer )
        a.save()

        # Creates an UPVOTE for the answer
        vt_upvote = VoteType( id = settings.QA_VOTE_TYPE_UPVOTE, name = "Upvote" )
        v = Vote( post = a, user = u2, vote_type = vt_upvote )

        # Assertions.










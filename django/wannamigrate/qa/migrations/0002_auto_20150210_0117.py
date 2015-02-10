"""
Populates the QA constants data.
"""

########################
# Imports
########################
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from django.conf import settings





#########################
# Migration functions
#########################
def populate_qa_constants( apps, schema_editor ):
    """
        Populates the QA constant data, such as PostTypes values and VoteTypes values.
        :param: apps A reference to the apps.
        :param: schema_editor A reference to the schema_editor.
    """
    # Gets the post type model manager
    PostType = apps.get_model( "qa", "PostType" )
    # Gets the vote type model manager
    VoteType = apps.get_model( "qa", "VoteType" )
    
    # Create and saves the Post Type constants
    post_types = [
        { "id" : settings.QA_POST_TYPE_ANSWER_ID, "name" : "Answer" },
        { "id" : settings.QA_POST_TYPE_BLOGPOST_ID, "name" : "Blog Post" },
        { "id" : settings.QA_POST_TYPE_COMMENT_ID, "name" : "Comment" },
        { "id" : settings.QA_POST_TYPE_QUESTION_ID, "name" : "Question" },
    ]
    for post_type in post_types:
        tmp = PostType()
        tmp.id = post_type[ "id" ]
        tmp.name = post_type[ "name" ]
        tmp.save()
    
    # Create and saves the Post Type constants
    vote_types = [
        { "id" : settings.QA_VOTE_TYPE_UPVOTE, "name" : "Upvote" },
        { "id" : settings.QA_VOTE_TYPE_DOWNVOTE, "name" : "Downvote" },
        { "id" : settings.QA_VOTE_TYPE_REPORT, "name" : "Report" },
    ]
    for vote_type in vote_types:
        tmp = VoteType()
        tmp.id = vote_type[ "id" ]
        tmp.name = vote_type[ "name" ]
        tmp.save()





#########################
# Migration configuration
#########################
class Migration(migrations.Migration):
    dependencies = [
        ('qa', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython( populate_qa_constants )
    ]
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
    # Gets the vote type model manager
    VoteType = apps.get_model( "qa", "VoteType" )

    # The Vote Type constants to be saved
    vote_types = [
        { "id" : settings.QA_VOTE_TYPE_UPVOTE_ID, "name" : "Upvote" },
        { "id" : settings.QA_VOTE_TYPE_DOWNVOTE_ID, "name" : "Downvote" },
        { "id" : settings.QA_VOTE_TYPE_REPORT_ID, "name" : "Report" },
    ]
    # Save...
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

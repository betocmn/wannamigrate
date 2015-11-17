# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.db import connection


#######################
# ACTIONS
#######################
def update_data( apps, schema_editor ):

    # Get model to use (historical version)
    Objective = apps.get_model( "director", "Objective" )
    HtmlContent = apps.get_model( "director", "HtmlContent" )
    RedirectContent = apps.get_model( "director", "RedirectContent" )

    # Fixes some information
    cursor = connection.cursor()
    cursor.execute( 'UPDATE director_missionsobjectives SET optional = 0' )
    cursor.execute( 'UPDATE director_objective SET is_public = 1' )
    cursor.execute( 'UPDATE director_objective SET is_public = 0 WHERE id in (4,41,7,25,44,62)' )

    # Inserts HTML content for premium missions/objectives
    html_content = HtmlContent()
    html_content.id = 13
    html_content.html = 'Request a time by sending an email to contact@wannamigrate.com'
    html_content.save()
    html_content = HtmlContent()
    html_content.id = 14
    html_content.html = 'Request a time by sending an email to contact@wannamigrate.com'
    html_content.save()

    # Updates ojectives for skype evaluation
    objective = Objective.objects.get(pk=4)
    objective.title = 'Personal Immigration Evaluation on Skype'
    objective.object_id = 13
    objective.content_module = 'html_content'
    objective.content_type_id = 87
    objective.save()

    objective = Objective.objects.get(pk=41)
    objective.title = 'Personal Immigration Evaluation on Skype'
    objective.object_id = 14
    objective.content_module = 'html_content'
    objective.content_type_id = 87
    objective.save()

    # deletes unused data
    RedirectContent.objects.filter(id__in = [2,4] ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('director', '0004_auto_20150929_2345'),
    ]

    operations = [
        migrations.RunPython( update_data ),
    ]

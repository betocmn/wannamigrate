# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# ACTIONS
#######################
def insert_new_objectives( apps, schema_editor ):

    # Get model to use (historical version)
    Objective = apps.get_model( "director", "Objective" )
    MissionsObjectives = apps.get_model( "director", "MissionsObjectives" )
    HtmlContent = apps.get_model( "director", "HtmlContent" )
    RedirectContent = apps.get_model( "director", "RedirectContent" )

    # Inserts ojectives for skype evaluation on "study" situations
    html_content = HtmlContent()
    html_content.id = 15
    html_content.html = 'Request a time by sending an email to contact@wannamigrate.com'
    html_content.save()

    html_content = HtmlContent()
    html_content.id = 16
    html_content.html = 'Request a time by sending an email to contact@wannamigrate.com'
    html_content.save()

    objective = Objective()
    objective.id = 75
    objective.title = 'Personal Immigration Evaluation on Skype'
    objective.description = 'Talk to an expert to have your situation evaluated'
    objective.object_id = 15
    objective.content_module = 'html_content'
    objective.content_type_id = 87
    objective.is_public = False
    objective.save()

    mission_objective = MissionsObjectives()
    mission_objective.order = 2
    mission_objective.optional = True
    mission_objective.mission_id = 8
    mission_objective.objective_id = 75
    mission_objective.save()

    objective = Objective()
    objective.id = 76
    objective.title = 'Personal Immigration Evaluation on Skype'
    objective.description = 'Talk to an expert to have your situation evaluated'
    objective.object_id = 16
    objective.content_module = 'html_content'
    objective.content_type_id = 87
    objective.is_public = False
    objective.save()

    mission_objective = MissionsObjectives()
    mission_objective.order = 2
    mission_objective.optional = True
    mission_objective.mission_id = 22
    mission_objective.objective_id = 76
    mission_objective.save()

    # Inserts ojectives for "International CV package"
    html_content = HtmlContent()
    html_content.id = 17
    html_content.html = 'Request a time by sending an email to contact@wannamigrate.com'
    html_content.save()

    html_content = HtmlContent()
    html_content.id = 18
    html_content.html = 'Request a time by sending an email to contact@wannamigrate.com'
    html_content.save()

    html_content = HtmlContent()
    html_content.id = 19
    html_content.html = 'Request a time by sending an email to contact@wannamigrate.com'
    html_content.save()

    html_content = HtmlContent()
    html_content.id = 20
    html_content.html = 'Request a time by sending an email to contact@wannamigrate.com'
    html_content.save()

    objective = Objective()
    objective.id = 77
    objective.title = 'Package - International Resumé'
    objective.description = 'We will translate and build your resumé, cover-letter and Linkedin'
    objective.object_id = 17
    objective.content_module = 'html_content'
    objective.content_type_id = 87
    objective.is_public = False
    objective.save()

    mission_objective = MissionsObjectives()
    mission_objective.order = 4
    mission_objective.optional = True
    mission_objective.mission_id = 5
    mission_objective.objective_id = 77
    mission_objective.save()

    objective = Objective()
    objective.id = 78
    objective.title = 'Package - International Resumé'
    objective.description = 'We will translate and build your resumé, cover-letter and Linkedin'
    objective.object_id = 18
    objective.content_module = 'html_content'
    objective.content_type_id = 87
    objective.is_public = False
    objective.save()

    mission_objective = MissionsObjectives()
    mission_objective.order = 4
    mission_objective.optional = True
    mission_objective.mission_id = 12
    mission_objective.objective_id = 78
    mission_objective.save()

    objective = Objective()
    objective.id = 79
    objective.title = 'Package - International Resumé'
    objective.description = 'We will translate and build your resumé, cover-letter and Linkedin'
    objective.object_id = 19
    objective.content_module = 'html_content'
    objective.content_type_id = 87
    objective.is_public = False
    objective.save()

    mission_objective = MissionsObjectives()
    mission_objective.order = 4
    mission_objective.optional = True
    mission_objective.mission_id = 19
    mission_objective.objective_id = 79
    mission_objective.save()

    objective = Objective()
    objective.id = 80
    objective.title = 'Package - International Resumé'
    objective.description = 'We will translate and build your resumé, cover-letter and Linkedin'
    objective.object_id = 20
    objective.content_module = 'html_content'
    objective.content_type_id = 87
    objective.is_public = False
    objective.save()

    mission_objective = MissionsObjectives()
    mission_objective.order = 4
    mission_objective.optional = True
    mission_objective.mission_id = 26
    mission_objective.objective_id = 80
    mission_objective.save()

    # Fixes is_optional information
    optional_ids = [ 4,7,25,41,44,62 ]
    MissionsObjectives.objects.filter( id__in = optional_ids ).update( optional = True )

class Migration(migrations.Migration):

    dependencies = [
        ('director', '0009_auto_20151117_1554'),
    ]

    operations = [
        migrations.RunPython( insert_new_objectives ),
    ]

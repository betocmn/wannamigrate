# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):


    def fix_questions_lad( apps, schema_editor ):
        """
            Updates the last activity date of the questions to it's
            most recent answer date or to it's date of creation
            if the first is not found.
            :param: apps A reference to the apps.
            :param: schema_editor A reference to the schema_editor.
        """
        # Gets the models
        Question = apps.get_model( "qa", "Question" )
        Answer = apps.get_model( "qa", "Answer" )


        questions = Question.objects.all()

        for q in questions:
            first_answer = q.answers.order_by( "-created_date" ).first()
            if first_answer:
                q.last_activity_date = first_answer.created_date
            else:
                q.last_activity_date = q.created_date

            q.save()



    dependencies = [
        ('qa', '0012_auto_20150608_1719'),
    ]


    operations = [
        migrations.RunPython( fix_questions_lad ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.db import connection


#######################
# ACTIONS
#######################
def add_answer_foreign_key( apps, schema_editor ):

    cursor = connection.cursor()


    cursor.execute( """ ALTER TABLE points_answer
                        MODIFY question_id INT(11) NOT NULL """ )

    cursor.execute( """ ALTER TABLE points_answer

                        ADD CONSTRAINT points_answer_question_id_52850fe9a7d3ca92_fk_points_question_id
                        FOREIGN KEY (question_id) REFERENCES points_question(id) """ )


#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('points', '0015_auto_20150116_2005'),
    ]

    operations = [
        migrations.RunPython( add_answer_foreign_key ),
    ]

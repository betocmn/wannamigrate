# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from django.db import transaction


#########################
# Migration functions
#########################
def fix_users_without_situation( apps, schema_editor ):
    """
        Creates an UserSituation object for each user that doesn't have it.
        :param: apps A reference to the apps.
        :param: schema_editor A reference to the schema_editor.
    """
    # Gets the models
    User = apps.get_model( "core", "User" )
    UserSituation = apps.get_model( "core", "UserSituation" )
    Situation = apps.get_model( "core", "Situation" )
    Country = apps.get_model( "core", "Country" )
    Goal = apps.get_model( "core", "Goal" )

    user_ids_ok = [ x.user.id for x in UserSituation.objects.all() ]

    from_country = Country.objects.get( id = 242 )
    to_country = Country.objects.get( id = 204 )
    goal = Goal.objects.get( id = 1 )

    situation, created = Situation.objects.get_or_create( from_country = from_country, to_country = to_country, goal = goal )

    users_to_fix = User.objects.exclude( id__in = user_ids_ok ).all()

    if users_to_fix:
        with transaction.atomic():
            for u in users_to_fix:
                temp = UserSituation( user = u, situation = situation )
                temp.save()

            situation.total_users += len( users_to_fix )
            situation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20150713_1606'),
    ]

    operations = [
        migrations.RunPython( fix_users_without_situation ),
    ]
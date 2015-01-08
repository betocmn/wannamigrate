# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# QUESTIONS
#######################
def core_add_country_config_values( apps, schema_editor ):

    # Get model to use (historical version)
    Country = apps.get_model( "core", "Country" )
    CountryConfig = apps.get_model( "core", "CountryConfig" )


    # Australia
    country_config = CountryConfig()
    country_config.id = 1
    country_config.country = Country.objects.get( pk = 117 )
    country_config.pass_mark_points = 60
    country_config.max_personal_points = 40
    country_config.max_language_points = 25
    country_config.max_education_points = 30
    country_config.max_work_points = 40
    country_config.max_total_points = 135
    country_config.save()

    # Canada
    country_config = CountryConfig()
    country_config.id = 2
    country_config.country = Country.objects.get( pk = 204 )
    country_config.pass_mark_points = 67
    country_config.max_personal_points = 17
    country_config.max_language_points = 33
    country_config.max_education_points = 30
    country_config.max_work_points = 35
    country_config.max_total_points = 115
    country_config.save()

    # New Zealand
    country_config = CountryConfig()
    country_config.id = 3
    country_config.country = Country.objects.get( pk = 131 )
    country_config.pass_mark_points = 100
    country_config.max_personal_points = 40
    country_config.max_language_points = 0
    country_config.max_education_points = 115
    country_config.max_work_points = 45
    country_config.max_total_points = 200
    country_config.save()



#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_countryconfig'),
    ]

    operations = [
        migrations.RunPython( core_add_country_config_values ),
    ]

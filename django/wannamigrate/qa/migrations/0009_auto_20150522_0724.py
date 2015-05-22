# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.utils import translation
import itertools


#########################
# Migration functions
#########################
def translate_topics_to_en( apps, schema_editor ):
    """
        Updates the slug value for existing topics
        :param: apps A reference to the apps.
        :param: schema_editor A reference to the schema_editor.
    """
    LANGUAGE_CODE = "en"
    # Gets the models
    Topic = apps.get_model( "qa", "Topic" )
    TopicTranslation = apps.get_model( "qa", "TopicTranslation" )
    Language = apps.get_model( "core", "Language" )

    translation.activate( LANGUAGE_CODE )
    # Gets the language
    language = Language.objects.filter( code = LANGUAGE_CODE ).first()
    topics = Topic.objects.order_by( "id" ).all()
    for topic in topics:
        # Translate each topic (call save on each entry is required to generate the slugs)
        translated_name = _( topic.name )

        # Calculates the slug handling repetition
        max_length = topic._meta.get_field( 'slug' ).max_length
        translated_slug = orig = slugify( translated_name )[:max_length]

        for x in itertools.count(1):
            if not TopicTranslation.objects.filter( slug = translated_slug, language = language ).exists():
                break
            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            translated_slug = "{0}-{1}".format( orig[ : max_length - len( str( x ) ) - 1 ], x )

        topic_translation = TopicTranslation( name = translated_name, slug = translated_slug, topic = topic, language = language )
        topic_translation.save()
    translation.deactivate()



#########################
# Migration configuration
#########################
class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0008_auto_20150522_0724'),
    ]

    operations = [
        migrations.RunPython( translate_topics_to_en ),
    ]
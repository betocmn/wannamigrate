# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from django.template.defaultfilters import slugify
import itertools





#########################
# Migration functions
#########################
def update_slug( apps, schema_editor ):
    """
        Updates the slug value for existing topics
        :param: apps A reference to the apps.
        :param: schema_editor A reference to the schema_editor.
    """
    # Gets the vote type model manager
    Topic = apps.get_model( "qa", "Topic" )
    topics = Topic.objects.order_by( "id" ).all()
    for topic in topics:
        if not topic.slug:
            # Calculates the slug handling repetition
            max_length = topic._meta.get_field( 'slug' ).max_length
            topic.slug = orig = slugify( topic.name )[:max_length]

            for x in itertools.count(1):
                if not Topic.objects.filter( slug = topic.slug ).exists():
                    break
                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                topic.slug = "{0}-{1}".format( orig[ : max_length - len( str( x ) ) - 1 ], x )

        topic.save()





#########################
# Migration configuration
#########################
class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20150512_2143'),
    ]

    operations = [

        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(max_length=100, default='', unique=True),
            preserve_default=False,
        ),

        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),

        migrations.RunPython( update_slug ),
    ]

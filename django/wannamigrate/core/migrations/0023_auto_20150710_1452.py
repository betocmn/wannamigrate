# -*- coding: utf-8 -*-
#######################
# Imports
#######################
from __future__ import unicode_literals
from django.db import models, migrations
from django.template.defaultfilters import slugify
import itertools





#########################
# Migration functions
#########################
def update_slug( apps, schema_editor ):
    """
        Updates the slug value for existing users
        :param: apps A reference to the apps.
        :param: schema_editor A reference to the schema_editor.
    """
    # Gets the vote type model manager
    User = apps.get_model( "core", "User" )
    users = User.objects.order_by( "id" ).all()
    slugs_used = []
    for user in users:
        if not user.slug:
            # Calculates the slug handling repetition
            max_length = user._meta.get_field( 'slug' ).max_length
            if not user.name or len( user.name ) <= 0:
                user.name = user.email.split( '@', 1 )[0]

            user.slug = orig = slugify( user.name )[:max_length]

            for x in itertools.count(1):
                if not user.slug in slugs_used:
                    slugs_used.append( user.slug )
                    break
                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                user.slug = "{0}-{1}".format( orig[ : max_length - len( str( x ) ) - 1 ], x )

        user.save()






#########################
# Migration configuration
#########################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20150609_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(max_length=200, unique=False, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=120, verbose_name='name', default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='preferred_language',
            field=models.CharField(max_length=6, choices=[('en', 'English'), ('pt', 'Portuguese')], verbose_name='Preferred Language', default='en'),
            preserve_default=True,
        ),

        migrations.RunPython( update_slug ),

        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, default=''),
            preserve_default=True,
        ),
    ]

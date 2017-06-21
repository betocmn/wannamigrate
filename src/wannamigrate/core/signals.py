"""
With signal you can pretty much setup state actions before
or after some action occurs.

Django includes a “signal dispatcher” which helps allow
decoupled applications get notified when actions occur elsewhere in the framework

Read more on: https://docs.djangoproject.com/en/1.9/topics/signals/
"""

##########################
# Imports
##########################
import itertools
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save, post_save
from django.contrib.auth import get_user_model
from wannamigrate.core.models import (
    Country
)


##########################
# Function Definitions
##########################
def generate_user_slug(sender, instance, raw, using, update_fields, **kwargs):
    """
    Pre-Save for User.
    Generates slug based on first name and last name.
    If it finds the exact same name, it appends a counter to the string.

    NOTE: It should only be executed on insert because of URL permanent links

    :param sender:
    :param instance:
    :param raw:
    :param using:
    :param update_fields:
    :param kwargs:
    :return:
    """

    instance.email = instance.email.lower()
    if not instance.slug:
        to_slug = instance.get_full_name()
        if not to_slug:
            temp = instance.email.split("@")
            to_slug = temp[0]
        max_length = sender._meta.get_field('slug').max_length
        instance.slug = orig = slugify(to_slug)[:max_length]
        for x in itertools.count(1):
            if instance.pk:
                users = sender.objects.filter(slug=instance.slug).exclude(pk=instance.pk)
            else:
                users = sender.objects.filter(slug=instance.slug)
            if not users.exists():
                break
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)


def generate_slug_from_name(sender, instance, raw, using, update_fields, **kwargs):
    """
    Generic slugify for models that use a 'name' and 'slug' attribute.
    This will always update the slug if the name has changed

    :param sender:
    :param instance:
    :param raw:
    :param using:
    :param update_fields:
    :param kwargs:
    :return:
    """
    max_length = sender._meta.get_field('slug').max_length
    instance.slug = orig = slugify(instance.name)[:max_length]
    for x in itertools.count(1):
        if instance.pk:
            records = sender.objects.filter(slug=instance.slug).exclude(pk=instance.pk)
        else:
            records = sender.objects.filter(slug=instance.slug)
        if not records.exists():
            break
        instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)


def generate_slug_from_title(sender, instance, raw, using, update_fields, **kwargs):
    """
    Generic slugify for models that use a 'name' and 'slug' attribute.
    This will always update the slug if the name has changed

    :param sender:
    :param instance:
    :param raw:
    :param using:
    :param update_fields:
    :param kwargs:
    :return:
    """
    max_length = sender._meta.get_field('slug').max_length
    instance.slug = orig = slugify(instance.title)[:max_length]
    for x in itertools.count(1):
        if instance.pk:
            records = sender.objects.filter(slug=instance.slug).exclude(pk=instance.pk)
        else:
            records = sender.objects.filter(slug=instance.slug)
        if not records.exists():
            break
        instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)


##########################
# Signals setup
##########################
pre_save.connect(generate_user_slug, sender=get_user_model())
pre_save.connect(generate_slug_from_name, sender=Country)

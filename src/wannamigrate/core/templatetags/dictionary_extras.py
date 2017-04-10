"""
Dictionary extras. This file defines methods to handle dictionaries.

To use the template methods defined here you should load this module
on the desired template using: {% load dictionary_extras %}
"""

##########################
# Imports
##########################
from django import template


##########################
# Instantiate template register
##########################
register = template.Library()


##########################
# Function definitions
##########################
@register.filter(name='get_dict_item')
def get_dict_item(dict_item, key):
    """
    Returns the value of a key in a dictionary.

    :param dict_item: dictionary.
    :param key: The key to be catched.
    :param is_int_key: Boolean
    :return The value for the given key in the dictionary, or empty if not set.
    """
    if not dict_item:
        return ''
    try:
        return dict_item[key]
    except KeyError:
        return ''


@register.filter(name='get_dict_item_by_int_key')
def get_dict_item_by_int_key(dict_item, key):
    """
    Returns the value of a key in a dictionary.

    :param dict_item: dictionary.
    :param key: The key to be catched.
    :return The value for the given key in the dictionary, or empty if not set.
    """
    if key:
        key = int(key)
        if not dict_item:
            return ''
        try:
            return dict_item[key]
        except KeyError:
            return ''
    return ''

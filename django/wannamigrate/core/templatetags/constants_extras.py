"""
    Constants extras. This file defines methods to handle constants, including access
    to the constants file.

    To use the template methods defined here you should load this module
    on the desired template using: {% load constants_extras %}
"""
from django import template
from wannamigrate import constants

register = template.Library()

# Register a template tag to get constant values in the constants file.
@register.simple_tag
def get_constant_value( name ):
    """
        Gets a constant value in the constants file.

        :param name: The name of the constant to retrieve.
        :return The value of the constant.
    """
    return getattr( constants, name, "" )
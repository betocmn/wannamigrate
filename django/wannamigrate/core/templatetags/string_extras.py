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
@register.filter( name = 'truncate_smart' )
def truncate_smart( value, limit = 80 ):
    """
    Truncates a string after a given number of chars keeping whole words.

    Usage:
        {{ string|truncatesmart }}
        {{ string|truncatesmart:50 }}

    :param: value
    :param: limit
    :return: String
    """

    try:
        limit = int( limit )
    # invalid literal for int()
    except ValueError:
        # Fail silently.
        return value

    # Make sure it's unicode
    value = str( value )

    # Return the string itself if length is smaller or equal to the limit
    if len( value ) <= limit:
        return value

    # Cut the string
    value = value[:limit]

    # Break into words and remove the last
    words = value.split( ' ' )[:-1]

    # Join the words and return
    return ' '.join( words )
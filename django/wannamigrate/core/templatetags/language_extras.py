"""
    Language extras. This file defines language utilities for templates.

    To use the template methods defined here you should load this module
    on the desired template using: {% load language_extras %}
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
@register.filter( name = 'change_language_link' )
def change_language_link( language, redirect_url ):
    """
    Returns an anchor to set the site's default language.

    :param language: The language code to change.
    :param redirect_url: The redirect url.
    :return A well formed anchor to change the language on clicking in.
    """
    pass
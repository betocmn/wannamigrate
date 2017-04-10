"""
String extras. This file defines methods to handle dictionaries.

To use the template methods defined here you should load this module
on the desired template using: {% load string_extras %}
"""
##########################
# Imports
##########################
from django import template
import re
from django.utils.translation import ugettext as _
from django.conf import settings


##########################
# Instantiate template register
##########################
register = template.Library()


##########################
# Function definitions
##########################
@register.filter
@register.filter(name='get_range')
def get_range(value):
    """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
    """
    return range(value)

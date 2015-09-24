################
# Imports
################
from django.http import HttpResponseRedirect
from django.template import Template, Context
import pkg_resources
import urllib





##################
# Functions
##################
def render( request, content_object ):
    """
    Simple displays the html of the object.
    :param request: The request argument
    :param content_object: The object being displayed.
    :return: The content of the object rendered as string.
    """

    if not content_object.blank:
        return HttpResponseRedirect( content_object.url )

    # Loads the template from a string
    html_str = pkg_resources.resource_string( __name__, "static/html/index.html" )
    t = Template(  html_str )
    # Creates a context to the template.
    c = Context( { "content_object" : content_object } )
    return t.render( c )




def get_progress( request, content_object ):
    f = urllib.urlopen( content_object.progress_url )
    return int( f.read() )
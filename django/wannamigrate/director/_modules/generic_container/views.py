################
# Imports
################
from django.template import Template, Context
import pkg_resources
from django.utils.module_loading import import_string





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

    layout_type = content_object.layout
    contents  = content_object.contents.order_by( "order" ).all()
    for obj in contents:
        # Loads the content from the objective
        module = obj.content_module
        content_object = obj.content_object

        # Loads the render method from the current content module.
        views_path = '.'.join( [ "wannamigrate.director._modules", module, 'views' ] )
        dynamic_render = import_string( '.'.join( [ views_path, "render" ] ) )

        # Renders and asign the result to content
        obj.content = dynamic_render( request, content_object )  # call f passing the content object. It should return a template rendered.


    # Loads the template from a string
    html_str = pkg_resources.resource_string( __name__, "static/html/{0}.html".format( layout_type ) )
    t = Template(  html_str )
    # Creates a context to the template.
    c = Context({
        "content_object" : content_object,
        "contents" : contents
    })
    return t.render( c )




def get_progress( request, content_object ):
    """
    Returns the progress of the user on the given content.
    :param request: The request
    :param content_object: The html content.
    :return: The progress of the user on the given content.
    """
    average = 0

    contents = content_object.contents.order_by( "order" ).all()
    for obj in contents:
        # Loads the content from the objective
        module = obj.content_module
        content_object = obj.content_object

        # Loads the render method from the current content module.
        views_path = '.'.join( [ "wannamigrate.director._modules", module, 'views' ] )
        dynamic_get_progress = import_string( '.'.join( [ views_path, "get_progress" ] ) )

        # Renders and asign the result to content
        average += int( dynamic_get_progress( request, content_object ) )

    average = int( average / len( contents ) )
    return average


################
# Imports
################
from django.template import Template, Context
from .models import IframeContent, IframeContentUserProgress
import pkg_resources





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

    update_progress( request.user, content_object, 100 )

    # Loads the template from a string
    html_str = pkg_resources.resource_string( __name__, "static/html/index.html" )
    css_str = pkg_resources.resource_string( __name__, "static/css/iframe.css" )
    #js_str = pkg_resources.resource_string( __name__, "static/js/iframe.js" )

    context = {
        "content_object" : content_object,
        "css" : css_str,
        #"js" : js_str
    }

    t = Template(  html_str )
    # Creates a context to the template.
    c = Context( context )
    return t.render( c )




def get_progress( request, content_object ):
    """
    Returns the progress of the user on the given content.
    :param request: The request
    :param content_object: The html content.
    :return: The progress of the user on the given content.
    """
    user_progress = IframeContentUserProgress.objects.filter( user = request.user, iframe = content_object ).first()
    if ( user_progress ):
        return user_progress.progress
    return 0




def update_progress( user, content_object, value ):
    """
    Updates the user progress on the given content
    :param user: The user.
    :param content_object: The html content object
    :param value: The value to update.
    :return: None.
    """
    user_progress = IframeContentUserProgress.objects.filter( user = user, iframe = content_object ).first()
    if ( user_progress ):
        user_progress.progress = value
        user_progress.save()
    else:
        user_progress = IframeContentUserProgress()
        user_progress.user = user
        user_progress.iframe = content_object
        user_progress.progress = value
        user_progress.save()
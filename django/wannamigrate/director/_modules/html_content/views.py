################
# Imports
################
from django.template import Template, Context
from .models import HtmlContent, HtmlContentUserProgress
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
    # Updates the progress to 100%
    update_progress( request.user, content_object, 100 )

    # Loads the template from a string
    html_str = pkg_resources.resource_string( __name__, "static/html/index.html" )
    t = Template(  html_str )
    # Creates a context to the template.
    c = Context( { "content_object" : content_object } )
    return t.render( c )




def get_progress( request, content_object ):
    """
    Returns the progress of the user on the given content.
    :param request: The request
    :param content_object: The html content.
    :return: The progress of the user on the given content.
    """
    user_progress = HtmlContentUserProgress.objects.filter( user = request.user, html = content_object ).first()
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
    user_progress = HtmlContentUserProgress.objects.filter( user = user, html = content_object ).first()
    if ( user_progress and user_progress.progress != value ):
        user_progress.progress = value
        user_progress.save()
    if ( not user_progress ):
        user_progress = HtmlContentUserProgress()
        user_progress.user = user
        user_progress.html = content_object
        user_progress.progress = value
        user_progress.save()
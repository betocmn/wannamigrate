################
# Imports
################
from django.http import HttpResponseRedirect
from django.template import Template, Context
import pkg_resources
from .models import RedirectContent, RedirectContentUserProgress
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
    # Updates the progress for this content
    if ( not content_object.progress_uri ):
        update_progress( request.user, content_object, 100 )

    # Returns the redirection
    return HttpResponseRedirect( content_object.url )

    # Loads the template from a string
    #html_str = pkg_resources.resource_string( __name__, "static/html/index.html" )
    #t = Template(  html_str )
    # Creates a context to the template.
    #c = Context( { "content_object" : content_object } )
    #return t.render( c )




def get_progress( request, content_object ):

    # If the redirection content has a progress_uri, loads the progress from it.
    if ( content_object.progress_uri ):
        try:
            # Loads the render method from the current content module.
            dynamic_get_progress = import_string( content_object.progress_uri )
            # Renders and asign the result to content
            return dynamic_get_progress( request )
        except:
            return 0


    # If not, look into RedirectContentUserProgress table.
    user_progress = RedirectContentUserProgress.objects.filter( user = request.user, redirect_content = content_object ).first()
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
    user_progress = RedirectContentUserProgress.objects.filter( user = user, redirect_content = content_object ).first()
    if ( user_progress and user_progress.progress != value ):
        user_progress.progress = value
        user_progress.save()
    if ( not user_progress ):
        user_progress = RedirectContentUserProgress()
        user_progress.user = user
        user_progress.redirect_content = content_object
        user_progress.progress = value
        user_progress.save()
################
# Imports
################
from .models import FormContent, FormContentChoice, FormContentUserChoice
from django.template import Template, RequestContext
import pkg_resources
from django.http import HttpResponse





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
    context = { "content_object" : content_object }

    if request.POST:
        answer = request.POST[ 'answer' ]
        user_choice = FormContentUserChoice.objects.filter( user = request.user, form = content_object )

        if ( user_choice ):
            user_choice.update( choice_id = answer )
        else:
            user_choice = FormContentUserChoice()
            user_choice.user = request.user
            user_choice.form = content_object
            user_choice.choice_id = answer
            user_choice.save()

    # Loads the template from a string
    html_str = pkg_resources.resource_string( __name__, "static/html/index.html" )
    t = Template(  html_str )
    # Creates a context to the template.
    c = RequestContext( request, context )
    return t.render( c )



def get_progress( request, content_object ):
    """
    Returns the progress of the user based on its answer to the form.
    :param request: The request object
    :param content_object: The form object
    :return:
    """
    user_choice = FormContentUserChoice.objects.filter( user = request.user, form = content_object ).first()
    if user_choice:
        return user_choice.choice.progress_amount
    return 0
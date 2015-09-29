################
# Imports
################
from .models import FormContent, FormContentChoice, FormContentUserChoice
from django.template import Template, RequestContext
import pkg_resources
from .forms import GenericForm
from django.contrib import messages
from django.http import HttpResponse
from django.utils.translation import ugettext as _




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

    # Loads the html and css from a string
    html_str = pkg_resources.resource_string( __name__, "static/html/index.html" )
    css_str = pkg_resources.resource_string( __name__, "static/css/form.css" )

    # Gets the user answer for this form
    user_choice = FormContentUserChoice.objects.filter( user = request.user, form = content_object ).first()
    # Gets the choices of this form
    form_choices = content_object.choices.values_list( "id", "text" )

    # Data submitted?
    if request.method == 'POST':

        # Creates the form with post data
        form = GenericForm( request.POST, choices = form_choices )

        if form.is_valid():
            choice = form.cleaned_data[ 'choice' ]

            # If the user has not answered yet, create an answer entry.
            if not user_choice:
                user_choice = FormContentUserChoice()
                user_choice.user = request.user
                user_choice.form = content_object

            # Updates the choice of the user and save
            user_choice.choice_id = choice
            user_choice.save()

            # Adds a successs message
            messages.success( request, _( 'Answer successfully updated.' ) )

    # if a GET (or any other method) we'll create a blank form
    else:

        if user_choice:
            initial = { "choice": user_choice.choice_id }
        else:
            initial = {}
        form = GenericForm( choices = form_choices, initial = initial )

    # prepares the context variable and render the template
    context = { "content_object" : content_object, "css" : css_str, "form": form }
    t = Template(  html_str )
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
"""
QA Views

These are the views that control logic flow for
the templates on qa app
"""

##########################
# Imports
##########################
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wannamigrate.qa.forms import (
    AddQuestionForm
)
from wannamigrate.qa.models import(
    Post, Topic
)

##########################
# Methods
##########################
def list_posts( request ):

    return HttpResponse( 'test' )


@login_required
def add_question( request ):
    """
        Handles the process of adding a question.
    :param request:
    :return: A template rendered
    """

    # Instantiate FORM
    form = AddQuestionForm( request.POST or None, owner = request.user )


    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        # Saves the post
        post = form.save()
        messages.success( request, 'Post successfully created.' )
        # Redirect with success message
        return HttpResponseRedirect( reverse( 'qa:view_post', args = ( post.id, ) ) )

    # Template data
    template_data = {
        'form': form,
        'cancel_url': reverse( 'qa:list_posts' ),
        'topics' : Topic.objects.values( "id", "name" ),
    }

    # Print Template
    return render( request, 'qa/posts/add_question.html', template_data )


@login_required
def view_post( request, post_id ):
    """
        Handles the process of viewing a question.
    :param request:
    :param post_id: The id of the post to viewing
    :return: A template rendered
    """
    template_data = []
    # Print Template
    return render( request, 'qa/posts/view.html', template_data )




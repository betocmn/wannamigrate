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
from wannamigrate.core.decorators import ajax_login_required
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
from django.conf import settings


##########################
# Methods
##########################
def list_posts( request, *args, **kwargs ):
    """
        Handles the process of adding a question.
    :param request:
    :return: A template rendered
    """


    dbg_str = ""
    if "post_type_id" in kwargs:
        dbg_str += "post type found" + "<br>"
    if "topic_id" in kwargs:
        dbg_str += "topic id found" + "<br>"



    # FILTERS
    filter_params = {
        "results_per_step" : 10,
        "step" : 0
    }

    # TEMPLATE
    template_data = {}

    # Should filter by topics?
    if "topic_id" in kwargs:
        filter_params[ "topic_id" ] = kwargs.get( "topic_id" )
    # No? So filter by user's situation
    else:
        # Fills up the situation
        from_country = request.session['situation']['from_country']
        to_country = request.session['situation']['to_country']
        goal = request.session['situation']['goal']

        # Fills the topics related to user's situation
        filter_params[ "related_countries_ids" ] = [ from_country.id, to_country.id ]
        filter_params[ "related_goals_ids" ] = [ goal.id ]

    # Should filter by a specific post type?
    if "post_type_id" in kwargs:
        filter_params[ "post_type_id" ] = kwargs.get( "post_type_id" )

        # Sets the selected filter to the template.
        if filter_params[ "post_type_id" ] == settings.QA_POST_TYPE_BLOGPOST_ID:
            template_data[ "blogposts_menu_selected" ] = True
        elif filter_params[ "post_type_id" ] == settings.QA_POST_TYPE_QUESTION_ID:
            template_data[ "questions_menu_selected" ] = True
    else:
        template_data[ "knowledge_menu_selected" ] = True

    # Search the Posts with filters
    posts = Post.get_ranked( **filter_params )

    # If the user is authenticated
    if request.user.is_authenticated():
        # Checks if the user is following the posts
        post_ids = list( post.id for post in posts )
        following_posts = Post.objects.filter( id__in = post_ids, followers__id = request.user.id ).values_list( "id", flat=True )

        for post in posts:
            if post.id in following_posts:
                post.is_followed = True
            else:
                post.is_followed = False


    template_data[ "posts" ] = posts
    template_data[ "POST_TYPE_QUESTION_ID" ] = settings.QA_POST_TYPE_QUESTION_ID
    template_data[ "POST_TYPE_BLOGPOST_ID" ] = settings.QA_POST_TYPE_BLOGPOST_ID

    # Print Template
    return render( request, 'qa/posts/list.html', template_data )



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
    template_data = {}

    post = Post.objects.get( pk = post_id  )
    answers = Post.objects.filter( parent__id = post_id ).prefetch_related( "votes" )

    return HttpResponse( answers )

    """

    template_data[ "post" ] = post
    template_data[ "answers" ] = answers

    template_data[ "answers" ] =

    # Print Template
    return render( request, 'qa/posts/view.html', template_data )

    """


@ajax_login_required
def set_following_post( request, post_id, follow = False ):
    """
        Follows or unfollows a post.
    :param request:
    :param post_id: The id of the post to follow/unfollow
    :param following: True to follow the post, False to unfollow.
    :return: A template rendered
    """
    post = Post.objects.get( pk = post_id )
    user_id = request.user.id
    already_following = post.followers.filter( id = user_id ).exists()



    if ( follow ):
        if not already_following:
            post.followers.add( user_id )
            post.followers_count = post.followers_count + 1
            post.save()
    else:
        if already_following:
            post.followers.remove( user_id )
            post.followers_count = post.followers_count - 1
            post.save()

    return HttpResponse( post.followers_count )




@login_required
def list_topics( request ):
    """
        Show the topics that the user is following.
    :param request:
    :return: A template rendered
    """
    template_data = {
        "topics_menu_selected" : True
    }
    return render( request, 'qa/topics/list.html', template_data )
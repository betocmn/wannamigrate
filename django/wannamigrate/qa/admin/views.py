##########################
# Imports
##########################
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from wannamigrate.admin.forms import (
    AddPostForm, AddAnswerForm, EditPostForm,
    AddTopicForm,
)
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.qa.models import (
    Post, PostType, PostHistory, Topic, Vote
)
from wannamigrate.admin.views import admin_check
from django.db import transaction





#################################
# Q&A VIEWS
#################################
# Posts
@restrict_internal_ips
@permission_required( 'qa.admin_list_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def list_post( request, reported = None ):
    """
    Lists Questions and BlogPosts with pagination.

    :param: request
    :return: String
    """
    if reported:    # Should list all reported content
        reported_post_ids = Vote.objects.filter( vote_type__id = settings.QA_VOTE_TYPE_REPORT_ID ).values( "post_id" )
        posts = Post.objects.filter( id__in = reported_post_ids )
    else:
        posts = Post.objects.filter( post_type_id__in = [ settings.QA_POST_TYPE_BLOGPOST_ID,settings.QA_POST_TYPE_QUESTION_ID ] )

    paginator = Paginator( posts, settings.DEFAULT_LISTING_ITEMS_PER_PAGE )

    context = {
        "posts" : posts,
        "reported" : True if reported else False
    }


    # Checks if the page number was passed.
    page = request.GET.get( 'page' )
    try:
        posts = paginator.page( page )
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page( paginator.num_pages )

    return render( request, "qa/admin/post/list.html", context )


@restrict_internal_ips
@permission_required( 'qa.admin_add_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def add_post( request ):
    """
    Creates a Blog Post or a Question.

    :param: request
    :return: String
    """

    # Instantiate FORM
    form = AddPostForm( request.POST or None )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        # Saves the post
        post = form.save()
        messages.success( request, 'Post successfully created.' )
        # Redirect with success message
        return HttpResponseRedirect( reverse( 'admin:qa:view_post', args = ( post.id, ) ) )

    # Template data
    context = {
        'form': form,
        'cancel_url': reverse( 'admin:qa:list_post' ),
        'topics' : Topic.objects.values( "id", "name" ),
    }

    return render( request, 'qa/admin/post/add.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_add_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def add_answer( request, parent_id ):
    """
    Creates an answer or a comment to a post.

    :param: request
    :return: String
    """

    # Try to get the information about the parent post.
    parent = Post.objects.filter( id = parent_id ).first()
    if not parent:  # parent post not found, redirect to listing
        messages.error( request, 'Post with id = {0} not found.'.format( parent_id ) )
        # Redirect with success message
        return HttpResponseRedirect( reverse( 'admin:qa:list_post' ) )

    # Instantiate FORM passing parent as argument
    form = AddAnswerForm( request.POST or None, parent = parent )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        with transaction.atomic():
            # Saves the answer
            post = form.save()

            # Updates the answers count for the parent post.
            post.parent.answers_count += 1
            post.parent.save()

            messages.success( request, '{0} successfully created.'.format( post.post_type.name ) )
            # Redirect with success message
            return HttpResponseRedirect( reverse( 'admin:qa:view_post', args = ( parent_id, ) ) )

    # Template data
    context = {
        'form': form,
        'cancel_url': reverse( 'admin:qa:list_post' ),
        'topics' : Topic.objects.values( "id", "name" ),
    }

    return render( request, 'qa/admin/post/add_answer.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_view_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def view_post( request, post_id ):
    """
    Lists all posts with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {
        'post' : Post.objects.get( id = post_id ),
        'answers' : Post.objects.filter( parent__id = post_id, post_type__id = settings.QA_POST_TYPE_ANSWER_ID ),
        'post_history' : PostHistory.objects.filter( original_post__id = post_id ),
        'answers' : Post.objects.filter( parent__id = post_id ),
    }

    return render( request, 'qa/admin/post/view.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_edit_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def edit_post( request, post_id ):
    """
    Edit a post. It should create an entry on the PostHistory and edit the content of the given post.

    :param: request
    :return: String
    """
    # Gets the information about the post being edited
    post_to_edit = Post.objects.get( pk = post_id )

    # Fill up the form with post data
    form = EditPostForm( instance = post_to_edit )

    # if data submitted, fill form
    if request.POST:
        form = EditPostForm( request.POST, instance = post_to_edit )

        # If form was submitted, it tries to validate and save data
        if form.is_valid():
            post = form.save()
            messages.success( request, 'Post successfully updated.' )
            # Redirect with success message
            return HttpResponseRedirect( reverse( 'admin:qa:view_post', args = ( post.id, ) ) )


    context = {
        'form' : form,
        'post_type' : post_to_edit.post_type.name,
        'cancel_url': reverse( 'admin:qa:list_post' ),
    }

    return render( request, 'qa/admin/post/edit.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_delete_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def delete_post( request, post_id ):
    """
    Lists all posts with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    post = Post.objects.filter( pk = post_id )
    if post.exists():
        with transaction.atomic():
            post = post.get()
            if post.post_type.id == settings.QA_POST_TYPE_ANSWER_ID:
                post.parent.answers_count -= 1
                post.parent.save()

            post.delete()
            messages.success( request, "Post(id = {0}) successfully deleted.".format( post_id ) )
    else:
        messages.error( request, "Post(id = {0}) not found.".format( post_id ) )

    return HttpResponseRedirect( reverse( "admin:qa:list_post" ) )


# Topics
@restrict_internal_ips
@permission_required( 'qa.admin_list_topic', login_url = 'admin:login' )
@user_passes_test( admin_check )
def list_topic( request, reported = None ):
    """
    Lists Topics with pagination.

    :param: request
    :return: String
    """
    topics = Topic.objects.all()

    paginator = Paginator( topics, settings.DEFAULT_LISTING_ITEMS_PER_PAGE )

    context = {
        "topics" : topics,
    }


    # Checks if the page number was passed.
    page = request.GET.get( 'page' )
    try:
        topics = paginator.page( page )
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        topics = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        topics = paginator.page( paginator.num_pages )

    return render( request, "qa/admin/topic/list.html", context )


@restrict_internal_ips
@permission_required( 'qa.admin_add_topic', login_url = 'admin:login' )
@user_passes_test( admin_check )
def add_topic( request ):
    """
    Creates a Topic.

    :param: request
    :return: String
    """

    # Instantiate FORM
    form = AddTopicForm( request.POST or None )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        # Saves the post
        topic = form.save()
        messages.success( request, 'Topic successfully created.' )
        # Redirect with success message
        return HttpResponseRedirect( reverse( 'admin:qa:view_topic', args = ( topic.id, ) ) )

    # Template data
    context = {
        'form': form,
        'cancel_url': reverse( 'admin:qa:list_topic' ),
    }

    return render( request, 'qa/admin/topic/add.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_view_topic', login_url = 'admin:login' )
@user_passes_test( admin_check )
def view_topic( request, topic_id ):
    """
    Show Topic details.

    :param: request
    :return: String
    """

    context = {
        'topic' : Topic.objects.get( id = topic_id ),
    }

    return render( request, 'qa/admin/topic/view.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_edit_topic', login_url = 'admin:login' )
@user_passes_test( admin_check )
def edit_topic( request, topic_id ):
    """
    Edit a Topic.

    :param: request
    :return: String
    """
    # Gets the information about the topic being edited
    topic_to_edit = Topic.objects.get( pk = topic_id )

    # Fill up the form with post data
    form = AddTopicForm( instance = topic_to_edit )

    # if data submitted, fill form
    if request.POST:
        form = AddTopicForm( request.POST, instance = topic_to_edit )

        # If form was submitted, it tries to validate and save data
        if form.is_valid():
            topic = form.save()
            messages.success( request, 'Topic successfully updated.' )
            # Redirect with success message
            return HttpResponseRedirect( reverse( 'admin:qa:view_topic', args = ( topic.id, ) ) )


    context = {
        'form' : form,
        'cancel_url': reverse( 'admin:qa:list_post' ),
    }

    return render( request, 'qa/admin/topic/edit.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_delete_topic', login_url = 'admin:login' )
@user_passes_test( admin_check )
def delete_topic( request, topic_id ):
    """
    Delete a topic.

    :param: request
    :return: String
    """

    topic = Topic.objects.filter( pk = topic_id )
    if topic.exists():
        topic.delete()
        messages.success( request, "Topic(id = {0}) successfully deleted.".format( topic_id ) )
    else:
        messages.error( request, "Topic(id = {0}) not found.".format( topic_id ) )

    return HttpResponseRedirect( reverse( "admin:qa:list_topic" ) )
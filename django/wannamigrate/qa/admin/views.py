##########################
# Imports
##########################
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from wannamigrate.admin.forms import (
    AddPostForm, AddAnswerForm, EditQuestionForm, EditBlogPostForm,
    AddTopicForm, AddTopicTranslationForm
)
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.qa.models import Topic, Vote, TopicTranslation, Question, QuestionHistory, Answer, BlogPost, BlogPostHistory
from wannamigrate.core.models import Language
from wannamigrate.admin.views import admin_check
from django.db import transaction





#################################
# Q&A VIEWS
#################################
# Posts
@restrict_internal_ips
@permission_required( 'qa.admin_list_questions', login_url = 'admin:login' )
@user_passes_test( admin_check )
def list_questions( request, reported = False ):
    """
    Lists Questions and BlogPosts with pagination.

    :param: request
    :return: String
    """

    # Extracts get parameters
    order_by = request.GET.get( 'order_by', "created_date" )
    page = request.GET.get( 'page' )


    questions = Question.objects.order_by( order_by ).all()

    paginator = Paginator( questions, settings.DEFAULT_LISTING_ITEMS_PER_PAGE )

    # Checks if the page number was passed.
    try:
        questions = paginator.page( page )
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page( paginator.num_pages )


    context = {}
    context[ "questions" ] = questions
    context[ "order_by" ] = order_by
    context[ "page" ] = page


    return render( request, "qa/admin/question/list.html", context )


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
        return HttpResponseRedirect( reverse( 'admin:qa:view_question', args = ( post.id, ) ) )

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
            return HttpResponseRedirect( reverse( 'admin:qa:view_question', args = ( parent_id, ) ) )

    # Template data
    context = {
        'form': form,
        'cancel_url': reverse( 'admin:qa:list_post' ),
        'topics' : Topic.objects.values( "id", "name" ),
    }

    return render( request, 'qa/admin/post/add_answer.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_delete_answer', login_url = 'admin:login' )
@user_passes_test( admin_check )
def delete_answer( request, id ):
    """
    Lists all posts with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    answer = Answer.objects.filter( pk = id )
    if answer.exists():
        with transaction.atomic():
            answer = answer.get()

            answer.delete()
            messages.success( request, "Answer (id = {0}) successfully deleted.".format( id ) )
    else:
        messages.error( request, "Answer (id = {0}) not found.".format( id ) )

    return HttpResponseRedirect( request.META.get('HTTP_REFERER') )


@restrict_internal_ips
@permission_required( 'qa.admin_view_question', login_url = 'admin:login' )
@user_passes_test( admin_check )
def view_question( request, id ):
    """
    Lists all posts with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {
        'question' : Question.objects.get( id = id ),
        'edition_history' : QuestionHistory.objects.filter( parent__id = id ),
        'answers' : Answer.objects.filter( question__id = id ),
    }

    return render( request, 'qa/admin/question/view.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_edit_question', login_url = 'admin:login' )
@user_passes_test( admin_check )
def edit_question( request, id ):
    """
    Edit a post. It should create an entry on the PostHistory and edit the content of the given post.

    :param: request
    :return: String
    """
    # Gets the information about the post being edited
    question = Question.objects.get( pk = id )
    edition = QuestionHistory( parent = question, title = question.title, body = question.body, parent_created_date = question.modified_date )

    # Fill up the form with post data
    form = EditQuestionForm( request.POST or None, instance = question )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        with transaction.atomic():
            question = form.save( commit = False )
            question.generate_slug()
            question.save()
            edition.save()

            messages.success( request, 'Question successfully updated.' )
            # Redirect with success message
            return HttpResponseRedirect( reverse( 'admin:qa:view_question', args = ( question.id, ) ) )


    context = {
        'form' : form,
        'cancel_url': reverse( 'admin:qa:list_questions' ),
    }

    return render( request, 'qa/admin/question/edit.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_delete_question', login_url = 'admin:login' )
@user_passes_test( admin_check )
def delete_question( request, id ):
    """
    Lists all posts with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    question = Question.objects.filter( pk = id )
    if question.exists():
        with transaction.atomic():
            question = question.get()

            question.delete()
            messages.success( request, "Question (id = {0}) successfully deleted.".format( id ) )
    else:
        messages.error( request, "Question (id = {0}) not found.".format( id ) )

    return HttpResponseRedirect( reverse( "admin:qa:list_questions" ) )





#########################
# Blogposts
#########################
@restrict_internal_ips
@permission_required( 'qa.admin_list_blogpost', login_url = 'admin:login' )
@user_passes_test( admin_check )
def list_blogposts( request, reported = False ):
    """
    Lists BlogPosts with pagination.

    :param: request
    :return: String
    """

    # Extracts get parameters
    order_by = request.GET.get( 'order_by', "created_date" )
    page = request.GET.get( 'page' )


    blogposts = BlogPost.objects.order_by( order_by ).all()

    paginator = Paginator( blogposts, settings.DEFAULT_LISTING_ITEMS_PER_PAGE )

    # Checks if the page number was passed.
    try:
        blogposts = paginator.page( page )
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogposts = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogposts = paginator.page( paginator.num_pages )


    context = {}
    context[ "blogposts" ] = blogposts
    context[ "order_by" ] = order_by
    context[ "page" ] = page


    return render( request, "qa/admin/blogpost/list.html", context )


@restrict_internal_ips
@permission_required( 'qa.admin_view_blogpost', login_url = 'admin:login' )
@user_passes_test( admin_check )
def view_blogpost( request, id ):
    """
    Lists all posts with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {
        'blogpost' : BlogPost.objects.get( id = id ),
        'edition_history' : BlogPostHistory.objects.filter( parent__id = id ),
    }

    return render( request, 'qa/admin/blogpost/view.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_edit_blogpost', login_url = 'admin:login' )
@user_passes_test( admin_check )
def edit_blogpost( request, id ):
    """
    Edit a post. It should create an entry on the PostHistory and edit the content of the given post.

    :param: request
    :return: String
    """
    # Gets the information about the post being edited
    blogpost = BlogPost.objects.get( pk = id )
    edition = BlogPostHistory( parent = blogpost, title = blogpost.title, body = blogpost.body, parent_created_date = blogpost.modified_date )

    # Fill up the form with post data
    form = EditBlogPostForm( request.POST or None, instance = blogpost )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        with transaction.atomic():
            blogpost = form.save( commit = False )
            blogpost.generate_slug()
            blogpost.save()
            edition.save()

            messages.success( request, 'BlogPost successfully updated.' )
            # Redirect with success message
            return HttpResponseRedirect( reverse( 'admin:qa:view_blogpost', args = ( blogpost.id, ) ) )


    context = {
        'form' : form,
        'cancel_url': reverse( 'admin:qa:list_blogposts' ),
    }

    return render( request, 'qa/admin/blogpost/edit.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_delete_blogpost', login_url = 'admin:login' )
@user_passes_test( admin_check )
def delete_blogpost( request, id ):
    """
    Lists all posts with pagination.

    :param: request
    :return: String
    """

    blogpost = BlogPost.objects.filter( pk = id )
    if blogpost.exists():
        blogpost = blogpost.get()
        blogpost.delete()
        messages.success( request, "Blogpost (id = {0}) successfully deleted.".format( id ) )
    else:
        messages.error( request, "Blogpost (id = {0}) not found.".format( id ) )

    return HttpResponseRedirect( reverse( "admin:qa:list_blogposts" ) )





########################
# Topics
########################
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

    context = {
        "topics" : topics,
    }

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
        with transaction.atomic():
            # Saves the post
            topic = form.save()
            # Saves the translation to english
            english = Language.objects.filter( code = settings.LANGUAGE_CODE ).first()
            translation = TopicTranslation( name = topic.name, slug = topic.slug, topic = topic, language = english )
            translation.save()
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



############################
# Topics Translations
#############################
@restrict_internal_ips
@permission_required( 'qa.admin_add_topic_translation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def add_topic_translation( request, topic_id = None ):
    """
    Creates a Topic.

    :param: request
    :return: String
    """

    # Instantiate FORM
    if topic_id:
        form = AddTopicTranslationForm( request.POST or None, initial={ "topic" : Topic.objects.get( pk=topic_id ) } )
    else:
        form = AddTopicTranslationForm( request.POST or None )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        # Saves the post
        translation = form.save()
        messages.success( request, 'Topic Translation successfully created.' )
        # Redirect with success message
        return HttpResponseRedirect( reverse( 'admin:qa:view_topic_translation', args = ( translation.id, ) ) )

    # Template data
    context = {
        'form': form,
        'cancel_url': reverse( 'admin:qa:list_topic_translation' ),
    }

    return render( request, 'qa/admin/topic/add.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_list_topic_translation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def list_topic_translation( request ):
    """
    Lists Topics with pagination.

    :param: request
    :return: String
    """
    translations = TopicTranslation.objects.all()

    paginator = Paginator( translations, settings.DEFAULT_LISTING_ITEMS_PER_PAGE )

    # Checks if the page number was passed.
    page = request.GET.get( 'page' )
    try:
        translations = paginator.page( page )
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        translations = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        translations = paginator.page( paginator.num_pages )


    context = {
        "translations" : translations,
    }

    return render( request, "qa/admin/topic_translation/list.html", context )


@restrict_internal_ips
@permission_required( 'qa.admin_view_topic_translation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def view_topic_translation( request, id ):
    """
    Show Topic details.

    :param: request
    :return: String
    """

    context = {
        'translation' : TopicTranslation.objects.get( id = id ),
    }

    return render( request, 'qa/admin/topic_translation/view.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_edit_topic_translation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def edit_topic_translation( request, id ):
    """
    Edit a Topic.

    :param: request
    :return: String
    """
    # Gets the information about the topic being edited
    translation = TopicTranslation.objects.get( pk = id )

    form = AddTopicForm( request.POST or None, instance = translation )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        translation = form.save()
        messages.success( request, 'Topic Translation successfully updated.' )
        # Redirect with success message
        return HttpResponseRedirect( reverse( 'admin:qa:view_topic_translation', args = ( translation.id, ) ) )


    context = {
        'form' : form,
        'cancel_url': reverse( 'admin:qa:list_topic_translation' ),
    }

    return render( request, 'qa/admin/topic/edit.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_delete_topic_translation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def delete_topic_translation( request, id ):
    """
    Delete a topic.

    :param: request
    :return: String
    """

    translation = TopicTranslation.objects.filter( pk = id )
    if translation.exists():
        translation.delete()
        messages.success( request, "TopicTranslation(id = {0}) successfully deleted.".format( id ) )
    else:
        messages.error( request, "TopicTranslation(id = {0}) not found.".format( id ) )

    return HttpResponseRedirect( reverse( "admin:qa:list_topic_translations" ) )

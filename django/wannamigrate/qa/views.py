"""
QA Views

These are the views that control logic flow for
the templates on qa app
"""

##########################
# Imports
##########################
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from wannamigrate.core.decorators import ajax_login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wannamigrate.qa.forms import (
    AddQuestionForm, AddAnswerForm
)
from wannamigrate.qa.models import BlogPost, Question, Answer, Vote, Topic
from wannamigrate.core.models import(
    User, UserStats
)
from django.conf import settings
from django.utils.translation import ugettext as _
from django.db import transaction
import json
import urllib


##########################
# NON HTTP METHODS
##########################
def get_questions_by_step( user, filter_params, step, results_per_step ):
    """
    Returns a list of questions filtered by filter_params. The results are limited by step and results_per_step
    :param user: The logged user.
    :param filter_params: A list of params to filter.
    :param step: The step on the filtering
    :param results_per_step: The number of results per step.
    :return:
    """
    # Limits
    start = results_per_step * step
    end = results_per_step * step + results_per_step

    # Search the Posts with filters
    questions = Question.objects.get_listing( **filter_params )[ start : end ]

    # If the user is authenticated
    if user.is_authenticated():
        # Checks if the user is following the question
        question_ids = list( question.id for question in questions )
        following_posts = Question.objects.filter( id__in = question_ids, followers__id = user.id ).values_list( "id", flat=True )
        for question in questions:
            if question.id in following_posts:
                question.is_followed = True
            else:
                question.is_followed = False

    return questions





##########################
# HTTP Methods
##########################
@login_required
def list_all( request, *args, **kwargs ):
    """
    Lists all contents (questions and blogposts).
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    pass


def list_questions( request, *args, **kwargs ):
    """
        Handles the process of listing questions.
    :param request:
    :return: A template rendered
    """

    # SET UP THE STEP AND THE TOTAL OF STEPS
    step = 0    # starts from the begining
    results_per_step = settings.QA_QUESTIONS_PER_STEP # The number of questions to load per step

    # PROCESS FILTERS
    filter_params = {}

    # Fills up the situation
    from_country = request.session['situation']['from_country']
    to_country = request.session['situation']['to_country']
    goal = request.session['situation']['goal']

    # Fills the topics related to user's situation
    filter_params[ "related_countries_ids" ] = [ from_country.id, to_country.id ]
    filter_params[ "related_goals_ids" ] = [ goal.id ]

    # Get questions per step
    questions = get_questions_by_step( request.user, filter_params, step, results_per_step )

    # TEMPLATE DATA
    template_data = {
        "questions_menu_selected" : True,
        "questions" : questions,
        "next_step" : step + 1,
        "filter_params" : urllib.parse.urlencode( filter_params, True ),
    }

    # Print Template
    return render( request, 'qa/question/list.html', template_data )


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
        with transaction.atomic():
            question = form.save()
            # PUT GET OR CREATE EVERYWHERE! NICE PATTERN. --
            user_stats, created = UserStats.objects.get_or_create( user_id = request.user.id )
            question.followers.add( request.user )
            question.total_followers += 1
            user_stats.total_questions_following += 1

            question.save()
            user_stats.save()

            messages.success( request, 'Post successfully created.' )
            # Redirect with success message
            return HttpResponseRedirect( reverse( 'qa:view_question', args = ( question.slug, ) ) )

    # Template data
    template_data = {
        'form': form,
        'cancel_url': reverse( 'qa:list_posts' ),
        'topics' : Topic.objects.values( "id", "name" ),
    }

    # Print Template
    return render( request, 'qa/posts/add_question.html', template_data )


@login_required
def view_question( request, slug ):
    """
    Question view. Shows a question and its answers.
    :param request:
    :param slug: The identifier of the question.
    :return:
    """
    template_data = {}

    question = get_object_or_404( Question, slug = slug )
    question.total_views += 1
    question.save()

    # Gets the answer form
    answer_form = AddAnswerForm( request.POST or None, owner = request.user, question = question )
    if answer_form.is_valid():
        answer = answer_form.save()
        messages.success( request, _( 'Answer successfully created.' ) )
        return HttpResponseRedirect( reverse( "qa:view_question", kwargs={ "slug" : slug } ) + "#answer_{0}".format( answer.id ) )

    related_content = Question.objects.filter( related_topics__in = question.related_topics.all() ).exclude( id = question.id ).order_by( "-total_upvotes", "-created_date" ).only( "id", "title" )[0:3]
    answers = Answer.objects.filter( question__id = question.id ).order_by( "-total_upvotes", "total_downvotes", "-created_date" )

    answers_ids = list( answer.id for answer in answers )

    upvoted_answers_ids = Vote.objects.filter(
        object_id__in = answers_ids,
        content_type = ContentType.objects.get_for_model( Answer ),
        user_id = request.user.id,
        vote_type__id = settings.QA_VOTE_TYPE_UPVOTE_ID
    ).values_list( "object_id", flat = True )

    downvoted_answers_ids = Vote.objects.filter(
        object_id__in = answers_ids,
        content_type = ContentType.objects.get_for_model( Answer ),
        user_id = request.user.id,
        vote_type__id = settings.QA_VOTE_TYPE_DOWNVOTE_ID
    ).values_list( "object_id", flat = True )

    for answer in answers:
        if answer.id in upvoted_answers_ids:
            answer.is_upvoted = True
        if answer.id in downvoted_answers_ids:
            answer.is_downvoted = True

    # Checks if the user is following the post
    if question.followers.filter( id = request.user.id ).exists():
        question.is_followed = True
    else:
        question.is_followed = False

    # Fills template data
    template_data[ "answers" ] = answers
    template_data[ "related_content" ] = related_content
    template_data[ "answer_form" ] = answer_form
    template_data[ "question" ] = question

    # Print Template
    return render( request, 'qa/question/view.html', template_data )


@login_required
def list_blogposts( request, *args, **kwargs ):
    """
        Handles the process of listing blogposts.
    :param request:
    :return: A template rendered
    """

    # SET UP THE STEP AND THE TOTAL OF STEPS
    step = 0    # starts from the begining
    results_per_step = settings.QA_QUESTIONS_PER_STEP # The number of questions to load per step

    # PROCESS FILTERS
    filter_params = {}

    # Fills up the situation
    from_country = request.session['situation']['from_country']
    to_country = request.session['situation']['to_country']
    goal = request.session['situation']['goal']

    # Fills the topics related to user's situation
    filter_params[ "related_countries_ids" ] = [ from_country.id, to_country.id ]
    filter_params[ "related_goals_ids" ] = [ goal.id ]

    # Get questions per step
    questions = get_questions_by_step( request.user, filter_params, step, results_per_step )

    # TEMPLATE DATA
    template_data = {
        "questions_menu_selected" : True,
        "questions" : questions,
        "next_step" : step + 1,
        "filter_params" : urllib.parse.urlencode( filter_params, True ),
    }

    # Print Template
    return render( request, 'qa/question/list.html', template_data )


@login_required
def add_blogpost( request ):
    """
        Handles the process of adding a blogpost.
    :param request:
    :return: A template rendered
    """
    pass


@login_required
def view_blogpost( request, slug ):
    """
    View a blgopost.
    :param request:
    :param slug:
    :return:
    """
    pass


@login_required
def list_topics( request ):
    """
        Show the topics that the user is following.
    :param request:
    :return: A template rendered
    """
    template_data = {
        "topics_menu_selected" : True,
        "following_topics" : request.user.following_topics.order_by( "name" ).values( "id", "name", "slug" )
    }
    return render( request, 'qa/topic/list.html', template_data )


@login_required
def view_topic( request, slug ):

    topic = get_object_or_404( Topic, slug = slug )
    # SET UP THE STEP AND THE TOTAL OF STEPS
    step = 0    # starts from the begining
    results_per_step = settings.QA_QUESTIONS_PER_STEP # The number of questions to load per step

    # PROCESS FILTERS
    filter_params = {}

    # Fills up the filter with the topic id
    filter_params[ "related_topics_ids" ] = [ topic.id ]

    # Get questions per step
    questions = get_questions_by_step( request.user, filter_params, step, results_per_step )

    # TEMPLATE DATA
    template_data = {
        "questions_menu_selected" : True,
        "questions" : questions,
        "next_step" : step + 1,
        "filter_params" : urllib.parse.urlencode( filter_params, True )
    }

    # Print Template
    return render( request, 'qa/question/list.html', template_data )






########################################
# AJAX CALLS
########################################
def ajax_load_questions( request ):
    """
    Loads questions based on params passed via GET.
    :param request:
    :return:
    """
    # Initializing variables
    filter_params = {}
    results_per_step = settings.QA_QUESTIONS_PER_STEP # The number of questions to load per step
    step = request.GET.get( "step", None )

    # If no step was provided, raise a Not Found error.
    if not step:
        raise Http404( "Not found." )

    # Get filters
    allowed_filters_names = [ "related_topics_ids", "related_countries_ids", "related_goals_ids" ]
    for filter_name in allowed_filters_names:
        if filter_name in request.GET:
            filter_params[ filter_name ] = request.GET.getlist( filter_name )

    # Get questions by step
    questions = get_questions_by_step( request.user, filter_params, int( step ), results_per_step )

    # Render the result and return or raise a Http404 if no questions was found.
    if questions:
        html = render_to_string( "qa/question/list_group.html", { "questions": questions } )
        return HttpResponse( html )
    else:
        raise Http404( "No results found." )


@ajax_login_required
def ajax_get_topics( request ):
    """
    Searchs for topics that matches the GET param "term" and returns a JSON.
    :param request:
    :return:
    """
    if request.is_ajax():
        q = request.GET.get( 'term', '' )
        topics = Topic.objects.filter( name__icontains = q )[:20]
        results = []
        for topic in topics:
            topic_json = {}
            topic_json['id'] = topic.id
            topic_json['view_url'] = reverse( "qa:view_topic", kwargs = { "slug" : topic.slug } )
            topic_json['unfollow_url'] = reverse( "qa:ajax_unfollow_topic", kwargs = { "topic_id" : topic.id } )
            topic_json['follow_url'] = reverse( "qa:ajax_follow_topic", kwargs = { "topic_id" : topic.id } )
            topic_json['value'] = topic.name
            results.append( topic_json )
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


@ajax_login_required
def ajax_follow_topic( request, topic_id ):
    """
        Follows a TOPIC.
    :param request:
    :param post_id: The id of the post to follow/unfollow
    :return: A template rendered
    """
    # Gets the post
    topic = Topic.objects.get( id = topic_id )
    stats, created = UserStats.objects.get_or_create( user_id = request.user.id )

    with transaction.atomic():
        if not topic.followers.filter( id = request.user.id ).exists():
            topic.followers.add( request.user )
            stats.total_topics_following += 1
            topic.save()
            stats.save()

    return HttpResponse( stats.total_topics_following )


@ajax_login_required
def ajax_unfollow_topic( request, topic_id ):
    """
        Follows a TOPIC.
    :param request:
    :param post_id: The id of the post to follow/unfollow
    :param following: True to follow the post, False to unfollow.
    :return: A template rendered
    """
    # Gets the post
    topic = Topic.objects.get( id = topic_id )
    stats, created = UserStats.objects.get_or_create( user_id = request.user.id )

    with transaction.atomic():
        if topic.followers.filter( id = request.user.id ).exists():
            topic.followers.remove( request.user )
            stats.total_topics_following -= 1
            topic.save()
            stats.save()

    return HttpResponse( stats.total_topics_following )


@ajax_login_required
def ajax_toggle_follow_content( request, id, followable_instance ):
    """
    Follows/Unfollows a FollowableContent.
    :param: slug The identifier of the content
    :param: model The model of the content (Question?BlogPost? etc)
    :return: The number of followers of the content.
    """
    # Gets the object
    obj = followable_instance.objects.get( pk = id )
    user_stats, created = UserStats.objects.get_or_create( user_id = request.user.id )

    is_followed = False   # flag indicating if the user is following the obj
    # The name of the field on UserStats that corresponds to the counter of the given FollowableInstance
    instance_counter_field_name = "total_" + followable_instance.__name__.lower() + 's' + "_following"

    with transaction.atomic():
        if not obj.followers.filter( id = request.user.id ).exists():
            # Adds the user to the followers of the content and increments its counter.
            obj.followers.add( request.user )
            obj.total_followers += 1
            # updates the counter for the followable instance on user stats
            user_stats.__dict__[ instance_counter_field_name ] += 1
            # Save the object and the userstats
            obj.save()
            user_stats.save()
            # Set a flag indicating that the user is following the FollowableInstance.
            is_followed = True
        else:
            # Removes the user from the followers of the content and decrements its counter.
            obj.followers.remove( request.user )
            obj.total_followers -= 1
            # updates the counter for the followable instance on user stats
            user_stats.__dict__[ instance_counter_field_name ] -= 1
            # Save the content and the UserStats
            obj.save()
            user_stats.save()
            # Set a flag indicating that the user is not following the FollowableInstance
            is_followed = False

    # Creates a response to the call
    response = {
        "primary_action" : False if is_followed else True,
        "total" : obj.total_followers
    }

    return JsonResponse( response )


@ajax_login_required
def ajax_toggle_upvote_content( request, id, votable_instance ):
    """
    Toggle upvotes on a VotableInstance.
    :param: slug The identifier of the content
    :param: model The model of the content (Question?BlogPost? etc)
    :return: The number of upvotes of the content.
    """
    obj = votable_instance.objects.get( pk = id )

    is_upvoted = False

    # Check if the object was already upvoted
    upvote = Vote.objects.filter(
        object_id = obj.id,
        content_type = ContentType.objects.get_for_model( votable_instance ),
        user_id = request.user.id,
        vote_type__id = settings.QA_VOTE_TYPE_UPVOTE_ID
    ).first()

    # Create or delete the upovte and update counters
    with transaction.atomic():
        if not upvote:
            v = Vote( content_object = obj, user = request.user, vote_type_id = settings.QA_VOTE_TYPE_UPVOTE_ID )
            v.save()
            obj.total_upvotes += 1
            obj.save()
            is_upvoted = True
        else:
            upvote.delete()
            obj.total_upvotes -= 1
            obj.save()
            is_upvoted = False

    # Creates a response to the call
    response = {
        "primary_action" : False if is_upvoted else True,
        "total" : obj.total_upvotes
    }

    return JsonResponse( response )


@ajax_login_required
def ajax_toggle_downvote_content( request, id, votable_instance ):
    """
    Toggle downvotes on a VotableInstance.
    :param: slug The identifier of the content
    :param: model The model of the content (Question?BlogPost? etc)
    :return: The number of upvotes of the content.
    """

    obj = votable_instance.objects.get( pk = id )
    is_downvoted = False

    # Check if the object was already upvoted
    downvote = Vote.objects.filter(
        object_id = obj.id,
        content_type = ContentType.objects.get_for_model( votable_instance ),
        user_id = request.user.id,
        vote_type__id = settings.QA_VOTE_TYPE_DOWNVOTE_ID
    ).first()

    with transaction.atomic():
        if not downvote:
            v = Vote( content_object = obj, user = request.user, vote_type_id = settings.QA_VOTE_TYPE_DOWNVOTE_ID )
            v.save()
            obj.total_downvotes += 1
            obj.save()
            is_downvoted = True
        else:
            downvote.delete()
            obj.total_downvotes -= 1
            obj.save()
            is_downvoted = False

        # Creates a response to the call
    response = {
        "primary_action" : False if is_downvoted else True,
        "total" : obj.total_downvotes
    }

    return JsonResponse( response )
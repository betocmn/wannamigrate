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


##########################
# Methods
##########################
def get_questions_by_step( user, filter_params, step, results_per_step ):

    # Limits
    start = results_per_step * step
    end = results_per_step * step + results_per_step

    # Search the Posts with filters
    questions = Question.objects.get_listing( **filter_params )[ start : end ]

    # If the user is authenticated
    if user.is_authenticated():
        # Checks if the user is following the posts
        question_ids = list( question.id for question in questions )
        following_posts = Question.objects.filter( id__in = question_ids, followers__id = user.id ).values_list( "id", flat=True )
        for question in questions:
            if question.id in following_posts:
                question.is_followed = True
            else:
                question.is_followed = False

    return questions



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
    }

    # Print Template
    return render( request, 'qa/question/list.html', template_data )



def list_posts( request, *args, **kwargs ):
    pass

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
    template_data = {}

    question = Question.objects.get( slug = slug )
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
def view_post( request, post_id ):
    """
        Handles the process of viewing a question.
    :param request:
    :param post_id: The id of the post to viewing
    :return: A template rendered
    """
    template_data = {}

    post = Post.objects.get( pk = post_id  )
    post.views_count = post.views_count + 1
    post.save()

    # Gets the answer form
    answer_form = AddAnswerForm( request.POST or None, owner = request.user, parent = post )
    if answer_form.is_valid():
        answer = answer_form.save()
        messages.success( request, _( '{0} successfully created.'.format( answer.post_type.name ) ) )
        return HttpResponseRedirect( reverse( "qa:view_post", kwargs={ "post_id" : post_id } ) + "#answer_{0}".format( answer.id ) )

    related_content = Post.objects.filter( related_topics__in = post.related_topics.all() ).exclude( id = post_id ).only( "id", "title" )[0:3]
    answers = Post.objects.filter( parent__id = post_id ).order_by( "-upvotes_count", "-created_date" )

    # Checks if the user is following the post
    if post.followers.filter( id = request.user.id ).exists():
        post.is_followed = True
    else:
        post.is_followed = False


    # Fills template data
    template_data[ "answers" ] = answers
    template_data[ "related_content" ] = related_content
    template_data[ "answer_form" ] = answer_form
    template_data[ "post" ] = post

    # Print Template
    return render( request, 'qa/posts/view.html', template_data )

    """

    template_data[ "post" ] = post
    template_data[ "answers" ] = answers

    template_data[ "answers" ] =

    # Print Template
    return render( request, 'qa/posts/view.html', template_data )

    """


@ajax_login_required
def toggle_follow( request, id, followable_instance ):
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
def toggle_upvote( request, id, votable_instance ):
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
def toggle_downvote( request, id, votable_instance ):
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


@ajax_login_required
def set_following_post( request, post_id, follow = False ):
    """
        Follows or unfollows a post.
    :param request:
    :param post_id: The id of the post to follow/unfollow
    :param following: True to follow the post, False to unfollow.
    :return: A template rendered
    """
    # Gets the post
    post = Post.objects.get( id = post_id )
    stats, created = UserStats.objects.get_or_create( user_id = request.user.id )

    with transaction.atomic():
        if follow:
            if not post.followers.filter( id = request.user.id ).exists():
                post.followers.add( request.user )
                post.followers_count += 1
                stats.total_posts_following += 1
                post.save()
                stats.save()
        else:
            if post.followers.filter( id = request.user.id ).exists():
                post.followers.remove( request.user )
                post.followers_count -= 1
                stats.total_posts_following -= 1
                post.save()
                stats.save()

    return HttpResponse( post.followers_count )


@ajax_login_required
def set_upvote_post( request, post_id, upvote = False ):
    """
        Upvote or downvote a post.
    :param request:
    :param post_id: The id of the post to follow/unfollow
    :param upvote: True to upvote the post, False to downvote.
    :return: A template rendered
    """
    post = Post.objects.get( id = post_id )

    upvoted = Vote.objects.filter(
        post_id = post_id,
        user_id = request.user.id,
        vote_type__id = settings.QA_VOTE_TYPE_UPVOTE_ID
    ).first()

    downvoted = Vote.objects.filter(
        post_id = post_id,
        user_id = request.user.id,
        vote_type__id = settings.QA_VOTE_TYPE_DOWNVOTE_ID
    ).first()

    with transaction.atomic():
        if upvote: # UPVOTING
            # Delete the downvote if exists
            if downvoted:
                downvoted.delete()
                post.upvotes_count += 1 # Do the mahts... downvote = -upvote -> -downvote = -(-upvote) -> -downvote = +upvote

            # The post wasn't upvoted yet?
            if not upvoted:
                # Creates the upvote
                v = Vote.objects.create( post_id = post_id, user_id = request.user.id, vote_type_id = settings.QA_VOTE_TYPE_UPVOTE_ID )

                # Increments the upvotes counter of the post
                post.upvotes_count += 1
                post.save()
        else:   # DOWNVOTING
            # Delete the upvote if exists
            if upvoted:
                upvoted.delete()
                post.upvotes_count -= 1 # Do the mahts...

            # The post wasn't downvoted yet?
            if not downvoted:
                # Creates the downvote
                v = Vote.objects.create( post_id = post_id, user_id = request.user.id, vote_type_id = settings.QA_VOTE_TYPE_DOWNVOTE_ID )

                # Decrements the upvotes counter of the post
                post.upvotes_count -= 1
                post.save()

    return HttpResponse( post.upvotes_count )


@login_required
def list_topics( request ):
    """
        Show the topics that the user is following.
    :param request:
    :return: A template rendered
    """
    template_data = {
        "topics_menu_selected" : True,
        "topics" : Topic.objects.values( "id", "name" )
    }
    return render( request, 'qa/topics/list.html', template_data )



@ajax_login_required
def ajax_load_questions( request ):
    """ Searchs for topics that matches the GET param "term" and returns a JSON.
    :param request:
    :return:
    """

    # SET UP STEP AND TOTAL RESULTS PER STEP
    step = int( request.GET.get( 'step', 0 ) ) # starts from the begining
    results_per_step = settings.QA_QUESTIONS_PER_STEP # The number of questions to load per step

    # FILTERS
    filter_params = {}

    # Fills up the situation
    from_country = request.session['situation']['from_country']
    to_country = request.session['situation']['to_country']
    goal = request.session['situation']['goal']

    # Fills the topics related to user's situation
    filter_params[ "related_countries_ids" ] = [ from_country.id, to_country.id ]
    filter_params[ "related_goals_ids" ] = [ goal.id ]

    # Get questions
    questions = get_questions_by_step( request.user, filter_params, step, results_per_step )

    if questions:
        # Render to string
        html = render_to_string( "qa/question/list_group.html", { "questions": questions } )
        return HttpResponse( html )
    else:
        raise Http404( "No results found." )


@ajax_login_required
def ajax_get_topics( request ):
    """ Searchs for topics that matches the GET param "term" and returns a JSON.
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
def ajax_set_following_topic( request, topic_id, follow = False ):
    """
        Follows or unfollows a TOPIC.
    :param request:
    :param post_id: The id of the post to follow/unfollow
    :param following: True to follow the post, False to unfollow.
    :return: A template rendered
    """
    # Gets the post
    topic = Topic.objects.get( id = topic_id )
    stats, created = UserStats.objects.get_or_create( user_id = request.user.id )

    with transaction.atomic():
        if follow:
            if not topic.followers.filter( id = request.user.id ).exists():
                topic.followers.add( request.user )
                stats.total_topics_following += 1
                topic.save()
                stats.save()
        else:
            if topic.followers.filter( id = request.user.id ).exists():
                topic.followers.remove( request.user )
                stats.total_topics_following -= 1
                topic.save()
                stats.save()

    return HttpResponse( stats.total_topics_following )
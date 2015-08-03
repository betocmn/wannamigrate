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
from django.utils.text import Truncator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse, HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from wannamigrate.core.decorators import ajax_login_required
from wannamigrate.site.views import get_situation_form
from django.core.urlresolvers import reverse
from django.contrib import messages
from wannamigrate.qa.forms import (
    AddQuestionForm, AddBlogPostForm, AddAnswerForm
)
from wannamigrate.core.tasks import add_notification
from wannamigrate.qa.models import BlogPost, Question, Answer, Vote, Topic, TopicTranslation
from wannamigrate.core.models import(
    UserStats, Language
)
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils import translation
from django.db import transaction
import json
import urllib
from django.db.models import F
from wannamigrate.qa.util import get_questions_by_step, get_blogposts_by_step
from django.templatetags.static import static





##########################
# HTTP Methods
##########################
def list_all( request, *args, **kwargs ):
    """
    Lists all contents (questions and blogposts).
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    # SET UP THE STEP AND THE TOTAL OF STEPS
    step = 0    # starts from the begining
    results_per_step = settings.QA_QUESTIONS_PER_STEP # The number of questions to load per step
    # Gets the language
    language = Language.objects.filter( code = request.LANGUAGE_CODE ).get()

    # PROCESS FILTERS
    filter_params = {}

    # Fills up the situation

    # Fills the topics related to user's situation
    filter_params[ "related_countries_ids" ] = [ request.session['situation']['to_country']['id'] ]
    filter_params[ "related_goals_ids" ] = [ request.session['situation']['goal']['id'] ]
    filter_params[ "language_ids" ] = [ language.id ]

    # Get questions per step
    questions = get_questions_by_step( request, filter_params, step, results_per_step )
    blogposts = get_blogposts_by_step( request, filter_params, step, results_per_step )
    for post in blogposts:
        post.user_slug = settings.QA_ANONYMOUS_USER_SLUG if post.is_anonymous else post.owner.slug

    # Join two querysets
    contents = [ x for x in questions ]
    contents += [ x for x in blogposts ]

    # Sorts elements
    contents.sort( key=lambda x: x.last_activity_date, reverse=True )

    # TEMPLATE DATA
    template_data = {
        "situation_form" : get_situation_form( request ),
        "meta_title" : _( 'Knowledge - Wanna Migrate' ),
        "knowledge_menu_selected" : True,
        "contents" : contents,
        "next_step" : step + 1,
        "filter_params" : urllib.parse.urlencode( filter_params, True ),
    }

    # Print Template
    return render( request, 'qa/common/list_all.html', template_data )



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
    language = Language.objects.filter( code = request.LANGUAGE_CODE ).get()

    # Fills the topics related to user's situation
    filter_params[ "related_countries_ids" ] = [ request.session['situation']['to_country']['id'] ]
    filter_params[ "related_goals_ids" ] = [ request.session['situation']['goal']['id'] ]
    filter_params[ "language_ids" ] = [ language.id ]

    # Get questions per step
    questions = get_questions_by_step( request, filter_params, step, results_per_step )

    # TEMPLATE DATA
    template_data = {
        "situation_form" : get_situation_form( request ),
        "meta_title" : _( 'Questions & Answers - Wanna Migrate' ),
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

    defaults = {}
    if "q" in request.GET:
        defaults['title'] = request.GET['q']

    # Instantiate FORM
    form = AddQuestionForm( request.POST or None, owner = request.user, initial = defaults, language = Language.objects.filter( code = request.LANGUAGE_CODE ).get() )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        # Saves the post
        with transaction.atomic():
            question = form.save()
            user_stats, created = UserStats.objects.get_or_create( user_id = request.user.id )
            question.followers.add( request.user )
            question.total_followers += 1
            user_stats.total_questions_following += 1

            question.save()
            user_stats.save()

            messages.success( request, 'Question successfully created.' )
            # Redirect with success message
            return HttpResponseRedirect( reverse( 'qa:view_question', args = ( question.slug, ) ) )

    # Template data
    template_data = {
        "situation_form" : get_situation_form( request ),
        "meta_title" : _( 'Add Question - Wanna Migrate' ),
        'form': form,
        'cancel_url': reverse( 'qa:list_questions' ),
        'topics' : Topic.objects.order_by( "name" ).values( "id", "name" ),
    }

    # Print Template
    return render( request, 'qa/question/add_question.html', template_data )



#@login_required
def view_question( request, slug ):
    """
    Question view. Shows a question and its answers.
    :param request:
    :param slug: The identifier of the question.
    :return:
    """
    template_data = {}

    question = get_object_or_404( Question.objects.prefetch_related( "related_topics"), slug = slug )
    question.total_views += 1
    question.save()

    ###############################
    # Process topic translation
    ###############################
    topics_ids = [x.id for x in question.related_topics.all()]
    temp = TopicTranslation.objects.filter( language__code = request.LANGUAGE_CODE, topic__id__in = topics_ids ).all()
    translations = {}
    for t in temp:
        translations[ t.topic_id ] = t
    for t in question.related_topics.all():
        if t.id in translations:
            t.name = translations[ t.id ].name
            t.slug = translations[ t.id ].slug

    # Gets the answer form
    if request.user.is_authenticated():
        answer_form = AddAnswerForm( request.POST or None, owner = request.user, question = question )

        if answer_form.is_valid():
            with transaction.atomic():
                user_stats, created = UserStats.objects.get_or_create( user_id = request.user.id )
                user_stats.total_answers += 1
                answer = answer_form.save()
                user_stats.save()
                messages.success( request, _( 'Answer successfully created.' ) )

                # Adds a notification to the users following the question, using a CELERY task
                add_notification.delay(
                    "{{{New answer to the question}}} " + '"' + Truncator( question.title ).words( 6 ) + '"',
                    reverse( "qa:view_question", kwargs={ "slug" : slug } ) + "#answer_{0}".format( answer.id ),
                    list( question.followers.all() ),
                    True
                )

                return HttpResponseRedirect( reverse( "qa:view_question", kwargs={ "slug" : slug } ) + "#answer_{0}".format( answer.id ) )

    # Get related contents
    related_content = Question.objects.filter( related_topics__in = question.related_topics.all() )\
        .exclude( id = question.id )\
        .order_by( "-total_upvotes", "-created_date" )\
        .only( "id", "title", "slug" )[0:3]

    # Get answers
    answers = Answer.objects.filter( question__id = question.id )\
        .select_related( "owner" )\
        .prefetch_related( "owner__provider_set", "owner__userpersonal" )\
        .order_by( "-total_upvotes", "total_downvotes", "-created_date" )

    if request.user.is_authenticated():
        answers_ids = list( answer.id for answer in answers )

        # Get upvoted answers
        upvoted_answers_ids = Vote.objects.filter(
            object_id__in = answers_ids,
            content_type = ContentType.objects.get_for_model( Answer ),
            user_id = request.user.id,
            vote_type__id = settings.QA_VOTE_TYPE_UPVOTE_ID
        ).values_list( "object_id", flat = True )

        # Get downvoted answers
        downvoted_answers_ids = Vote.objects.filter(
            object_id__in = answers_ids,
            content_type = ContentType.objects.get_for_model( Answer ),
            user_id = request.user.id,
            vote_type__id = settings.QA_VOTE_TYPE_DOWNVOTE_ID
        ).values_list( "object_id", flat = True )

        # extra processing
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


    for answer in answers:
        answer.klass = "" if answer.owner.provider_set.exists() else "commom"


    # Fills template data
    template_data['situation_form'] = get_situation_form( request )
    template_data['meta_title'] = question.title
    template_data[ "answers" ] = answers
    template_data[ "related_content" ] = related_content
    template_data[ "is_authenticated" ] = request.user.is_authenticated()
    template_data[ "answer_form" ] = answer_form if request.user.is_authenticated() else None
    template_data[ "question" ] = question

    # Print Template
    return render( request, 'qa/question/view.html', template_data )

#    from wannamigrate.core.util import debug_sql
#    return debug_sql()



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
    language = Language.objects.filter( code = request.LANGUAGE_CODE ).get()

    # Fills the topics related to user's situation
    filter_params[ "related_countries_ids" ] = [ request.session['situation']['to_country']['id'] ]
    filter_params[ "related_goals_ids" ] = [ request.session['situation']['goal']['id'] ]
    filter_params[ "language_ids" ] = [ language.id ]

    # Get questions per step
    blogposts = get_blogposts_by_step( request, filter_params, step, results_per_step )
    for post in blogposts:
        post.user_slug = settings.QA_ANONYMOUS_USER_SLUG if post.is_anonymous else post.owner.slug


    # TEMPLATE DATA
    template_data = {
        "situation_form" : get_situation_form( request ),
        "meta_title" : _( 'Blog Posts - Wanna Migrate' ),
        "blogposts_menu_selected" : True,
        "blogposts" : blogposts,
        "next_step" : step + 1,
        "filter_params" : urllib.parse.urlencode( filter_params, True ),
    }

    # Print Template
    return render( request, 'qa/blogpost/list.html', template_data )



@login_required
def add_blogpost( request ):
    """
        Handles the process of adding a blogpost.
    :param request:
    :return: A template rendered
    """

    # Instantiate FORM
    form = AddBlogPostForm( request.POST or None, owner = request.user, language = Language.objects.filter( code = request.LANGUAGE_CODE ).get() )


    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        # Saves the post
        with transaction.atomic():
            blogpost = form.save()
            user_stats, created = UserStats.objects.get_or_create( user_id = request.user.id )
            blogpost.followers.add( request.user )
            blogpost.total_followers += 1
            user_stats.total_questions_following += 1

            blogpost.save()
            user_stats.save()

            user_slug = settings.QA_ANONYMOUS_USER_SLUG if blogpost.is_anonymous else request.user.slug

            messages.success( request, _( 'Post successfully created.' ) )

            # notify the followers of the user
            if request.user.followers.count():
                add_notification.delay(
                    request.user.name + " {{{wrote a new post}}}",
                    reverse( 'qa:view_blogpost', args = ( user_slug, blogpost.slug, ) ),
                    list( request.user.followers.all() ),
                    True
                )


            # Redirect with success message
            return HttpResponseRedirect( reverse( 'qa:view_blogpost', args = ( user_slug, blogpost.slug, ) ) )

    # Template data
    template_data = {
        "situation_form" : get_situation_form( request ),
        "meta_title" : _( 'Add Blog Post - Wanna Migrate' ),
        'form': form,
        'cancel_url': reverse( 'qa:list_blogposts' ),
        'topics' : Topic.objects.order_by( "name" ).values( "id", "name" ),
    }

    # Print Template
    return render( request, 'qa/blogpost/add.html', template_data )




def view_blogpost_old( request, slug ):
    blogpost = get_object_or_404( BlogPost.objects.prefetch_related( "owner" ), slug = slug )
    if blogpost.is_anonymous == False:
        return redirect( reverse( 'qa:view_blogpost', args = ( blogpost.owner.slug, blogpost.slug, ), ), permanent = True )
    else:
        return redirect( reverse( 'qa:view_blogpost', args = ( settings.QA_ANONYMOUS_USER_SLUG, blogpost.slug, ), ), permanent = True )



def view_blogpost( request, user_slug, slug ):
    """
    BlogPost view. Shows a blogpost and its comments.
    :param request:
    :param slug: The identifier of the question.
    :return:
    """
    template_data = {}

    # Identifies blog post and increments number of views
    blogpost = get_object_or_404( BlogPost.objects.prefetch_related( "related_topics", "owner" ), slug = slug )


    if ( blogpost.is_anonymous and user_slug != settings.QA_ANONYMOUS_USER_SLUG ) or \
            ( blogpost.is_anonymous == False and user_slug != blogpost.owner.slug ):
        raise Http404( "No BlogPost matches the given query." )

    blogpost.total_views += 1
    blogpost.save()

    # Sets image as preview for sharing (as for facebook, twitter, etc.)
    # TODO: This is "gambiarra". After image support is added to posts, change this code to
    # automatically get one image from the HTML posted (if any).
    if blogpost.id == 1:
        template_data['meta_image'] = settings.BASE_URL + static( 'site/img/share-image-post-wanna-migrate.png' )
    elif blogpost.id == 2:
        template_data['meta_image'] = settings.BASE_URL + static( 'site/img/share-image-post-wanna-migrate-2.jpg' )
    elif blogpost.id == 3:
        template_data['meta_image'] = settings.BASE_URL + static( 'site/img/share-image-post-wanna-migrate-3.jpg' )
    elif blogpost.id == 4:
        template_data['meta_image'] = settings.BASE_URL + static( 'site/img/share-image-post-wanna-migrate-4.jpg' )


    ###############################
    # Process topic translation
    ###############################
    topics_ids = [x.id for x in blogpost.related_topics.all()]
    temp = TopicTranslation.objects.filter( language__code = request.LANGUAGE_CODE, topic__id__in = topics_ids ).all()
    translations = {}
    for t in temp:
        translations[ t.topic_id ] = t
    for t in blogpost.related_topics.all():
        if t.id in translations:
            t.name = translations[ t.id ].name
            t.slug = translations[ t.id ].slug

    related_content = BlogPost.objects.filter( related_topics__in = blogpost.related_topics.all() ).exclude( id = blogpost.id ).prefetch_related( "owner" ).order_by( "-total_upvotes", "-created_date" ).only( "id", "title", "owner" )[0:3]

    for rc in related_content:
        rc.user_slug = settings.QA_ANONYMOUS_USER_SLUG if rc.is_anonymous else rc.owner.slug

    # Checks if the user has upvoted or downvoted the post
    blogpost.is_upvoted = Vote.objects.filter(
        object_id = blogpost.id,
        content_type = ContentType.objects.get_for_model( BlogPost),
        user_id = request.user.id,
        vote_type__id = settings.QA_VOTE_TYPE_UPVOTE_ID
    ).exists()

    blogpost.is_downvoted = Vote.objects.filter(
        object_id = blogpost.id,
        content_type = ContentType.objects.get_for_model( BlogPost),
        user_id = request.user.id,
        vote_type__id = settings.QA_VOTE_TYPE_DOWNVOTE_ID
    ).exists()


    # Fills template data
    template_data['situation_form'] = get_situation_form( request )
    template_data['meta_title'] = blogpost.title
    template_data[ "related_content" ] = related_content
    template_data[ "blogpost" ] = blogpost

    # Print Template
    return render( request, 'qa/blogpost/view.html', template_data )



@login_required
def list_topics( request ):
    """
        Show the topics that the user is following.
    :param request:
    :return: A template rendered
    """

    translations = TopicTranslation.objects.filter( topic__in=request.user.following_topics.all() ).order_by( "name" ).only( "topic", "name", "slug" )

    for t in translations:
        t.id = t.topic_id

    template_data = {
        "situation_form" : get_situation_form( request ),
        "meta_title" : _( 'Topics - Wanna Migrate' ),
        "topics_menu_selected" : True,
        "following_topics" : translations
    }
    return render( request, 'qa/topic/list.html', template_data )



@login_required
def view_topic( request, slug ):

    topic = get_object_or_404( TopicTranslation, slug = slug, language__code = request.LANGUAGE_CODE ).topic
    # SET UP THE STEP AND THE TOTAL OF STEPS
    step = 0    # starts from the begining
    results_per_step = settings.QA_QUESTIONS_PER_STEP # The number of questions to load per step
    # Gets the language
    language = Language.objects.filter( code = request.LANGUAGE_CODE ).get()


    # PROCESS FILTERS
    filter_params = {}

    # Fills up the filter with the topic id
    filter_params[ "related_topics_ids" ] = [ topic.id ]
    filter_params[ "language_ids" ] = [ language.id ]

    # Get questions per step
    questions = get_questions_by_step( request, filter_params, step, results_per_step )

    # TEMPLATE DATA
    template_data = {
        "situation_form" : get_situation_form( request ),
        "meta_title" : topic.name,
        "questions_menu_selected" : True,
        "questions" : questions,
        "next_step" : step + 1,
        "filter_params" : urllib.parse.urlencode( filter_params, True )
    }

    # Print Template
    return render( request, 'qa/question/list.html', template_data )





@login_required
def list_answers( request ):
    """
        Lists all answers of the user.
    :param request:
    :return: A template rendered
    """

    # Gets all the answers of the user (including anonymous answers).
    answers = Answer.objects.filter( owner = request.user ).prefetch_related( "question" ).all()

    # Process the answers to properly display on view.
    processed_answers = [ { "title" : x.question.title, "body" : x.body, "url" : reverse( "qa:view_question", kwargs={ "slug" : x.question.slug } ) + "#answer_{0}".format( x.id )  } for x in answers ]

    # Fills template_data
    template_data = {
        "meta_title" : _( 'My answers - Wanna Migrate' ),
        "contents" : processed_answers,
        "answers_menu_selected" : True,
        "special_title" : _( "My answers" ),
    }
    return render( request, "qa/common/title_body_container.html", template_data )


@login_required
def reading_list( request ):
    """
        Lists all favourited questions of the user.
    :param request:
    :return: A template rendered
    """
    raise Http404( "Not implemented" )



@login_required
def list_following( request ):
    following = request.user.following.prefetch_related( "userpersonal" ).all()
    processed_following = [ { "name" : x.name, "avatar" : x.userpersonal.avatar.thumbnail.url if x.userpersonal.avatar else None, "url" : reverse( "site:user_profile", kwargs={ "slug" : x.slug } ) } for x in following ]

    template_data = {
        "meta_title" : _( 'Following - Wanna Migrate' ),
        "contents" : processed_following,
        "following_menu_selected" : True,
        "special_title" : _( "Following" ),
    }

    return render( request, "qa/common/avatar_name_container.html", template_data )


def list_followers( request ):
    followers = request.user.followers.prefetch_related( "userpersonal" ).all()
    processed_followers = [ { "name" : x.name, "avatar" : x.userpersonal.avatar.thumbnail.url if x.userpersonal.avatar else None, "url" : reverse( "site:user_profile", kwargs={ "slug" : x.slug } ) } for x in followers ]

    template_data = {
        "meta_title" : _( 'Following - Wanna Migrate' ),
        "contents" : processed_followers,
        "followers_menu_selected" : True,
        "special_title" : _( "Followers" ),
    }

    return render( request, "qa/common/avatar_name_container.html", template_data )



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
    allowed_filters_names = [ "related_topics_ids", "related_countries_ids", "related_goals_ids", "language_ids" ]
    for filter_name in allowed_filters_names:
        if filter_name in request.GET:
            filter_params[ filter_name ] = request.GET.getlist( filter_name )

    # Get questions by step
    questions = get_questions_by_step( request, filter_params, int( step ), results_per_step )

    # Render the result and return or raise a Http404 if no questions was found.
    if questions:
        html = render_to_string( "qa/question/list_group.html", { "questions": questions } )
        return HttpResponse( html )
    else:
        raise Http404( "No results found." )


def ajax_load_blogposts( request ):
    """
    Loads blogposts based on params passed via GET.
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
    allowed_filters_names = [ "related_topics_ids", "related_countries_ids", "related_goals_ids", "language_ids" ]
    for filter_name in allowed_filters_names:
        if filter_name in request.GET:
            filter_params[ filter_name ] = request.GET.getlist( filter_name )

    # Get questions by step
    blogposts = get_blogposts_by_step( request, filter_params, int( step ), results_per_step )
    for post in blogposts:
        post.user_slug = settings.QA_ANONYMOUS_USER_SLUG if post.is_anonymous else post.owner.slug

    # Render the result and return or raise a Http404 if no questions was found.
    if blogposts:
        html = render_to_string( "qa/blogpost/list_group.html", { "blogposts": blogposts } )
        return HttpResponse( html )
    else:
        raise Http404( "No results found." )


def ajax_load_all( request ):
    """
    Loads all based on params passed via GET.
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
    allowed_filters_names = [ "related_topics_ids", "related_countries_ids", "related_goals_ids", "language_ids" ]
    for filter_name in allowed_filters_names:
        if filter_name in request.GET:
            filter_params[ filter_name ] = request.GET.getlist( filter_name )

    # Get questions by step
    questions = get_questions_by_step( request, filter_params, int( step ), results_per_step )
    blogposts = get_blogposts_by_step( request, filter_params, int( step ), results_per_step )

    contents = [x for x in questions]
    contents += [x for x in blogposts]

    # Sorts elements
    contents.sort( key=lambda x: x.last_activity_date, reverse=True )

    # Render the result and return or raise a Http404 if no questions was found.
    if len( contents ) > 0:
        html = render_to_string( "qa/common/list_group_all.html", { "contents": contents } )
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
        topics_translations = TopicTranslation.objects.filter( language__code = request.LANGUAGE_CODE, name__icontains = q )[:10]
        results = []
        for t in topics_translations :
            topic_json = {}
            topic_json['id'] = t.topic.id
            topic_json['view_url'] = reverse( "qa:view_topic", kwargs = { "slug" : t.slug } )
            topic_json['unfollow_url'] = reverse( "qa:ajax_unfollow_topic", kwargs = { "topic_id" : t.topic.id } )
            topic_json['follow_url'] = reverse( "qa:ajax_follow_topic", kwargs = { "topic_id" : t.topic.id } )
            topic_json['value'] = t.name
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


    # Generates a notification to owner of the content
    # if the content was upvoted.
    if is_upvoted:
        if votable_instance == Question:
            add_notification.delay(
                request.user.name + " {{{liked your question}}}.",
                reverse( 'qa:view_question', args = ( obj.slug, ) ),
                obj.owner,
                False
            )
        elif votable_instance == Answer:
            add_notification.delay(
                request.user.name + " {{{liked your answer}}}.",
                reverse( "qa:view_question", kwargs={ "slug" : obj.question.slug } ) + "#answer_{0}".format( obj.id ),
                obj.owner,
                False
            )
        elif votable_instance == BlogPost:
            user_slug = settings.QA_ANONYMOUS_USER_SLUG if obj.is_anonymous else obj.owner.slug
            add_notification.delay(
                request.user.name + " {{{liked your post}}}.",
                reverse( 'qa:view_blogpost', args = ( user_slug, obj.slug, ) ),
                obj.owner,
                False
            )

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
from wannamigrate.qa.models import Topic, TopicTranslation, Question, BlogPost
##########################
# NON HTTP METHODS
##########################
def get_content_by_step( instance, request, filter_params, step, results_per_step ):
    """
    Returns a list of contents specified by instance filtered by filter_params. The results are limited by step and results_per_step
    :param instance: The model to lookup
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
    posts = instance.objects.get_listing( **filter_params )[ start : end ]

    ############################################
    # Process the translations for each topic
    ############################################
    topics_ids = []
    for q in posts:
        for t in q.related_topics.all():
            topics_ids.append( t.id )
    temp = TopicTranslation.objects.filter( language__code = request.LANGUAGE_CODE, topic__id__in = topics_ids ).all()
    translations = {}
    for t in temp:
        translations[ t.topic_id ] = t
    for q in posts:
        for t in q.related_topics.all():
            if t.id in translations:
                t.name = translations[ t.id ].name
                t.slug = translations[ t.id ].slug

    ######################################
    # Process if the user is following the contents
    ######################################
    if request.user.is_authenticated():
        # Checks if the user is following the question
        posts_ids = list( post.id for post in posts )
        following_posts = instance.objects.filter( id__in = posts_ids, followers__id = request.user.id ).values_list( "id", flat=True )
        for post in posts:
            if post.id in following_posts:
                post.is_followed = True
            else:
                post.is_followed = False

    return posts


# Shortcut method to query questions
def get_questions_by_step( request, filter_params, step, results_per_step ):
    return get_content_by_step( Question, request, filter_params, step, results_per_step )


# Shortcut method to query blogposts
def get_blogposts_by_step( request, filter_params, step, results_per_step ):
    return get_content_by_step( BlogPost, request, filter_params, step, results_per_step )

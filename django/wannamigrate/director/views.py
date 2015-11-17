##################
# Imports
##################
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from wannamigrate.director.models import Mission, Objective, MissionsObjectives
from wannamigrate.site.views import get_situation_form
from django.utils.module_loading import import_string





# Create your views here.
@login_required
def dashboard( request ):
    """
    Process the dashboard page of the Wanna Cademy module.
    """

    # Initial template
    template_data = {}

    # Gets the country/goal config from situation
    to_country_id = request.session[ "situation" ]["to_country"][ "id" ]
    goal_id = request.session[ "situation" ]["goal"][ "id" ]

    # Gets the missions for the situation
    missions = Mission.objects.filter( to_country_id = to_country_id, goal_id = goal_id ).order_by( "order" ).all()

    # Gets the objectives for the missions
    missions_objectives = MissionsObjectives.objects.filter( mission__in = missions ).order_by( "order" ).all()
    for mo in missions_objectives:
        for m in missions:
            if m.id == mo.mission.id:
                mo.objective.optional = mo.optional
                if not hasattr( m, 'objectives_set'):
                    m.objectives_set = []
                m.objectives_set.append( mo.objective )


    # Calculates the general progress of this user
    general_progress = 0
    n_objectives = 0

    # Gets the percenage of the user foreach objective
    for m in missions:
        for o in m.objectives_set:
            # Loads the content from the objective
            module = o.content_module
            content_object = o.content_object

            # Loads the render method from the current content module.
            views_path = '.'.join( [ __package__, '_modules', module, 'views' ] )
            dynamic_get_progress = import_string( '.'.join( [ views_path, "get_progress" ] ) )

            # Renders and asign the result to content
            o.progress = dynamic_get_progress( request, content_object )
            general_progress += o.progress
            n_objectives += 1

    if ( n_objectives > 0 ):
        general_progress /= n_objectives

    template_data[ "subscription" ] = 'subscription' in request.session and request.session['subscription']
    template_data[ "missions" ] = missions
    template_data[ "general_progress" ] = int( general_progress )
    template_data[ "situation_form" ] = get_situation_form( request )


    return render( request, 'director/dashboard.html', template_data )



def view( request, mission_hash, objective_hash ):
    """
    Shows the content of an objective.
    :param mission_id: The id of the mission being acomplished.
    :param objective_id: The id of the objective being acomplished.
    """

    # Gets the mission and objective being visualized
    mission = get_object_or_404( Mission, hash = mission_hash )
    objective = get_object_or_404( Objective, hash = objective_hash )


    # If there's no active subscription, and the objective is not public, redirect.
    no_subscription = 'subscription' not in request.session or request.session['subscription'] is None
    if not objective.is_public and no_subscription:
        return HttpResponseRedirect( reverse( "site:premium" ) )

    # Loads the content from the objective
    module = objective.content_module
    content_object = objective.content_object


    # Loads the render method from the current content module.
    views_path = '.'.join( [ __package__, '_modules', module, 'views' ] )
    dynamic_render = import_string( '.'.join( [ views_path, "render" ] ) )

    # Renders and asign the result to content
    content = dynamic_render( request, content_object )  # call f passing the content object. It should return a template rendered.

    # If content is an redirection, redirects the page instead of rendering it.
    if isinstance( content, ( HttpResponse, HttpResponseRedirect ) ):
        return content

    # Sets the template data passing the content rendererd.
    template_data = {
        "mission" : mission,
        "objective" : objective,
        "content" : content,
    }

    # render
    return render( request, 'director/view.html', template_data )
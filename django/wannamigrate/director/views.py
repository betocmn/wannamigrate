##################
# Imports
##################
from django.template.loader import render_to_string
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from wannamigrate.director.models import Mission, Objective, MissionsObjectives, SituationsMissions
from django.db.models import Prefetch, Count
from django.conf import settings
from django.utils.module_loading import import_string



# Create your views here.
@login_required
def dashboard( request ):
    """
    Process the dashboard page of the Wanna Cademy module.
    """

    # Initial template
    template_data = {}

    # Gets the situation id of the user.
    situation_id = request.session[ "situation" ][ "id" ]

    # Gets the missions for the situation
    missions = []
    situations_missions = SituationsMissions.objects.filter( situation__id = situation_id ).order_by( "order" ).all()
    for x in situations_missions:
        x.mission.objectives_set = []
        missions.append( x.mission )


    # Gets the objectives for the missions
    missions_objectives = MissionsObjectives.objects.filter( mission__in = missions ).order_by( "order" ).all()
    for mo in missions_objectives:
        for m in missions:
            if m.id == mo.mission.id:
                mo.objective.optional = mo.optional
                m.objectives_set.append( mo.objective )



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

    template_data[ "missions" ] = missions

    return render( request, 'director/dashboard.html', template_data )



def view( request, mission_id, objective_id ):
    """
    Shows the content of an objective.
    :param mission_id: The id of the mission being acomplished.
    :param objective_id: The id of the objective being acomplished.
    """
    # Gets the mission and objective being visualized
    mission = get_object_or_404( Mission, pk = mission_id )
    objective = get_object_or_404( Objective, pk = objective_id )


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
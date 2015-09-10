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

    template_data[ "missions" ] = missions

    return render( request, 'director/dashboard.html', template_data )



def view( request, mission_id, objective_id ):
    """
    Shows the content of an objective.
    :param mission_id: The id of the mission being acomplished.
    :param objective_id: The id of the objective being acomplished.
    """
    # Gets the objects
    mission = get_object_or_404( Mission, pk = mission_id )
    objective = get_object_or_404( Objective, pk = objective_id )

    # Sets the template data.
    template_data = {
        "mission" : mission,
        "objective" : objective,
    }

    # render
    return render( request, 'director/view.html', template_data )
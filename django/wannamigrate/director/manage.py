from wannamigrate.core.models import Situation
from wannamigrate.director.models import Mission, Objective, MissionsObjectives, SituationsMissions
from wannamigrate.director._modules.form_content.models import FormContent, FormContentChoice
from wannamigrate.director._modules.generic_container.models import GenericContainer, GenericContainerContent
from wannamigrate.director._modules.redirect_content.models import RedirectContent
from wannamigrate.director._modules.iframe_content.models import IframeContent
from wannamigrate.director._modules.html_content.models import HtmlContent
from django.contrib.contenttypes.models import ContentType


def process_iframe( content ):
    print( "Processing iframe" )
    iframe = IframeContent( url = content["url"] )
    iframe.save()
    return ( iframe.id, ContentType.objects.get_for_model( IframeContent ) )


def process_redirect( content ):
    print( "Processing redirect" )
    redirect = RedirectContent( url = content["url"], blank = content["blank"] )
    if ( content[ "progress_url" ] ):
        redirect.progress_url = content[ "progress_url" ]
    redirect.save()
    return ( redirect.id, ContentType.objects.get_for_model( RedirectContent ) )


def process_form( content ):
    print( "Processing form" )
    form = FormContent()
    form.question = content[ "question" ]
    form.save()

    print( "processing choices" )
    for choice in content[ "choices" ]:
        temp = FormContentChoice()
        temp.text = choice[0]
        temp.progress_amount = choice[1]
        temp.form = form
        temp.save()

    print( "done!" )
    return ( form.id, ContentType.objects.get_for_model( FormContent ) )


def process_html( content ):
    print( "Processing html" )
    html = HtmlContent()
    html.html = content[ "html" ]
    html.save()
    return ( html.id, ContentType.objects.get_for_model( HtmlContent ) )


def process_container( container ):
    print( "Processing container" )
    generic_container = GenericContainer()
    generic_container.layout = container[ "layout" ]
    generic_container.save()

    order = 0
    print( "Processing container contents" )
    for generic_content in container[ "content" ]:

        # Process the generic content of the objective
        content_object = process_generic_content( generic_content )

        # Creates the objective and save
        o = GenericContainerContent(
            container = generic_container,
            order = order,
            object_id = content_object[0],
            content_type = content_object[1],
            content_module = generic_content["type"],
        )
        o.save()
        order += 1
    print( "done!" )

    return ( generic_container.id, ContentType.objects.get_for_model( GenericContainer ) )


def process_generic_content( generic_content ):
    if ( generic_content["type"] == "form_content" ):
        return process_form( generic_content )
    if ( generic_content["type"] == "generic_container" ):
        return process_container( generic_content )
    if ( generic_content["type"] == "html_content" ):
        return process_html( generic_content )
    if ( generic_content["type"] == "iframe_content" ):
        return process_iframe( generic_content )
    if ( generic_content["type"] == "redirect_content" ):
        return process_redirect( generic_content )


def process_data_for_situation( data, to_country_id, goal_id ):

    # Gets all the situations for live and work in canada.
    situations = Situation.objects.filter( to_country__id = to_country_id, goal__id = goal_id ).all()

    # MISSIONS
    mission_order = 0
    for mission in data:
        m = Mission()
        m.title = mission["title"]
        m.save()

        print( "Created mission: " + str( m.title ) )

        # OBJECTIVES
        objective_order = 0
        for objective in mission["objectives"]:

            generic_content = objective[ "content" ]

            # Process the generic content of the objective
            content_object = process_generic_content( generic_content )

            # Creates the objective and save
            o = Objective(
                title = objective["title"],
                description = objective["description"],
                object_id = content_object[0],
                content_type = content_object[1],
                content_module = generic_content["type"]
            )
            o.save()
            print( "Created objective: " + str( o.title ) )

            # Creates the Mission-Objective association
            mo = MissionsObjectives()
            mo.mission = m
            mo.objective = o
            mo.order = objective_order
            mo.optional = objective['optional']
            mo.save()

            objective_order += 1


        print( "Adding the mission to all situations" )
        for s in situations:
            sm = SituationsMissions()
            sm.mission = m
            sm.situation = s
            sm.order = mission_order
            sm.save()
        print( "done!" )

        mission_order += 1

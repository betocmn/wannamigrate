##########################
# Imports
##########################
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.forms.models import inlineformset_factory
from django.db import transaction
from django.db.models import ProtectedError
from wannamigrate.admin.forms import (
    QuestionForm, AnswerForm,
    BaseAnswerFormSet, OccupationForm
)
from wannamigrate.core.models import (
    Country
)
from wannamigrate.points.models import (
    Question, Answer, CountryPoints, Occupation
)
from wannamigrate.core.util import build_datatable_json
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.admin.views import admin_check





#######################
# IMMIGRATION RULES VIEWS (QUESTIONS, ANSWERS AND POINTS)
#######################
@restrict_internal_ips
@permission_required( 'core.admin_view_immigration_rule', login_url = 'admin:login' )
@user_passes_test( admin_check )
def question_list( request ):
    """
    Lists all immigration rules (questions)

    :param: request
    :return: String
    """

    context = {}
    return render( request, 'points/admin/question/list.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_view_immigration_rule', login_url = 'admin:login' )
@user_passes_test( admin_check )
def question_list_json( request ):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = Question.objects.all()

    # settings
    info = {
        'fields_to_select': [ 'id', 'description' ],
        'fields_to_search': [ 'id', 'description', 'help_text' ],
        'default_order_by': 'id',
        'url_base_name': 'immigration_rule',
        'namespace': 'admin:points:'
    }

    #build json data and return it to the screen
    json = build_datatable_json( request, objects, info )
    return HttpResponse( json )


@restrict_internal_ips
@permission_required( 'core.admin_add_immigration_rule', login_url = 'admin:login' )
@user_passes_test( admin_check )
def question_add( request ):
    """
    Add new Immigration Rule (question, answers and points)

    :param: request
    :return: String
    """

    # Get countries supported for immigration
    countries = Country.objects.filter( immigration_enabled = True )

    # Get all answer points per country supported
    points_per_country = {}

    # Instantiate Question Form
    question_form = QuestionForm( request.POST or None )

    # Instantiate Answer Formset
    AnswerInlineFormSet = inlineformset_factory( Question, Answer, formset = BaseAnswerFormSet, form = AnswerForm, extra = 10, can_delete = True )
    answer_formset = AnswerInlineFormSet( request.POST or None, countries = countries, points_per_country = points_per_country )

    # Form was submitted so it tries to validate and save data
    if question_form.is_valid():

        # Start a DB Transaction, so if there are any errors in answers/points, question is not saved
        with transaction.atomic():

            # Saves Question
            question = question_form.save()

            # Saves answers
            answer_formset = AnswerInlineFormSet( request.POST or None, instance = question, countries = countries, points_per_country = points_per_country )
            if answer_formset.is_valid():
                answer_formset.save()
                # Redirect with success message
                messages.success( request, 'Immigration Rule was successfully added.')
                return HttpResponseRedirect( reverse( 'admin:points:immigration_rule_details', args = ( question.id, ) ) )
            else:
                transaction.set_rollback( True )



    # Template data
    context = {
        'question_form': question_form,
        'answer_formset': answer_formset,
        'cancel_url': reverse( 'admin:points:immigration_rules' ),
        'countries': countries
    }

    # Print Template
    return render( request, 'points/admin/question/add.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_view_immigration_rule', login_url = 'admin:login' )
@user_passes_test( admin_check )
def question_details( request, question_id ):
    """
    View Immigration Rule page

    :param: request
    :param: question_id
    :return: String
    """

    # Identify database record
    question = get_object_or_404( Question, pk = question_id )

    # Get countries supported for immigration
    countries = Country.objects.filter( immigration_enabled = True )

    # Get all answer points per country supported
    points_per_country = CountryPoints.get_all_points_per_question( question_id )

    # Template data
    context = { 'question': question, 'countries': countries, 'points_per_country': points_per_country }

    # Print Template
    return render( request, 'points/admin/question/details.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_change_immigration_rule', login_url = 'admin:login' )
@user_passes_test( admin_check )
def question_edit( request, question_id ):
    """
    Edit Immigration Rule page

    :param: request
    :param: question_id
    :return: String
    """
    # Identify database record
    question = get_object_or_404( Question, pk = question_id )

    # Get countries supported for immigration
    countries = Country.objects.filter( immigration_enabled = True )

    # Get all answer points per country supported
    points_per_country = CountryPoints.get_all_points_per_question( question_id )

    # Instantiate Question Form
    question_form = QuestionForm( request.POST or None, instance = question )

    # Instantiate Answer Formset
    AnswerInlineFormSet = inlineformset_factory( Question, Answer, formset = BaseAnswerFormSet, form = AnswerForm, extra = 0, can_delete = True, max_num = 2000 )
    answer_formset = AnswerInlineFormSet( request.POST or None, instance = question, countries = countries, points_per_country = points_per_country )

    # Form was submitted so it tries to validate question first
    if question_form.is_valid():

        # Start a DB Transaction, so if there are any errors in answers/points, question is not saved
        with transaction.atomic():

            # Saves Question
            question = question_form.save()

            # Validate answers
            if answer_formset.is_valid():

                # Try to save with a integrity check
                try:
                    answer_formset.save()
                    messages.success( request, 'Immigration Rule was successfully updated.' )
                    return HttpResponseRedirect( reverse( 'admin:points:immigration_rule_details', args = ( question.id, ) ) )

                except ProtectedError:
                    transaction.set_rollback( True )
                    messages.error( request, 'ERROR: Operation could not be completed because you tried to delete records already related to other itens in the system' )
                    return HttpResponseRedirect( reverse( 'admin:points:immigration_rule_edit', args = ( question.id, ) ) )
            else:
                transaction.set_rollback( True )

    # Template data
    context = {
        'question': question,
        'question_form': question_form,
        'answer_formset': answer_formset,
        'cancel_url': reverse( 'admin:points:immigration_rules' ),
        'countries': countries
    }

    # Print Template
    return render( request, 'points/admin/question/edit.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_delete_immigration_rule', login_url = 'admin:login' )
@user_passes_test( admin_check )
def question_delete( request, question_id ):
    """
    Delete Immigration Rule.

    :param: request
    :param: user_id
    :return: String
    """
    # Identify database record
    question = get_object_or_404( Question  , pk = question_id )

    # remove it
    question.delete()

    # Redirect with success message
    messages.success( request, 'Question was successfully deleted.')
    return HttpResponseRedirect( reverse( 'admin:points:immigration_rules' ) )





#######################
# OCCUPATIONS VIEWS
#######################
@restrict_internal_ips
@permission_required( 'auth.view_occupation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def occupation_list( request ):
    """
    Lists all admin users with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render( request, 'points/admin/occupation/list.html', context )


@restrict_internal_ips
@permission_required( 'auth.view_occupation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def occupation_list_json( request ):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = Occupation.objects.select_related( 'occupation_category' ).all()

    # settings
    info = {
        'fields_to_select': [ 'id', 'occupation_category.name', 'name' ],
        'fields_to_search': [ 'id', 'name', 'occupation_category__name' ],
        'default_order_by': 'occupation_category__name',
        'url_base_name': 'occupation',
        'namespace': 'admin:points:'
    }

    #build json data and return it to the screen
    json = build_datatable_json( request, objects, info )

    return HttpResponse( json )

@restrict_internal_ips
@permission_required( 'auth.add_occupation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def occupation_add( request ):
    """
    Add new Occupation

    :param: request
    :param: user_id
    :return: String
    """

    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and save data
        form = OccupationForm( request.POST )
        if form.is_valid():
            occupation = form.save()
            messages.success( request, 'Occupation was successfully added.')
            return HttpResponseRedirect( reverse( 'admin:points:occupation_details', args = ( occupation.id, ) ) )

    else:
        form = OccupationForm()

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:points:occupations' ) }

    # Print Template
    return render( request, 'points/admin/occupation/add.html', context )


@restrict_internal_ips
@permission_required( 'auth.view_occupation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def occupation_details( request, occupation_id ):
    """
    View OCCUPATION page

    :param: request
    :param: occupation_id
    :return: String
    """

    # Identify database record
    occupation = get_object_or_404( Occupation, pk = occupation_id )

    # Template data
    context = { 'occupation': occupation }

    # Print Template
    return render( request, 'points/admin/occupation/details.html', context )


@restrict_internal_ips
@permission_required( 'auth.edit_occupation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def occupation_edit( request, occupation_id ):
    """
    Edit Occupation data

    :param: request
    :param: occupation_id
    :return: String
    """

    # Identify database record
    occupation = get_object_or_404( Occupation, pk = occupation_id )

    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and save data
        form = OccupationForm( request.POST, instance = occupation )
        if form.is_valid():
            form.save()
            messages.success( request, 'Occupation was successfully updated.')
            return HttpResponseRedirect( reverse( 'admin:points:occupation_details', args = ( occupation_id, ) ) )

    else:
        form = OccupationForm( instance = occupation )

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:points:occupation_details', args = ( occupation_id, ) ) }

    # Print Template
    return render( request, 'points/admin/occupation/edit.html', context )


@restrict_internal_ips
@permission_required( 'auth.delete_occupation', login_url = 'admin:login' )
@user_passes_test( admin_check )
def occupation_delete( request, occupation_id ):
    """
    Delete Occupation action.

    :param: request
    :param: occupation_id
    :return: String
    """

    # Identify database record
    occupation = get_object_or_404( Occupation, pk = occupation_id )

    # delete
    occupation.delete()

    # Redirect with success message
    messages.success( request, 'occupation was successfully deleted.' )
    return HttpResponseRedirect( reverse( 'admin:points:occupations' ) )
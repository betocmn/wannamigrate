"""
Admin Views

These are the views that control logic flow for
the templates on admin
"""

##########################
# Imports
##########################
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.forms.models import inlineformset_factory
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import ProtectedError
from wannamigrate.admin.forms import (
    LoginForm, MyAccountForm, AdminUserForm, GroupForm, QuestionForm, AnswerForm,
    BaseAnswerFormSet, OccupationForm, UserForm, 
    AddPostForm, AddAnswerForm, EditPostForm,
    AddTopicForm,
)
from wannamigrate.core.models import (
    Country, UserStats
)
from wannamigrate.points.models import (
    Question, Answer, CountryPoints, Occupation,
    UserResult, OccupationCategory
)
from wannamigrate.core.util import build_datatable_json
from wannamigrate.core.mailer import Mailer
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.qa.models import (
    Post, PostType, PostHistory, Topic, Vote
)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.utils import timezone


#######################
# Function to check user is admin
#######################
def admin_check( user ):
    return user.is_admin





#######################
# LOGIN / LOGOUT / MY ACCOUNT View
#######################
@restrict_internal_ips
def login_index( request ):
    """
    Login Form

    :param: request
    :return: String
    """

    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and authenticate user
        form = LoginForm( request.POST )
        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate( email = email, password = password )

            if user is not None and user.is_active and user.is_admin:
                # Login Successfully
                login( request, user )
                return HttpResponseRedirect( reverse( 'admin:home' ) )
            else:
                # Login Failed :(
                messages.error( request, 'Invalid Login. Please Try Again.' )

    else:
        form = LoginForm()

    # Template data
    context = { 'form': form }

    # Print Template
    return render( request, 'admin/login/index.html', context )


@restrict_internal_ips
@login_required( login_url = 'admin:login' )
@user_passes_test( admin_check )
def login_logout( request ):
    """
    Action for logout

    :param: request
    :return: String
    """
    logout( request )
    return HttpResponseRedirect( reverse( 'admin:login' ) )


@restrict_internal_ips
@login_required( login_url = 'admin:login' )
@user_passes_test( admin_check )
def login_my_account( request ):
    """
    Displays personal data from the logged user

    :param: request
    :return: String
    """

    # Template data
    context = {}

    # Print Template
    return render( request, 'admin/login/my_account.html', context )


@restrict_internal_ips
@login_required( login_url = 'admin:login' )
@user_passes_test( admin_check )
def login_edit_my_account( request ):
    """
    Edit personal data from the logged user

    :param: request
    :return: String
    """
    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and save data
        form = MyAccountForm( request.POST, instance = request.user )
        if form.is_valid():
            request.user = form.save()
            messages.success( request, 'You personal data was successfully updated.')
            return HttpResponseRedirect( reverse( 'admin:my_account' ) )

    else:
        form = MyAccountForm( instance = request.user )

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:my_account' )  }

    # Print Template
    return render( request, 'admin/login/edit_my_account.html', context )


@restrict_internal_ips
@login_required( login_url = 'admin:login' )
@user_passes_test( admin_check, login_url = 'admin:login' )
def home_index( request ):
    """
    Index Dashboard - After an user successfully logs in

    :param: request
    :return: String
    """

    context = { 'user': request.user }
    return render( request, 'admin/home/index.html', context )





#######################
# USERS VIEWS
#######################
@restrict_internal_ips
@permission_required( 'core.admin_view_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def user_list( request ):
    """
    Lists all users with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render( request, 'admin/user/list.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_view_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def user_list_json( request ):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    user = get_user_model()
    objects = user.objects.filter( is_admin = False, is_superuser = False )

    # settings
    info = {
        'fields_to_select': [ 'id', 'name', 'email' ],
        'fields_to_search': [ 'id', 'name', 'email' ],
        'default_order_by': 'id',
        'url_base_name': 'user',
    }

    #build json data and return it to the screen
    json = build_datatable_json( request, objects, info )
    return HttpResponse( json )


@restrict_internal_ips
@permission_required( 'core.admin_add_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def user_add( request ):
    """
    Add new  USER

    :param: request
    :param: user_id
    :return: String
    """

    # Instantiate FORM
    form = UserForm( request.POST or None )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():

        # Sets additional data
        form.is_active = True
        form.is_admin = False

        # Saves User
        user = form.save()
        messages.success( request, 'User was successfully added.' )

        # Sends Welcome Email to User
        # TODO Change this to a celery/signal background task
        Mailer.send_welcome_email( user )

        # Redirect with success message
        return HttpResponseRedirect( reverse( 'admin:user_details', args = ( user.id, ) ) )

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:users' ) }

    # Print Template
    return render( request, 'admin/user/add.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_view_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def user_details( request, user_id ):
    """
    View  USER page

    :param: request
    :param: user_id
    :return: String
    """

    # Identify database record
    user = get_object_or_404( get_user_model(), pk = user_id )

    # Get user results
    try:
        user_result = user.userresult_set.select_related( 'country__name' )
    except UserResult.DoesNotExist:
        user_result = False

    # Get user registrion % (stats)
    try:
        user_stats = UserStats.objects.filter( user = user )
    except UserStats.DoesNotExist:
        user_stats = False

    # Template data
    context = { 'user': user, 'user_result': user_result, 'user_stats': user_stats }

    # Print Template
    return render( request, 'admin/user/details.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_change_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def user_edit( request, user_id ):
    """
    Edit  USER personal data

    :param: request
    :param: user_id
    :return: String
    """
    # Identify database record
    user = get_object_or_404( get_user_model(), pk = user_id )

    # Instantiate FORM
    form = UserForm( request.POST or None, instance = user )

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        form.save()
        messages.success( request, 'User was successfully updated.' )
        return HttpResponseRedirect( reverse( 'admin:user_details', args = ( user_id, ) ) )

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:user_details', args = ( user_id, ) ) }

    # Print Template
    return render( request, 'admin/user/edit.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_delete_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def user_delete( request, user_id ):
    """
    Delete  USER action.
    In the case of users, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: user_id
    :return: String
    """
    # Identify database record
    user = get_object_or_404( get_user_model(), pk = user_id )

    # mark as INACTIVE
    user.is_active = False
    user.save()

    # Redirect with success message
    messages.success( request, 'User was successfully marked as INACTIVE.')
    return HttpResponseRedirect( reverse( 'admin:users' ) )





#######################
# ADMIN USERS VIEWS
#######################
@restrict_internal_ips
@permission_required( 'core.admin_view_admin_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def admin_user_list( request ):
    """
    Lists all admin users with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render( request, 'admin/admin_user/list.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_view_admin_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def admin_user_list_json( request ):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    user = get_user_model()
    objects = user.objects.filter( is_admin = True )

    # settings
    info = {
        'fields_to_select': [ 'id', 'name', 'email', 'is_superuser' ],
        'fields_to_search': [ 'id', 'name', 'email', 'is_superuser' ],
        'default_order_by': 'id',
        'url_base_name': 'admin_user',
    }

    #build json data and return it to the screen
    json = build_datatable_json( request, objects, info )
    return HttpResponse( json )


@restrict_internal_ips
@permission_required( 'core.admin_add_admin_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def admin_user_add( request ):
    """
    Add new Admin USER

    :param: request
    :param: user_id
    :return: String
    """

    # Instantiate FORM
    form = AdminUserForm( request.POST or None )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():

        # Sets additional data
        form.is_active = True
        form.is_admin = True

        # Saves User
        user = form.save()
        messages.success( request, 'User was successfully added.' )

        # Sends Welcome Email to User
        # TODO Change this to a celery/signal background task
        Mailer.send_welcome_email( user )

        # Redirect with success message
        return HttpResponseRedirect( reverse( 'admin:admin_user_details', args = ( user.id, ) ) )

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:admin_users' ) }

    # Print Template
    return render( request, 'admin/admin_user/add.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_view_admin_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def admin_user_details( request, user_id ):
    """
    View Admin USER page

    :param: request
    :param: user_id
    :return: String
    """

    # Identify database record
    user = get_object_or_404( get_user_model(), pk = user_id )

    # Template data
    context = { 'user': user }

    # Print Template
    return render( request, 'admin/admin_user/details.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_change_admin_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def admin_user_edit( request, user_id ):
    """
    Edit Admin USER personal data

    :param: request
    :param: user_id
    :return: String
    """
    # Identify database record
    user = get_object_or_404( get_user_model(), pk = user_id )

    # Instantiate FORM
    form = AdminUserForm( request.POST or None, instance = user )

    # When form is submitted , it tries to validate and save data
    if form.is_valid():
        form.save()
        messages.success( request, 'User was successfully updated.' )
        return HttpResponseRedirect( reverse( 'admin:admin_user_details', args = ( user_id, ) ) )

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:admin_user_details', args = ( user_id, ) ) }

    # Print Template
    return render( request, 'admin/admin_user/edit.html', context )


@restrict_internal_ips
@permission_required( 'core.admin_delete_admin_user', login_url = 'admin:login' )
@user_passes_test( admin_check )
def admin_user_delete( request, user_id ):
    """
    Delete Admin USER action.
    In the case of users, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: user_id
    :return: String
    """
    # Identify database record
    user = get_object_or_404( get_user_model(), pk = user_id )

    # mark as INACTIVE
    user.is_active = False
    user.save()

    # Redirect with success message
    messages.success( request, 'User was successfully marked as INACTIVE.')
    return HttpResponseRedirect( reverse( 'admin:admin_users' ) )





#######################
# GROUPS AND PERMISSIONS VIEWS
#######################
@restrict_internal_ips
@permission_required( 'auth.view_group', login_url = 'admin:login' )
@user_passes_test( admin_check )
def group_list( request ):
    """
    Lists all admin users with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render( request, 'admin/group/list.html', context )


@restrict_internal_ips
@permission_required( 'auth.view_group', login_url = 'admin:login' )
@user_passes_test( admin_check )
def group_list_json( request ):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    #group = Group()
    objects = Group.objects.all()

    # settings
    info = {
        'fields_to_select': [ 'id', 'name' ],
        'fields_to_search': [ 'id', 'name' ],
        'default_order_by': 'name',
        'url_base_name': 'group',
    }

    #build json data and return it to the screen
    json = build_datatable_json( request, objects, info )
    return HttpResponse( json )

@restrict_internal_ips
@permission_required( 'auth.add_group', login_url = 'admin:login' )
@user_passes_test( admin_check )
def group_add( request ):
    """
    Add new Group

    :param: request
    :param: user_id
    :return: String
    """

    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and save data
        form = GroupForm( request.POST )
        if form.is_valid():
            group = form.save()
            messages.success( request, 'Group was successfully added.')
            return HttpResponseRedirect( reverse( 'admin:group_details', args = ( group.id, ) ) )

    else:
        form = GroupForm()

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:groups' ) }

    # Print Template
    return render( request, 'admin/group/add.html', context )


@restrict_internal_ips
@permission_required( 'auth.view_group', login_url = 'admin:login' )
@user_passes_test( admin_check )
def group_details( request, group_id ):
    """
    View GROUP page

    :param: request
    :param: group_id
    :return: String
    """

    # Identify database record
    group = get_object_or_404( Group, pk = group_id )

    # Template data
    context = { 'group': group }

    # Print Template
    return render( request, 'admin/group/details.html', context )


@restrict_internal_ips
@permission_required( 'auth.edit_group', login_url = 'admin:login' )
@user_passes_test( admin_check )
def group_edit( request, group_id ):
    """
    Edit Group data

    :param: request
    :param: group_id
    :return: String
    """

    # Identify database record
    group = get_object_or_404( Group, pk = group_id )

    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and save data
        form = GroupForm( request.POST, instance = group )
        if form.is_valid():
            form.save()
            messages.success( request, 'Group was successfully updated.')
            return HttpResponseRedirect( reverse( 'admin:group_details', args = ( group_id, ) ) )

    else:
        form = GroupForm( instance = group )

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:group_details', args = ( group_id, ) ) }

    # Print Template
    return render( request, 'admin/group/edit.html', context )


@restrict_internal_ips
@permission_required( 'auth.delete_group', login_url = 'admin:login' )
@user_passes_test( admin_check )
def group_delete( request, group_id ):
    """
    Delete Group action.

    :param: request
    :param: group_id
    :return: String
    """
    
    # Identify database record
    group = get_object_or_404( Group, pk = group_id )
    return HttpResponse( 'Deleted' )

    # mark as INACTIVE
    group.is_active = False
    group.save()

    # Redirect with success message
    messages.success( request, 'group was successfully marked as INACTIVE.')
    return HttpResponseRedirect( reverse( 'admin:admin_groups' ) )





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
    return render( request, 'admin/question/list.html', context )


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
                return HttpResponseRedirect( reverse( 'admin:immigration_rule_details', args = ( question.id, ) ) )
            else:
                transaction.set_rollback( True )



    # Template data
    context = {
        'question_form': question_form,
        'answer_formset': answer_formset,
        'cancel_url': reverse( 'admin:immigration_rules' ),
        'countries': countries
    }

    # Print Template
    return render( request, 'admin/question/add.html', context )


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
    return render( request, 'admin/question/details.html', context )


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
                    return HttpResponseRedirect( reverse( 'admin:immigration_rule_details', args = ( question.id, ) ) )

                except ProtectedError:
                    transaction.set_rollback( True )
                    messages.error( request, 'ERROR: Operation could not be completed because you tried to delete records already related to other itens in the system' )
                    return HttpResponseRedirect( reverse( 'admin:immigration_rule_edit', args = ( question.id, ) ) )
            else:
                transaction.set_rollback( True )

    # Template data
    context = {
        'question': question,
        'question_form': question_form,
        'answer_formset': answer_formset,
        'cancel_url': reverse( 'admin:immigration_rules' ),
        'countries': countries
    }

    # Print Template
    return render( request, 'admin/question/edit.html', context )


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
    return HttpResponseRedirect( reverse( 'admin:immigration_rules' ) )





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
    return render( request, 'admin/occupation/list.html', context )


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
            return HttpResponseRedirect( reverse( 'admin:occupation_details', args = ( occupation.id, ) ) )

    else:
        form = OccupationForm()

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:occupations' ) }

    # Print Template
    return render( request, 'admin/occupation/add.html', context )


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
    return render( request, 'admin/occupation/details.html', context )


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
            return HttpResponseRedirect( reverse( 'admin:occupation_details', args = ( occupation_id, ) ) )

    else:
        form = OccupationForm( instance = occupation )

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:occupation_details', args = ( occupation_id, ) ) }

    # Print Template
    return render( request, 'admin/occupation/edit.html', context )


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
    return HttpResponseRedirect( reverse( 'admin:occupations' ) )





#################################
# Q&A VIEWS
#################################
# Posts
@restrict_internal_ips
@permission_required( 'qa.admin_list_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_list_post( request, reported = None ):
    """
    Lists Questions and BlogPosts with pagination.

    :param: request
    :return: String
    """
    if reported:    # Should list all reported content
        reported_post_ids = Vote.objects.filter( vote_type__id = settings.QA_VOTE_TYPE_REPORT_ID ).values( "post_id" )
        posts = Post.objects.filter( id__in = reported_post_ids )
    else:
        posts = Post.objects.filter( post_type_id__in = [ settings.QA_POST_TYPE_BLOGPOST_ID,settings.QA_POST_TYPE_QUESTION_ID ] )

    paginator = Paginator( posts, settings.DEFAULT_LISTING_ITEMS_PER_PAGE ) 

    context = {
        "posts" : posts,
        "reported" : True if reported else False
    }


    # Checks if the page number was passed.
    page = request.GET.get( 'page' )
    try:
        posts = paginator.page( page )
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page( paginator.num_pages )

    return render( request, "admin/qa/post/list.html", context )


@restrict_internal_ips
@permission_required( 'qa.admin_add_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_add_post( request ):
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
        return HttpResponseRedirect( reverse( 'admin:qa_view_post', args = ( post.id, ) ) )

    # Template data
    context = { 
        'form': form, 
        'cancel_url': reverse( 'admin:qa_list_post' ),
        'topics' : Topic.objects.values( "id", "name" ),
    }

    return render( request, 'admin/qa/post/add.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_add_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_add_answer( request, parent_id ):
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
        return HttpResponseRedirect( reverse( 'admin:qa_list_post' ) )
    
    # Instantiate FORM passing parent as argument
    form = AddAnswerForm( request.POST or None, parent = parent )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        # Saves the post
        post = form.save()
        messages.success( request, '{0} successfully created.'.format( post.post_type.name ) )
        # Redirect with success message
        return HttpResponseRedirect( reverse( 'admin:qa_view_post', args = ( parent_id, ) ) )

    # Template data
    context = { 
        'form': form, 
        'cancel_url': reverse( 'admin:qa_list_post' ),
        'topics' : Topic.objects.values( "id", "name" ),
    }

    return render( request, 'admin/qa/post/add_answer.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_view_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_view_post( request, post_id ):
    """
    Lists all posts with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {
        'post' : Post.objects.get( id = post_id ),
        'answers' : Post.objects.filter( parent__id = post_id, post_type__id = settings.QA_POST_TYPE_ANSWER_ID ),
        'post_history' : PostHistory.objects.filter( original_post__id = post_id ),
        'answers' : Post.objects.filter( parent__id = post_id ),
    }
    
    return render( request, 'admin/qa/post/view.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_edit_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_edit_post( request, post_id ):
    """
    Edit a post. It should create an entry on the PostHistory and edit the content of the given post.

    :param: request
    :return: String
    """
    # Gets the information about the post being edited
    post_to_edit = Post.objects.get( pk = post_id )
    
    # Fill up the form with post data
    form = EditPostForm( instance = post_to_edit )
    
    # if data submitted, fill form
    if request.POST:
        form = EditPostForm( request.POST, instance = post_to_edit )

        # If form was submitted, it tries to validate and save data
        if form.is_valid():
            post = form.save()
            messages.success( request, 'Post successfully updated.' )
            # Redirect with success message
            return HttpResponseRedirect( reverse( 'admin:qa_view_post', args = ( post.id, ) ) )
    

    context = {
        'form' : form,
        'post_type' : post_to_edit.post_type.name,
        'cancel_url': reverse( 'admin:qa_list_post' ),
    }
    
    return render( request, 'admin/qa/post/edit.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_delete_post', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_delete_post( request, post_id ):
    """
    Lists all posts with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    post = Post.objects.filter( pk = post_id )
    if post.exists():
        post.delete()
        messages.success( request, "Post(id = {0}) successfully deleted.".format( post_id ) )
    else:
        messages.error( request, "Post(id = {0}) not found.".format( post_id ) )
    
    return HttpResponseRedirect( reverse( "admin:qa_list_post" ) )


# Topics
@restrict_internal_ips
@permission_required( 'qa.admin_list_topic', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_list_topic( request, reported = None ):
    """
    Lists Topics with pagination.

    :param: request
    :return: String
    """
    topics = Topic.objects.all()

    paginator = Paginator( topics, settings.DEFAULT_LISTING_ITEMS_PER_PAGE ) 

    context = {
        "topics" : topics,
    }


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

    return render( request, "admin/qa/topic/list.html", context )


@restrict_internal_ips
@permission_required( 'qa.admin_add_topic', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_add_topic( request ):
    """
    Creates a Topic.

    :param: request
    :return: String
    """

    # Instantiate FORM
    form = AddTopicForm( request.POST or None )

    # If form was submitted, it tries to validate and save data
    if form.is_valid():
        # Saves the post
        topic = form.save()
        messages.success( request, 'Topic successfully created.' )
        # Redirect with success message
        return HttpResponseRedirect( reverse( 'admin:qa_view_topic', args = ( topic.id, ) ) )

    # Template data
    context = { 
        'form': form, 
        'cancel_url': reverse( 'admin:qa_list_topic' ),
    }

    return render( request, 'admin/qa/topic/add.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_view_topic', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_view_topic( request, topic_id ):
    """
    Show Topic details.

    :param: request
    :return: String
    """

    context = {
        'topic' : Topic.objects.get( id = topic_id ),
    }
    
    return render( request, 'admin/qa/topic/view.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_edit_topic', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_edit_topic( request, topic_id ):
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
            return HttpResponseRedirect( reverse( 'admin:qa_view_topic', args = ( topic.id, ) ) )
    

    context = {
        'form' : form,
        'cancel_url': reverse( 'admin:qa_list_post' ),
    }
    
    return render( request, 'admin/qa/topic/edit.html', context )


@restrict_internal_ips
@permission_required( 'qa.admin_delete_topic', login_url = 'admin:login' )
@user_passes_test( admin_check )
def qa_delete_topic( request, topic_id ):
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
    
    return HttpResponseRedirect( reverse( "admin:qa_list_topic" ) )
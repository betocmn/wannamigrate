from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from wannamigrate.admin.forms import LoginForm, MyAccountForm, AdminUserForm, GroupForm
from django.contrib.auth import get_user_model
from wannamigrate.core.util import Helper


#######################
# LOGIN / LOGOUT / MY ACCOUNT
#######################
def login_index( request ):
    """
    Login Form

    :param request:
    :return String:
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


@login_required
def login_logout( request ):
    """
    Action for logout

    :param request:
    :return String:
    """
    logout( request )
    return HttpResponseRedirect( reverse( 'admin:login' ) )


@login_required
def login_my_account( request ):
    """
    Displays personal data from the logged user

    :param request:
    :return String:
    """

    # Template data
    context = {}

    # Print Template
    return render( request, 'admin/login/my_account.html', context )


@login_required
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


@login_required
def home_index( request ):
    """
    Index Dashboard - After an user successfully logs in

    :param: request
    :return: String
    """

    context = { 'user': request.user }
    return render( request, 'admin/home/index.html', context )


#######################
# ADMIN USERS
#######################
@permission_required( 'core.admin_view_admin_user' )
def admin_user_list( request ):
    """
    Lists all admin users with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render( request, 'admin/admin_user/list.html', context )


@permission_required( 'core.admin_view_admin_user' )
def admin_user_list_json( request ):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    user = get_user_model()
    objects = user.objects.all()

    # settings
    info = {
        'fields_to_select': [ 'id', 'name', 'email', 'is_superuser' ],
        'fields_to_search': [ 'id', 'name', 'email', 'is_superuser' ],
        'default_order_by': 'name',
        'url_base_name': 'admin_user',
    }

    #build json data and return it to the screen
    json = Helper.build_datatable_json( request, objects, info )
    return HttpResponse( json )


@permission_required( 'core.admin_add_admin_user' )
def admin_user_add( request ):
    """
    Add new Admin USER

    :param: request
    :param: user_id
    :return: String
    """

    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and save data
        form = AdminUserForm( request.POST )
        if form.is_valid():

            # Sets additional data
            form.is_active = True
            form.is_admin = True

            # Saves User
            user = form.save()
            messages.success( request, 'User was successfully added.')

            # Redirect with success message
            return HttpResponseRedirect( reverse( 'admin:admin_user_details', args = ( user.id, ) ) )

    else:
        form = AdminUserForm()

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:admin_users' ) }

    # Print Template
    return render( request, 'admin/admin_user/add.html', context )


@permission_required( 'core.admin_view_admin_user' )
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


@permission_required( 'core.admin_change_admin_user' )
def admin_user_edit( request, user_id ):
    """
    Edit Admin USER personal data

    :param: request
    :param: user_id
    :return: String
    """
    # Identify database record
    user = get_object_or_404( get_user_model(), pk = user_id )

    # When form is submitted
    if request.method == 'POST':

        # Tries to validate form and save data
        form = AdminUserForm( request.POST, instance = user )
        if form.is_valid():
            form.save()
            messages.success( request, 'User was successfully updated.')
            return HttpResponseRedirect( reverse( 'admin:admin_user_details', args = ( user_id, ) ) )

    else:
        form = AdminUserForm( instance = user )

    # Template data
    context = { 'form': form, 'cancel_url': reverse( 'admin:admin_user_details', args = ( user_id, ) ) }

    # Print Template
    return render( request, 'admin/admin_user/edit.html', context )


@permission_required( 'core.admin_delete_admin_user' )
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
# GROUPS AND PERMISSIONS
#######################
@permission_required( 'auth.view_group' )
def group_list( request ):
    """
    Lists all admin users with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render( request, 'admin/group/list.html', context )


@permission_required( 'auth.view_group' )
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
    json = Helper.build_datatable_json( request, objects, info )
    return HttpResponse( json )

@permission_required( 'auth.add_group' )
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


@permission_required( 'auth.view_group' )
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


@permission_required( 'auth.edit_group' )
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


@permission_required( 'auth.delete_group' )
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


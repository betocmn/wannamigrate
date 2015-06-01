"""
Site Views

These are the views that control logic flow for
the templates on site app
"""

##########################
# Imports
##########################
from django.contrib import messages
from django.db import transaction
from django.template.defaultfilters import slugify
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.utils.translation import ugettext as _
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.conf import settings
from django.forms.models import inlineformset_factory
import math
from wannamigrate.core.util import (
    get_object_or_false
)
from wannamigrate.site.forms import (
    ContactForm, LoginForm, SignupForm, PasswordRecoveryForm,   PasswordResetForm,
    EditAccountForm, EditPasswordForm, SituationForm, EditProviderForm, ProviderCountryForm,
    BaseProviderCountryFormSet, ProviderServiceTypeForm, BaseProviderServiceTypeFormSet,
    UploadAvatarForm, StartConversationForm, ReplyConversationForm
)
from wannamigrate.core.models import (
    Country, UserSituation, Goal, Situation, UserPersonal, Conversation, ConversationMessage, ConversationStatus_User, User, Language, Notification
)
from wannamigrate.marketplace.models import (
    Provider, ProviderServiceType, Service, ProviderCountry, ProviderServiceType
)
from wannamigrate.qa.models import(
    Question, Topic
)
from wannamigrate.core.mailer import Mailer
from django.utils import translation
from django.core import serializers
import time
from PIL import Image
from django.core.files.base import ContentFile
from django.utils import timezone, translation
import pytz
from django.db.models import Prefetch, Count, F
from wannamigrate.qa.util import get_content_by_step, get_questions_by_step, get_blogposts_by_step
from wannamigrate.core.decorators import ajax_login_required





#######################
# SITUATION FORM
#######################
def get_situation_form( request ):
    """
    It checks if it's a visitor or a logged user to
    return the correct situation form.

    The situation form is the one on landing-page and on
    top of every page, so it's used for many apps and views.

    Situation: "I'm From Brazil and wanna study in Canada"

    :param: request
    :return Object - Form object
    """

    # initializes the dict that will store values to be selected on the form by default
    initial_data = {}

    # Checks if there's an active session from this visitor/users
    if 'situation' in request.session and 'from_country' in request.session['situation']:
        initial_data['from_country'] = request.session['situation']['from_country']
        initial_data['to_country'] = request.session['situation']['to_country']
        initial_data['goal'] = request.session['situation']['goal']

    # Returns filled form
    if request.user.is_authenticated():
        return SituationForm( request.POST or None, initial = initial_data, user = request.user )
    else:
        return SituationForm( request.POST or None, initial = initial_data )


def change_situation( request ):
    """
    Action for the change situation form on the top of dashboard
    and internal pages

    :param: request
    :return: Boolean
    """

    # Creates form
    form = get_situation_form( request )

    # If the form has been submitted and is valid...
    if form.is_valid():

        # Saves in DB
        situation = form.save()

        # Saves this information in the session
        request.session['situation'] = {}
        request.session['situation']['from_country'] = situation.from_country
        request.session['situation']['to_country'] = situation.to_country
        request.session['situation']['goal'] = situation.goal
        request.session['situation']['total_users'] = situation.total_users

        # Set portuguese language if from_country uses it as native language
        if situation.from_country.code.lower() in settings.COUNTRIES_BY_LANGUAGE['pt']:
            translation.activate( 'pt' )
            request.session[translation.LANGUAGE_SESSION_KEY] = 'pt'

    # Redirects to dashboard
    return HttpResponseRedirect( reverse( 'site:dashboard' ) )





#######################
# HOME-PAGE VIEWS
#######################
def home( request ):
    """
    Home-Page - Used as a provocative landing page to conquer new users

    :param: request
    :return: String - The html page rendered
    """

    # Temporary code to login automatically (for YCombinator Application)
    if 'demo' in request.GET and request.GET.get( 'demo' ) == '672gah829sP32s89UiQz09321':
        email = 'demo@demo.com'
        password = 'demowanna'
        user = authenticate( email = email, password = password )
        auth_login( request, user )
    else:
        # Checks if the user is already authenticated.
        if request.user.is_authenticated():
            return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Initializes template data dictionary
    template_data = {}

    # passes form to template
    template_data['form'] = get_situation_form( request )

    # Prints Template
    return render( request, 'site/home/home.html', template_data )





#######################
# LOGIN and SIGNUP VIEWS
#######################
def login( request ):
    """
    Process user login.

    :param: request
    :return: String - The html page rendered
    """

    # Checks if the user is already authenticated.
    if request.user.is_authenticated():
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Login - Wanna Migrate' )

    # Instantiates the form
    form = LoginForm( request.POST or None )

    # if Form was submitted and is valid
    if form.is_valid():

        # Authenticates user
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate( email = email, password = password )
        if user is not None and user.is_active:
            # Login Successfully
            auth_login( request, user )
            if 'next' in request.GET:
                return HttpResponseRedirect( request.GET.get( 'next' ) )
            return HttpResponseRedirect( reverse( "site:dashboard" ) )
        else:
            messages.error( request, _( 'Invalid login. Please try again.' ) )

    # passes form to template Forms
    template_data['form'] = form
    template_data['next'] = request.GET.get( 'next' )

    # Prints Template
    return render( request, "site/login/login.html", template_data )


def logout( request ):
    """
    Process Logout

    :param: request
    :return HTTP Redirection:
    """

    # Executes auth Logout
    if request.user.is_authenticated():
        auth_logout( request )

    # Redirect to home-page
    return HttpResponseRedirect( reverse( "site:home" ) )


def signup( request, type = 'user' ):
    """
    Signup action. It creates a new user on the platform

    :param: request
    :return: String - The html page rendered
    """

    # Checks if the user is already authenticated.
    if request.user.is_authenticated():
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Sign Up - Wanna Migrate' )

    # If it's a service provider, register in session for further registration
    template_data['type'] = type

    # Instantiates the form
    form = SignupForm( request.POST or None )

    # if form was submitted and is valid
    if form.is_valid():

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        # Creates user
        user = get_user_model().objects.create_user( email, name = name, password = password )

        if user is not None:

            # Logins user
            user = authenticate( email = email, password = password )
            auth_login( request, user )

            # Saves session to indicate this is a new fresh user
            request.session['new_sign_up'] = True

            # If it's a service provider, saves extra info and redirect to further edition
            is_provider = False
            if 'type' in request.POST and request.POST['type'] == 'service-provider':
                is_provider = True
                provider = Provider()
                provider.user_id = user.id
                provider.display_name = user.name if user.name else user.email
                provider.headline = '--'
                provider.description = '--'
                provider.provider_status_id = 1
                provider.save()


            # Sends Welcome Email to User
            # TODO Change this to a celery/signal background task
            Mailer.send_welcome_email( user, type )

            if is_provider:
                return HttpResponseRedirect( reverse( 'site:edit_account' ) )
            else:
                return HttpResponseRedirect( reverse( 'site:dashboard' ) )

    # passes form to template Forms
    template_data['form'] = form

    # Prints Template
    return render( request, "site/login/signup.html", template_data )


def recover_password( request ):
    """
    Send a link to user redefine it password

    :param: request
    :return: String - The html page rendered
    """

    # Checks if the user is already authenticated.
    if request.user.is_authenticated():
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Recover Password - Wanna Migrate' )

    # Instantiates the form
    form = PasswordRecoveryForm( request.POST or None )

    # if form was submitted and is valid
    if form.is_valid():

        email = form.cleaned_data['email']
        user = get_object_or_false( get_user_model(), email = email )

        if user and user.is_active:

            # Send email with link to reset password
            # TODO: Change this to a celery background event and use a try/exception block
            Mailer.send_reset_password_email( user )

            # Return success message to template
            messages.success( request, _( 'Password reset instructions were successfully sent to your e-mail.' ) )

    # passes form to template Forms
    template_data['form'] = form

    # Prints Template
    return render( request, "site/login/recover_password.html", template_data )


@sensitive_post_parameters()
@never_cache
def reset_password( request, uidb64 = None, token = None ):
    """
    Page to set a new password after clicking on a link from email sent by 'recover password feature'

    :param: request
    :param: uidb64
    :param: token
    :return: String - The html page rendered
    """

    # Try to find user by the uid given
    uid = urlsafe_base64_decode( uidb64 )
    user = get_object_or_404( get_user_model(), pk = uid )

    # Check if token is valid
    token_generator = PasswordResetTokenGenerator()
    if user is None or not token_generator.check_token( user, token ):
        raise Http404

    # Initialize template data dictionary
    template_data = { 'finished': False }

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Reset Password - Wanna Migrate' )

    # Create form
    form = PasswordResetForm( request.POST or None )

    # If form was submitted, it tries to validate and save new password
    if form.is_valid():

        # Saves New password for user
        user.set_password( form.cleaned_data['password'] )
        user.save()

        # mark in the template that it was successfully finished
        messages.success( request, _( 'Password successfully updated.' ) )

    # Pass form to template
    template_data['form'] = form

    # Print Template
    return render( request, 'site/login/reset_password.html', template_data )





#######################
# CONTACT US VIEWS
#######################
def contact( request ):
    """
    Displays the contact page with a form to send us a message by email.

    :param: request
    :return: String - The html page rendered
    """

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Contact Us - Wanna Migrate' )

    # Creates form
    form = ContactForm( request.POST or None )

    # If the form has been submitted...
    if form.is_valid():

        email = form.cleaned_data[ 'email' ]
        name = form.cleaned_data[ 'name' ]
        subject = form.cleaned_data[ 'subject' ]
        message = form.cleaned_data[ 'message' ]

        # Send Email with message
        # TODO: Change this to a celery background event and use a try/exception block
        send_result = Mailer.send_contact_email( email, name, message, subject )
        messages.success( request, _( 'Your message was successfully sent.' ) )

    # pass form to template
    template_data['form'] = form

    # Print Template
    return render( request, 'site/contact/contact.html', template_data )





#######################
# HOW IT WORKS VIEW
#######################
def how_it_works( request ):
    """
    Displays "how It Works" static page

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'How it Works - Wanna Migrate' )


    # Print Template
    return render( request, 'site/about/how_it_works.html', template_data )





#######################
# SERVICE PROVIDERS VIEWS
#######################
def service_providers( request ):
    """
    Displays "I'm a Service Provider" page

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Become a Service Provider - Wanna Migrate' )
    template_data['meta_description'] = _( 'Wanna Migrate brings online clients to you. We are specialized in attracting people planning to migrate to another country, temporarily or permanently.' )

    # Print Template
    return render( request, 'site/about/service_providers.html', template_data )





#######################
# SERVICE PROVIDERS VIEWS
#######################
def tools( request ):
    """
    Home-Page for "Tools".

    :param: request
    :return String - HTML
    """

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Extra Tools - Wanna Migrate' )

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # Print Template
    return render( request, 'site/tools/tools.html', template_data )





#######################
# TERMS, CONDITIONS AND PRIVACY
#######################
def terms( request ):
    """
    Displays "Terms and Conditions" static page

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Terms & Conditions - Wanna Migrate' )

    # Print Template
    return render( request, 'site/terms/terms.html', template_data )


def privacy( request ):
    """
    Displays "Privacy Policy" static page

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initializes template data dictionary
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Privacy Policy - Wanna Migrate' )

    # Print Template
    return render( request, 'site/terms/privacy.html', template_data )





#######################
# MY ACCOUNT VIEWS
#######################
@login_required
def account( request ):
    """
    Displays "My Account" page with user's info.

    :param: request
    :return String - HTML from my account page.
    """

    # Initial template
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'My Account - Wanna Migrate' )

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # Passes user to template
    template_data['user'] = request.user

    # if it's a service provider, passes it to template
    provider = get_object_or_false( Provider, user = request.user )
    if provider:
        template_data['provider'] = provider
        template_data['provider_service_types'] = ProviderServiceType.get_listing( provider.id )

    # Renders the page
    return render( request, 'site/account/view.html', template_data )


@login_required
def contracts( request ):
    """
    Displays "My contracts" page with list of hired services

    :param: request
    :return String - HTML from my account page.
    """

    # Initial template
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'My Contracts - Wanna Migrate' )

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # Passes services to template
    template_data['user_services'] = Service.get_listing( request.user.id, False )
    template_data['provider_services'] = Service.get_listing( request.user.id, True )

    # Renders the page
    return render( request, 'site/account/contracts.html', template_data )


@login_required
def list_conversations( request, conversation_status_id ):
    """
    Displays "inbox" page.

    :param: request
    :return String - HTML from my account page.
    """

    if request.POST:
        # Updates the status of the selected items
        archive_csu_ids = request.POST.getlist( "archive" )
        ConversationStatus_User.objects.filter(
            id__in = archive_csu_ids,
            user__id = request.user.id,
        ).update( status_id = ( settings.CORE_CONVERSATION_STATUS_INBOX_ID if conversation_status_id == settings.CORE_CONVERSATION_STATUS_ARCHIVE_ID else settings.CORE_CONVERSATION_STATUS_ARCHIVE_ID ) )




    # Gets the status of all conversations that belongs to the user
    entries = ConversationStatus_User.objects.filter(
        user__id = request.user.id,
        status__id = conversation_status_id
    ).select_related( "conversation", "conversation__from_user", "conversation__to_user" ).only( "conversation", "has_updates" )

    for entry in entries:
        entry.other_user = entry.conversation.to_user if ( entry.conversation.from_user == request.user ) else entry.conversation.from_user









    # Initial template
    template_data = {}

    if conversation_status_id == settings.CORE_CONVERSATION_STATUS_OUTBOX_ID:
        template_data['sent_menu_selected'] = True
    elif conversation_status_id == settings.CORE_CONVERSATION_STATUS_ARCHIVE_ID:
        template_data['archive_menu_selected'] = True
    else:
        template_data['messages_menu_selected'] = True

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )
    template_data['entries'] = entries

    if conversation_status_id == settings.CORE_CONVERSATION_STATUS_INBOX_ID:
        template_data['display_title'] = _( "Inbox" )
    elif conversation_status_id == settings.CORE_CONVERSATION_STATUS_OUTBOX_ID:
        template_data['display_title'] = _( "Sent" )
    else:
        template_data['display_title'] = _( "Archive" )

    # Renders the page
    return render( request, 'site/conversation/list.html', template_data )


@login_required
def view_conversation( request, id ):
    """
    Displays "inbox" page.

    :param: request
    :return String - HTML from my account page.
    """
    conversation = get_object_or_404( Conversation, pk = id )

    # Checks if the conversation relates to the user
    if request.user.id not in [ conversation.from_user_id, conversation.to_user_id ]:
        return HttpResponseRedirect( reverse( 'site:list_conversations' ) )

    # Get the messages of the conversation
    messages = ConversationMessage.objects.filter( conversation = conversation ).order_by( "-created_date" ).all()

    # Sets the message class to view
    for message in messages:
        if message.owner == request.user:
            message.custom_class = "odd"
        else:
            message.custom_class = "recent" if not message.is_read else "even"

    # Set all received messages as read
    ConversationMessage.objects.filter( conversation = conversation ).exclude( owner = request.user ).update( is_read = True )
    # Set the status of the conversation (has_updates to false)
    ConversationStatus_User.objects.filter( conversation = conversation, user = request.user ).update( has_updates = False )


    form = ReplyConversationForm( request.POST or None, conversation = conversation, owner = request.user )
    if form.is_valid():
        with transaction.atomic():
            # Saves the message
            message = form.save()

            # updates the modified date of the conversation
            conversation.modified_date = message.created_date
            conversation.save()

            # Updates the conversation status for the other user
            csu = ConversationStatus_User.objects.filter( conversation = conversation ).exclude( user = request.user ).update( status_id = settings.CORE_CONVERSATION_STATUS_INBOX_ID, has_updates = True )

            # Data for email notification
            from_user = request.user
            to_user = conversation.to_user if from_user.id == conversation.from_user_id else conversation.from_user

            # Sends Notification to User
            # TODO Change this to a celery/signal background task
            Mailer.send_inbox_notification( from_user, to_user )

            return HttpResponseRedirect( reverse( 'site:view_conversation', kwargs={ "id" : conversation.id } ) )

    template_data = {}
    template_data[ "form" ] = form
    template_data[ "conversation" ] = conversation
    template_data[ "messages" ] = messages
    #template_data[ "messages_menu_selected" ] = True

    return render( request, 'site/conversation/view.html', template_data )


@login_required
def start_conversation( request, to_user_id ):
    """
    Displays "inbox" page.
    Obs: for now, the destination should be specified

    :param: request
    :return String - HTML from my account page.
    """

    # Make sure that the destination is a service provider
    provider = get_object_or_404( Provider, user_id = to_user_id )
    to_user = provider.user

    # Avoid auto-messaging.
    if to_user == request.user:
        return HttpResponseRedirect( reverse( 'site:list_conversations' ) )

    form = StartConversationForm( request.POST or None, owner = request.user, to_user = to_user )

    if form.is_valid():
        with transaction.atomic():
            conversation = form.save()

            # Sets the status of the message for from_user
            csu_from = ConversationStatus_User()
            csu_from.conversation = conversation
            csu_from.user = conversation.from_user
            csu_from.status_id = settings.CORE_CONVERSATION_STATUS_OUTBOX_ID
            csu_from.has_updates = False
            csu_from.save()

            # Sets the status of the message for to_user
            csu_to = ConversationStatus_User()
            csu_to.conversation = conversation
            csu_to.user = conversation.to_user
            csu_to.status_id = settings.CORE_CONVERSATION_STATUS_INBOX_ID
            csu_to.has_updates = True
            csu_to.save()

            # Creates the message
            msg = ConversationMessage()
            msg.conversation = conversation
            msg.owner = conversation.from_user
            msg.is_read = False
            msg.content = form.cleaned_data[ "content" ]
            msg.save()

            # Sends Notification to User
            # TODO Change this to a celery/signal background task
            Mailer.send_inbox_notification( conversation.from_user, conversation.to_user )

            return HttpResponseRedirect( reverse( 'site:view_conversation', kwargs={ "id" : conversation.id } ) )


    # Initial template
    template_data = {}
    template_data[ 'messages_menu_selected' ] = True
    template_data[ 'form' ] = form
    template_data[ 'to_user' ] = to_user
    template_data[ 'situation_form' ] = get_situation_form( request )

    # Renders the page
    return render( request, 'site/conversation/start.html', template_data )


@login_required
def edit_account( request ):
    """
    Edit "My Account" page.

    :param: request
    :return String - HTML from Edit My Account page.
    """

    # Initial template
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Edit My Account - Wanna Migrate' )

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # Passes user and provider to template
    template_data['user'] = request.user

    # Instantiates the User Form
    user_form = EditAccountForm( request.POST or None, instance = request.user )

    # Check if the Provider exists
    provider = get_object_or_false( Provider, user = request.user )
    template_data['provider'] = provider
    if provider:

        # instantiates provider FORM
        provider_form = EditProviderForm( request.POST or None, instance = provider )

        # Instantiates Countries Formset
        try:
            count = provider.countries.count()
            if count > 0:
                extra = 0
            else:
                extra = 1
        except ProviderCountry.DoesNotExist:
            extra = 1
        ProviderCountryInlineFormset = inlineformset_factory( Provider, ProviderCountry, form = ProviderCountryForm, formset = BaseProviderCountryFormSet, extra = extra, can_delete = True )
        provider_country_formset = ProviderCountryInlineFormset( request.POST or None, instance = provider )

        # Instantiates Services Formset
        try:
            count = provider.service_types.count()
            if count > 0:
                extra = 0
            else:
                extra = 1
        except ProviderServiceType.DoesNotExist:
            extra = 1
        ProviderServiceTypeInlineFormset = inlineformset_factory( Provider, ProviderServiceType, form = ProviderServiceTypeForm, formset = BaseProviderServiceTypeFormSet, extra = extra, can_delete = True )
        provider_service_type_formset = ProviderServiceTypeInlineFormset( request.POST or None, instance = provider )

    # if form was submitted and is valid
    success = True
    if user_form.is_valid() and ( ( provider and provider_form.is_valid() ) or not provider ):

        # Start a DB Transaction, so if there are any errors in answers/points, question is not saved
        with transaction.atomic():

            # Update user's information
            user = user_form.save()

            # if it's a provider
            if provider:

                # Update provider's info
                provider = provider_form.save()

                # Update countries supported
                if provider_country_formset.is_valid():
                    instances = provider_country_formset.save()
                else:
                    transaction.set_rollback( True )
                    success = False

                # Update services supported
                if provider_service_type_formset.is_valid():
                    instances = provider_service_type_formset.save()
                else:
                    transaction.set_rollback( True )
                    success = False

            if success:

                # Updates the active language
                if user.preferred_language:
                    translation.activate( user.preferred_language )
                    request.session[translation.LANGUAGE_SESSION_KEY] = user.preferred_language

                # Updates the active timezone
                if user.preferred_timezone:
                    timezone.activate( pytz.timezone( user.preferred_timezone ) )
                    request.session['django_timezone'] = user.preferred_timezone

                # Redirects to view page with success message
                messages.success( request, _( 'Data successfully updated.' ) )
                return HttpResponseRedirect( reverse( 'site:account' ) )

    # passes forms to template
    template_data['user_form'] = user_form
    if provider:
        template_data['provider_form'] = provider_form
        template_data['provider_country_formset'] = provider_country_formset
        template_data['provider_service_type_formset'] = provider_service_type_formset

    # Prints Template
    return render( request, 'site/account/edit.html', template_data )


@login_required
def upload_avatar( request ):

    # gets user personal object
    user_personal = get_object_or_false( UserPersonal, user = request.user )
    if not user_personal:
        user_personal = UserPersonal()
        user_personal.user = request.user

    # if form was sent
    if request.method == 'POST':

        # instantiates form to validate the file
        form = UploadAvatarForm( request.POST, request.FILES )
        if form.is_valid():

            # sets image name
            user_name = request.user.name if request.user.name is not None else request.user.email
            image_basename = slugify( user_name + "-avatar" )
            image_name = '%s%s.jpg' % ( int( time.time() ), image_basename )

            # save image
            user_personal.avatar.save( image_name, request.FILES['file'] )


    return HttpResponse( 'ok' )


@login_required
def edit_password( request ):
    """
    Edit account's password page.

    :param: request
    :return String - HTML from Edit account's password page.
    """
    # Initial template
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Change Password - Wanna Migrate' )

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # Passes user and provider to template
    template_data['user'] = request.user

    # Instantiates the User Form
    form = EditPasswordForm( request.POST or None, instance = request.user )

    # If the form has been submitted...
    if form.is_valid():

        # saves in the db
        form.save()

        # redirect with success message
        messages.success( request, _( 'Your password was successfully updated.' ) )
        return HttpResponseRedirect( reverse( 'site:account' ) )


    # pass form to template
    template_data['form'] = form

    # Print Template
    return render( request, 'site/account/edit_password.html', template_data )





#######################
# DASHBOARD VIEWS
#######################
def dashboard( request ):
    """
    Process the dashboard page.

    The dashboard is the main screen of the system,
    where the users can view its informations, progress, etc.

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Initial template
    template_data = {}

    # Checks if its a new signup
    if 'new_sign_up' in request.session and request.session['new_sign_up']:
        is_new_signup = True
        request.session['new_sign_up'] = False
    else:
        is_new_signup = False

    # Activates Page Conversion tags for Google Ad Words
    template_data['track_conversion_view_dashboard'] = True
    if is_new_signup:
        template_data['track_conversion_sign_up'] = True

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # Gets the user language
    language = Language.objects.filter( code = request.LANGUAGE_CODE ).get()


    # If situation is defined, we load questions and professionals related to it
    if 'situation' in request.session and 'from_country' in request.session['situation']:

        from_country = request.session['situation']['from_country']
        to_country = request.session['situation']['to_country']
        goal = request.session['situation']['goal']

        # Saves user situation from session if it's a new signup
        if is_new_signup:
            situation, created = Situation.objects.get_or_create(
                from_country = from_country,
                to_country = to_country,
                goal = goal,
                defaults = {
                    'total_users': 1,
                    'total_visitors': 0,
                    'from_country': from_country,
                    'to_country': to_country,
                    'goal': goal
                }
            )
            if not created:
                situation.total_users = F( 'total_users' ) + 1
                situation.save()
            user_situation = UserSituation()
            user_situation.user = request.user
            user_situation.situation = situation
            user_situation.save()

        # Gets 5 most related service providers
        template_data['providers'] = Provider.get_listing( to_country.id, 0, 5 )

        filter_params = {}
        # Fills the topics related to user's situation
        filter_params[ "related_countries_ids" ] = [ to_country.id ]
        filter_params[ "related_goals_ids" ] = [ goal.id ]
        filter_params[ "language_ids" ] = [ language.id ]

        # Get questions per step
        questions = get_questions_by_step( request, filter_params, 0, 5 )

        # Gets 5 most related questions (page 0 by default)
        template_data['questions'] = questions


    # Print Template
    return render( request, 'site/dashboard/dashboard.html', template_data )





#######################
# INTERNATIONALIZATION VIEWS
#######################
def set_lang( request, language_code ):
    """
    Changes the current language to the desired language defined by language_code parameter.
    If you want to redirect the user to other page that isn't '/' provide a parameter named "next" in the GET request.

    :param: request Default request param.
    :param language_code: The code of the language to localize.
    :return Sets the desired language and redirects the user to '/' or to a next page defined via GET.
    """

    # Checks if next parameters is set.
    next = '/'
    if request.GET[ "next" ]:
        next = request.GET[ "next" ]

    # Activates language
    translation.activate( language_code )
    request.session[translation.LANGUAGE_SESSION_KEY] = language_code

    return redirect( settings.BASE_URL_SECURE + next )







#########################
# AJAX / DYNAMIC VIEWS
#########################
@ajax_login_required
def ajax_consume_notifications( request ):
    """
    Set all unread notifications for the authenticated user as read.
    """
    Notification.mark_as_read_for( request.user )
    return HttpResponse( "" )


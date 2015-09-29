"""
Site Views

These are the views that control logic flow for
the templates on site app
"""

##########################
# Imports
##########################
from django.template.loader import render_to_string
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
    User, UserStats, UserSituation, UserPersonal, Conversation, ConversationMessage,
    ConversationStatus_User, Language, Notification, Country, Goal
)
from wannamigrate.marketplace.models import (
    Provider, ProviderCountry, ProviderServiceType,
    Order, Product, Subscription, SubscriptionStatus
)
from wannamigrate.core.mailer import Mailer
import time
from django.utils import timezone, translation
import pytz
from django.db.models import Prefetch
from wannamigrate.qa.util import get_questions_by_step
from wannamigrate.core.decorators import ajax_login_required
from wannamigrate.qa.models import Answer, Question, BlogPost
from wannamigrate.core.tasks import add_notification, send_welcome_email





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
        initial_data['from_country'] = Country.objects.get( pk = request.session['situation']['from_country']['id'] )
        initial_data['to_country'] = Country.objects.get( pk = request.session['situation']['to_country']['id'] )
        initial_data['goal'] = Goal.objects.get( pk = request.session['situation']['goal']['id'] )

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
        from_country = situation.from_country
        to_country = situation.to_country
        goal = situation.goal
        request.session['situation'] = { 'id': situation.id, 'from_country': {}, 'goal': {}, 'to_country': {} }
        request.session['situation']['from_country']['id'] = from_country.id
        request.session['situation']['from_country']['name'] = from_country.name
        request.session['situation']['from_country']['code'] = from_country.code
        request.session['situation']['goal']['id'] = goal.id
        request.session['situation']['goal']['name'] = goal.name
        request.session['situation']['to_country']['id'] = to_country.id
        request.session['situation']['to_country']['name'] = to_country.name
        request.session['situation']['to_country']['code'] = to_country.code
        request.session['situation']['total_users'] = situation.total_users

        # Sets language accordingly to FROM Country
        if from_country.code.lower() in settings.COUNTRIES_BY_LANGUAGE['pt']:
            language_code = 'pt'
        else:
            language_code = 'en'

        # Updates current and preferred language
        if language_code != translation.get_language():
            translation.activate( language_code )
            request.session[translation.LANGUAGE_SESSION_KEY] = language_code
            if request.user.is_authenticated():
                request.user.preferred_language = language_code
                request.user.save()
            language = Language.objects.get( code = language_code )
            request.session['language'] = {
                'id': language.id,
                'name': language.name,
                'code': language.code
            }

        # Session used in middleware
        request.session['situation_updated'] = True

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

    # Saves session to indicate this is a new registration
    request.session['login_or_signup_started'] = True

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
        if 'next' in request.GET:
            return HttpResponseRedirect( request.GET.get( 'next' ) )
        return HttpResponseRedirect( reverse( "site:dashboard" ) )

    # Saves session to indicate this is a new registration
    request.session['login_or_signup_started'] = True

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
        user = get_user_model().objects.create_user(
            email,
            name = name,
            password = password,
            language = translation.get_language(),
            timezone = 'America/Sao_Paulo'
        )

        if user is not None:

            # Logins user
            user = authenticate( email = email, password = password )
            auth_login( request, user )

            # If it's a service provider, saves extra info and redirects to further edition
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


            # CELERY TASK to send Welcome Email to User
            send_welcome_email.delay( user, type )

            if 'next' in request.GET:
                return HttpResponseRedirect( request.GET.get( 'next' ) )
            elif is_provider:
                return HttpResponseRedirect( reverse( 'site:edit_account' ) )
            else:
                return HttpResponseRedirect( reverse( 'site:dashboard' ) )

    # passes form to template Forms
    template_data['form'] = form
    template_data['next'] = request.GET.get( 'next' )

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
# GUIDE - STEP BY STEP - VIEWS
#######################
def guide( request, country_name ):
    """
    Step-by-step guide to migrate to a destination country

    :param: request
    :param: country_name
    :return String - HTML from The dashboard page.
    """
    return redirect( reverse( 'site:premium' ), permanent = True )





#######################
# PREMIUM SUBSCRIPTION - VIEWS
#######################
def premium( request ):
    """
    Sales page for the subscription service

    :param: request
    :return String - HTML from The dashboard page.
    """

    # If user is already subscribe, redirects him to premium features page
    if 'subscription' in request.session and request.session['subscription']:
        return HttpResponseRedirect( reverse( "director:dashboard" ) )

    # Initializes template data dictionary
    template_data = {}
    error = False

    # If form was submitted (to proceed to payment page)
    if request.method == 'POST':

        # Identifies database records
        product = get_object_or_false( Product, pk = request.POST['product_id'], is_active = True )
        if not product:
            return HttpResponseRedirect( reverse( "site:dashboard" ) )

        # saves details to session
        payment_info = {
            'product': { 'id': product.id, 'name': product.name, 'price': product.price, 'product_category_id': product.product_category_id }
        }

        # saves subscription
        if request.user.is_authenticated() and product.product_category_id in settings.SUBSCRIPTION_PRODUCT_CATEGORIES:

            subscription = get_object_or_false(
                Subscription,
                user_id = request.user.id,
                product_id = product.id,
                subscription_status_id = settings.ID_SUBSCRIPTION_STATUS_ACTIVE
            )
            if subscription:
                error = True
                messages.error( request, _( "There's already an active subscription for this country and product." ) )
            else:
                subscription = Subscription()
                subscription.product_id = product.id
                subscription.subscription_status_id = SubscriptionStatus.get_status_from_order_status()
                subscription.user = request.user
                subscription.save()
                payment_info['subscription'] = { 'id': subscription.id, 'subscription_status_id': subscription.subscription_status_id }

        if not error:
            # saves details to session and redirect
            request.session['payment'] = payment_info
            return HttpResponseRedirect( reverse( "marketplace:payment" ) )

    else:
        # Cleans payment session
        request.session['payment'] = {}
        del request.session['payment']

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'Premium Subscription - Wanna Migrate' )
    template_data['meta_description'] = _( 'Powerful immigration tool to help you to immigrate to your dream country.' )

    # Activates Page Conversion tags for Google Ad Words
    template_data['track_conversion_view_subscription_plan'] = True

    # Print Template
    return render( request, 'site/premium/premium.html', template_data )





#######################
# TOOLS VIEWS
#######################
def tools( request ):
    """
    Home-Page for "Tools".

    :param: request
    :return String - HTML
    """
    return redirect( reverse( 'site:premium' ), permanent = True )





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
# ROBOTS.txt
#######################
def robots( request ):
    """
    Displays the robots.txt file

    :param: request
    :return Text/Plain
    """

    # Initializes template data dictionary
    template_data = {}

    # Print Template
    return render( request, 'site/seo/robots.txt', template_data, content_type = 'text/plain' )





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
    template_data['provider_order_services'] = Order.get_listing( 'service', request.user.id, True )
    template_data['user_order_services'] = Order.get_listing( 'service', request.user.id )
    template_data['user_order_products'] = Order.get_listing( 'product', request.user.id )

    # Renders the page
    return render( request, 'site/account/contracts.html', template_data )



@login_required
def notifications( request ):
    """
    Displays "My contracts" page with list of hired services

    :param: request
    :return String - HTML from my account page.
    """

    # Initial template
    template_data = {}

    # Overwrites meta title and description (for SEO)
    template_data['meta_title'] = _( 'My Notifications - Wanna Migrate' )

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # Gets Situation Form
    template_data['notifications'] = Notification.get_all_notifications_for( request.user )
    Notification.mark_as_read_for( request.user )

    # Renders the page
    return render( request, 'site/account/notifications.html', template_data )


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
    ).select_related( "conversation", "conversation__from_user", "conversation__to_user" ).only( "conversation", "has_updates" ).order_by( "-conversation__modified_date" )

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

            # CELERY TASK to add a notification to the destination user
            translation_hack = _( "New message from" )
            add_notification.delay(
                "{{{New message from}}} " + from_user.name,
                reverse( 'site:view_conversation', kwargs={ "id" : conversation.id } ),
                [ to_user ],
                True
            )

            return HttpResponseRedirect( reverse( 'site:view_conversation', kwargs={ "id" : conversation.id } ) )

    template_data = {}
    template_data[ "form" ] = form
    template_data[ "conversation" ] = conversation
    template_data[ "messages" ] = messages
    #template_data[ "messages_menu_selected" ] = True

    return render( request, 'site/conversation/view.html', template_data )


@login_required
def start_conversation( request, to_user_slug ):
    """
    Displays "inbox" page.
    Obs: for now, the destination should be specified

    :param: request
    :return String - HTML from my account page.
    """

    # Make sure that the destination is a service provider
    to_user = get_object_or_404( User, slug = to_user_slug )

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

            # CELERY TASK to add a notification to the destination user
            add_notification.delay(
                "{{{New message from}}} " + conversation.from_user.name,
                reverse( 'site:view_conversation', kwargs={ "id" : conversation.id } ),
                [ conversation.to_user ],
                True
            )

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
                    language = Language.objects.get( code = user.preferred_language )
                    request.session['language'] = {
                        'id': language.id,
                        'name': language.name,
                        'code': language.code
                    }

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
@login_required( login_url = '/signup' )
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
    if 'conversion_new_signup' in request.session and request.session['conversion_new_signup']:
        is_new_signup = True
        del request.session['conversion_new_signup']
    else:
        is_new_signup = False

    # Activates Page Conversion tags for Google Ad Words
    if is_new_signup:
        template_data['track_conversion_sign_up'] = True

    # Gets Situation Form
    template_data['situation_form'] = get_situation_form( request )

    # Gets the user language
    language = Language.objects.filter( code = request.LANGUAGE_CODE ).get()


    # If situation is defined, we load questions and professionals related to it
    if 'situation' in request.session and 'from_country' in request.session['situation']:

        # Fills the topics related to user's situation
        filter_params = {}
        filter_params[ "related_countries_ids" ] = [ request.session['situation']['to_country']['id'] ]
        filter_params[ "related_goals_ids" ] = [ request.session['situation']['goal']['id'] ]
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

    # If user is logged-in, we update his preferred language
    if request.user.is_authenticated():
        request.user.preferred_language = language_code
        request.user.save()

    # Gets language ID from DB and saves in session
    language = Language.objects.get( code = language_code )
    request.session['language'] = {
        'id': language.id,
        'name': language.name,
        'code': language.code
    }

    return redirect( settings.BASE_URL_SECURE + next )







#######################
# User Profile view
#######################
@login_required
def user_profile( request, slug ):
    """
    Displays "User's profile" page

    :param: request
    :return String - HTML from The dashboard page.
    """

    # Gets the requested user
    requested_user = get_object_or_404( User.objects.prefetch_related( "userstats" ), slug = slug )

    # If the requested user is a service provider, redirects to service provider profile page
    provider = Provider.objects.filter( user = requested_user ).first()
    if provider:
        return HttpResponseRedirect( reverse( 'marketplace:profile', kwargs={ "user_id" : provider.user_id, "name" : slugify( provider.display_name ) } ) )

    # Gets the situation of the requested user and formats it to display on the template.
    situation = UserSituation.objects.filter( user = requested_user ).select_related( "situation" ).get().situation
    situation_description = "{0} {1} {2} {3} {4} {5} {6}".format(
        _( "I'm from" ),
        _( situation.from_country.name ),
        _( "and" ).lower(),
        _( "I wanna" ).lower(),
        _( situation.goal.name ).lower(),
        _( "in" ).lower(),
        _( situation.to_country.name )
    )

    # Initializes template data dictionary
    template_data = {
        "requested_user" : requested_user,
        "meta_title" : "{0} - ".format( requested_user.name ) +  _( "Profile - Wanna Migrate" ),
        "questions_count" : Question.objects.filter( owner = requested_user, is_anonymous = False ).count(),
        "answers_count" : Answer.objects.filter( owner = requested_user, is_anonymous = False ).count(),
        "posts_count" : BlogPost.objects.filter( owner = requested_user, is_anonymous = False ).count(),
        "followers_count" : requested_user.userstats.total_users_followers,
        "following_count" : requested_user.userstats.total_users_following,
        "is_followed" : request.user.following.filter( id = requested_user.id ).exists(),
        "hide_buttons" : ( request.user == requested_user ),
        "situation_description" : situation_description,
    }


    # Print Template
    return render( request, 'site/profile/view.html', template_data )





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




@ajax_login_required
def ajax_toggle_follow_user( request, slug ):

    # Gets the stats of the logged user
    user_stats, created = UserStats.objects.get_or_create( user_id = request.user.id )

    # Gets the stats of the requested user
    requested_user = get_object_or_404( User.objects, slug = slug )
    requested_user_stats, created = UserStats.objects.get_or_create( user_id = requested_user.id )


    if request.user.id == requested_user.id:
        return JsonResponse( {
        "action" : _( "Follow" ),
        "total" : requested_user_stats.total_users_followers
    } )

    is_followed = False   # flag indicating if the user is following the user


    with transaction.atomic():
        if not request.user.following.filter( id = requested_user.id ).exists():
            # If the logged user isn't following the requested user, follows him.
            request.user.following.add( requested_user )
            user_stats.total_users_following += 1
            requested_user_stats.total_users_followers += 1

            user_stats.save()
            requested_user_stats.save()

            # Set a flag indicating that the user is following the FollowableInstance.
            is_followed = True
        else:
            # If the logged user isn't following the requested user, follows him.
            request.user.following.remove( requested_user )
            user_stats.total_users_following -= 1
            requested_user_stats.total_users_followers -= 1

            user_stats.save()
            requested_user_stats.save()

            # Set a flag indicating that the user is following the FollowableInstance.
            is_followed = False

    # Creates a response to the call
    response = {
        "action" : _( "Unfollow" ) if is_followed else _( "Follow" ),
        "total" : requested_user_stats.total_users_followers
    }

    # Generates a notification to the followed user
    if is_followed:
        translation_hack = _( "now is following you" )
        add_notification.delay(
            request.user.name + " {{{now is following you}}}.",
            reverse( "site:user_profile", kwargs={ "slug" : request.user.slug } ),
            requested_user,
            True
        )

    return JsonResponse( response )


@ajax_login_required
def ajax_get_user_questions( request, slug ):

    user = get_object_or_404( User.objects, slug = slug )

    questions = Question.objects.filter( owner = user, is_anonymous = False ).all()

    processed_questions = [ { "title" : x.title, "body" : "", "url" : reverse( "qa:view_question", kwargs={ "slug" : x.slug } ) } for x in questions ]

    html = render_to_string( "site/profile/user-content-post.html", { "contents": processed_questions } )
    return HttpResponse( html )


@ajax_login_required
def ajax_get_user_answers( request, slug ):

    user = get_object_or_404( User.objects, slug = slug )

    answers = Answer.objects.filter( owner = user, is_anonymous = False ).prefetch_related( "question" ).all()

    processed_answers = [ { "title" : x.question.title, "body" : x.body, "url" : reverse( "qa:view_question", kwargs={ "slug" : x.question.slug } )  } for x in answers ]

    html = render_to_string( "site/profile/user-content-post.html", { "contents": processed_answers } )
    return HttpResponse( html )


@ajax_login_required
def ajax_get_user_posts( request, slug ):

    user = get_object_or_404( User.objects, slug = slug )

    posts = BlogPost.objects.filter( owner = user, is_anonymous = False ).all()

    processed_posts = [ { "title" : x.title, "body" : x.body, "url" : reverse( "qa:view_blogpost", kwargs={ "user_slug" : settings.QA_ANONYMOUS_USER_SLUG if x.is_anonymous else user.slug , "slug" : x.slug } ) } for x in posts ]

    html = render_to_string( "site/profile/user-content-post.html", { "contents": processed_posts } )
    return HttpResponse( html )


@ajax_login_required
def ajax_get_user_followers( request, slug ):

    user = get_object_or_404( User.objects.prefetch_related(
        Prefetch(
                "followers",
                queryset=User.objects.select_related( "userpersonal" )
            ) ), slug = slug )

    followers = user.followers.all()
    processed_followers = []
    for x in followers:
        try:
            processed_followers.append( { "name" : x.name, "avatar" : x.userpersonal.avatar.thumbnail.url if x.userpersonal.avatar else None, "url" : reverse( "site:user_profile", kwargs={ "slug" : x.slug } ) } )
        except Exception:
            processed_followers.append( { "name" : x.name, "avatar" : None, "url" : reverse( "site:user_profile", kwargs={ "slug" : x.slug } ) } )

    html = render_to_string( "site/profile/user-content-people.html", { "contents": processed_followers } )
    return HttpResponse( html )


@ajax_login_required
def ajax_get_user_following( request, slug ):

    user = get_object_or_404( User.objects.prefetch_related(
        Prefetch(
                "following",
                queryset=User.objects.select_related( "userpersonal" )
            ) ), slug = slug )

    following = user.following.all()
    processed_following = []
    for x in following:
        try:
            processed_following.append( { "name" : x.name, "avatar" : x.userpersonal.avatar.thumbnail.url if x.userpersonal.avatar else None, "url" : reverse( "site:user_profile", kwargs={ "slug" : x.slug } ) } )
        except Exception:
            processed_following.append( { "name" : x.name, "avatar" : None, "url" : reverse( "site:user_profile", kwargs={ "slug" : x.slug } ) } )

    html = render_to_string( "site/profile/user-content-people.html", { "contents": processed_following } )
    return HttpResponse( html )
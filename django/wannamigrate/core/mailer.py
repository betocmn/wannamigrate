"""
Class responsible to send-out all system emails

Usage:

Mailer.send_welcome_email( user )

"""

##########################
# Imports
##########################
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.urlresolvers import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.translation import ugettext as _





##########################
# Class definitions
##########################
class Mailer( object ):

    @staticmethod
    def send( subject, body, to, from_email = None, cc = None, bcc = None, attachments = None ):
        """
        Send the email using Django's EmailMessage class

        :param: subject
        :param: body
        :param: to
        :param: from_email
        :param: cc
        :param: bcc
        :param: attachments
        :return: String
        """

        #if not settings.IS_PROD:
            #return True

        email = EmailMessage()
        email.content_subtype = "html"
        email.subject = subject
        email.body = body
        email.to = [to] if isinstance( to, str ) else to
        if from_email:
            email.from_email = from_email
        if cc:
            email.cc = [cc] if isinstance( cc, str ) else cc
        if bcc:
            email.bcc = [bcc] if isinstance( bcc, str ) else bcc
        if attachments:
            for attachment in attachments:
                email.attach( attachment )

        return email.send()


    @staticmethod
    def build_body_from_template( template_path, template_data = None ):
        """
        Returns generated HTML from django template

        :param: template_path
        :param: template_data
        :return: String
        """

        template = get_template( template_path )
        template_data['base_url'] = settings.BASE_URL
        template_data['base_url_secure'] = settings.BASE_URL_SECURE
        context = Context( template_data )
        content = template.render( context )
        return content


    @staticmethod
    def send_welcome_email( user, type = 'user' ):
        """
        Sends welcome email to users

        :param: user
        """

        if type == 'service-provider':
            bcc = settings.EMAIL_NOTIFICATION_PROVIDER_SIGNUP
            template_file = 'welcome_provider.html'
        else:
            bcc = None
            template_file = 'welcome_user.html'

        template_data = { 'user': user }
        body = Mailer.build_body_from_template( 'emails/' + template_file, template_data )
        return Mailer.send( _( 'Welcome to Wanna Migrate' ), body, user.email, None, None, bcc )


    @staticmethod
    def send_reset_password_email( user ):
        """
        Sends email with link to reset password

        :param: user
        """

        # creates token
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token( user )

        # builds link
        base_secure_url = settings.BASE_URL_SECURE
        uid = urlsafe_base64_encode( force_bytes( user.pk ) )
        link = base_secure_url + reverse( 'site:reset_password', args = ( uid, token, ) )

        template_data = { 'user': user, 'link': link }
        body = Mailer.build_body_from_template( 'emails/reset_password.html', template_data )
        return Mailer.send( _( 'Reset your Password' ), body, user.email )


    @staticmethod
    def send_contact_email( email, name, message, subject ):
        """
        Sends contact e-mail from site

        :param: email
        :param: name
        :param: message
        """
        template_data = { 'email': email, 'name': name, 'message': message, 'subject': subject }
        body = Mailer.build_body_from_template( 'emails/contact.html', template_data )
        return Mailer.send( _( 'Contact: ' + subject ), body, settings.EMAIL_NOTIFICATION_CONTACT_FORM )


    @staticmethod
    def send_professional_help_email( email, name, message ):
        """
        Sends  e-mail from site notifying an user needs professional help

        :param: email
        :param: name
        :param: message
        """
        template_data = { 'email': email, 'name': name, 'message': message }
        body = Mailer.build_body_from_template( 'emails/contact.html', template_data )
        return Mailer.send( _( 'Professional Help Requested' ), body, settings.EMAIL_NOTIFICATION_CONTACT_FORM )


    @staticmethod
    def send_order_confirmation_user( user, order, provider = None ):
        """
        Sends order confirmation to user

        :param: user
        :param: order
        :param: provider
        """
        
        # Defines order message accordingly to status
        message = ''
        if order.order_status_id == settings.ID_ORDER_STATUS_PENDING:
            message = _( "Your order was received and will be processed soon." )
        elif order.order_status_id == settings.ID_ORDER_STATUS_APPROVED:
            message = _( "Your order was approved." )
        elif order.order_status_id == settings.ID_ORDER_STATUS_DENIED:
            message = _( "Your order was denied." )
        elif order.order_status_id == settings.ID_ORDER_STATUS_CANCELLED:
            message = _( "Your order was cancelled." )
        elif order.order_status_id == settings.ID_ORDER_STATUS_REFUNDED:
            message = _( "Your order was refunded." )

        # passes data to template
        template_data = {}
        template_data['order'] = order
        template_data['message'] = message
        template_data['user'] = user
        template_data['provider'] = provider
        if order.order_status_id == settings.ID_ORDER_STATUS_PENDING and order.boleto_url:
            template_data['boleto_url'] = order.boleto_url

        body = Mailer.build_body_from_template( 'emails/order_confirmation_user.html', template_data )
        return Mailer.send( _( 'Your Order Details' ), body, user.email, None, None, settings.EMAIL_NOTIFICATION_NEW_ORDER )


    @staticmethod
    def send_order_confirmation_provider( user, order, provider ):
        """
        Sends order confirmation to provider.

        We do NOT use translation here so that it will always be in english

        :param: user
        :param: order
        :param: provider
        """

        # Defines order message accordingly to status
        message = ''
        if order.order_status_id == settings.ID_ORDER_STATUS_PENDING:
            message = "The order was received and will be processed soon."
        elif order.order_status_id == settings.ID_ORDER_STATUS_APPROVED:
            message = "The order was approved."
        elif order.order_status_id == settings.ID_ORDER_STATUS_DENIED:
            message = "The order was denied."
        elif order.order_status_id == settings.ID_ORDER_STATUS_CANCELLED:
            message = "The order was cancelled."
        elif order.order_status_id == settings.ID_ORDER_STATUS_REFUNDED:
            message = "The order was refunded."

        template_data = {
            'order': order,
            'provider': provider,
            'message': message,
            'user': user,
        }
        body = Mailer.build_body_from_template( 'emails/order_confirmation_provider.html', template_data )
        return Mailer.send( 'Service Requested', body, provider.user.email )


    @staticmethod
    def send_order_download_link( user, order ):
        """
        Sends order download link to user

        :param: user
        :param: order
        """

        # passes data to template
        template_data = {}
        template_data['order'] = order
        template_data['user'] = user

        # Creates the download link
        base_secure_url = settings.BASE_URL_SECURE
        order_id_64 = urlsafe_base64_encode( force_bytes( order.pk ) )
        user_id_64 = urlsafe_base64_encode( force_bytes( order.user_id ) )
        product_id_64 = urlsafe_base64_encode( force_bytes( order.product_id ) )
        external_code_64 = urlsafe_base64_encode( force_bytes( order.external_code ) )
        template_data['download_link'] = base_secure_url + reverse( 'marketplace:order_download', args = ( order_id_64, user_id_64, product_id_64, external_code_64 ) )

        body = Mailer.build_body_from_template( 'emails/order_download_link.html', template_data )
        return Mailer.send( _( 'Your Download Link' ), body, user.email, None, None, settings.EMAIL_NOTIFICATION_NEW_ORDER )


    @staticmethod
    def send_notification( user, notification ):
        """
        Sends e-mail from site notifying an user of a relevant update

        :param: user
        :param: notification
        """
        template_data = { 'user': user, 'notification': notification }
        body = Mailer.build_body_from_template( 'emails/notification.html', template_data )
        return Mailer.send( notification.message, body, user.email, None, None, settings.EMAIL_NOTIFICATION_ACTIVITY )
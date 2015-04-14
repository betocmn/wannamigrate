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

        if not settings.IS_PROD:
            return True

        email = EmailMessage()
        email.content_subtype = "html"
        email.subject = subject
        email.body = body
        email.to = [to] if isinstance( to, str ) else to
        if from_email:
            email.from_email = from_email
        if cc:
            email.cc = cc
        if bcc:
            email.bcc = bcc
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
        template_data['logo_url'] = settings.EMAIL_LOGO_URL
        context = Context( template_data )
        content = template.render( context )
        return content


    @staticmethod
    def send_welcome_email( user ):
        """
        Sends welcome email to users

        :param: user
        """

        template_data = { 'user': user }
        body = Mailer.build_body_from_template( 'emails/welcome.html', template_data )
        return Mailer.send( _( 'Welcome to Wanna Migrate' ), body, user.email )


    @staticmethod
    def send_reset_password_email( user ):
        """
        Sends email with link to reset password

        :param: user
        """

        # create token
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token( user )

        # build link
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
        return Mailer.send( _( 'Contact: ' + subject ), body, settings.CONTACT_FORM_EMAIL )


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
        return Mailer.send( _( 'Professional Help Requested' ), body, settings.CONTACT_FORM_EMAIL )


    @staticmethod
    def send_order_confirmation( email, provider_service_type, order ):
        """
        Sends order confirmation to user

        :param: user
        """
        
        # Defines order message accordingly to status
        message = ''
        if order.order_status_id == 1:
            message = "Your payment was received and will be processed soon."
        elif order.order_status_id == 2:
            message = "Your payment was approved."
        elif order.order_status_id == 3:
            message = "Your payment was denied."
        elif order.order_status_id == 4:
            message = "Your payment was cancelled."
        elif order.order_status_id == 5:
            message = "Your payment was refunded."

        template_data = {
            'provider_service_type': provider_service_type,
            'order': order,
            'service_type': provider_service_type.service_type,
            'provider': provider_service_type.provider,
            'message': message
        }
        body = Mailer.build_body_from_template( 'emails/order_confirmation.html', template_data )
        return Mailer.send( _( 'Your Order Details' ), body, email )
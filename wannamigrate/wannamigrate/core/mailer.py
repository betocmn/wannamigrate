from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context

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

        email = EmailMessage()
        email.content_subtype = "html"
        email.subject = subject
        email.body = body
        email.to = to
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
        context = Context( template_data )
        content = template.render( context )
        return content

    @staticmethod
    def send_login_email( to, template_data ):
        """
        Sends welcome email to user, with his login details

        :param: template_data
        """

        body = Mailer.build_body_from_template( 'emails/user/login_details.html', template_data )
        return Mailer.send( 'Your Login Details', body, [to] )

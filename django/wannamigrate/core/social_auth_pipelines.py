# -*- coding: utf-8 -*-
import time
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from PIL import Image
from wannamigrate.core.util import get_object_or_false
from wannamigrate.core.models import UserPersonal
from wannamigrate.core.mailer import Mailer


def save_extra_data( backend, details, response, user = None, is_new = False, *args, **kwargs ):
    """
    Update user extra details using data from provider.

    :param: backedn
    :param: details
    :param: response
    :param: user
    :param: is_new
    :return: String
    """
    if user is None or not is_new:
        return

    user_personal = get_object_or_false( UserPersonal, user = user )
    if not user_personal:
        user_personal = UserPersonal()
        user_personal.user = user

    try:
        url = None
        full_name = None
        if backend.name == 'facebook' and "id" in response:
            url = "http://graph.facebook.com/%s/picture?width=600" \
                  % response["id"]
            full_name = response.get( 'name', '' )

        elif backend.name == 'google-oauth2':
            if "image" in response:
                url = response['image'].get('url').replace( 'sz=50', 'sz=600' )
            if "name" in response:
                full_name = response['name']['givenName'] + ' ' + response['name']['familyName']

        elif backend.name == 'linkedin':
            #if "pictureUrl" in response:
                #url = response["pictureUrl"]
            url = response['pictureUrls']['values'][0]
            if 'fullname' in details:
                full_name = details['fullname']

        # if we got a full name
        if full_name:
            user.name = full_name
            user.save()

        # If we got a profile image URL
        if url:
            avatar = urlopen( url )
            image_basename = slugify( user.name + " avatar" )
            image_name = '%s%s.jpg' % ( int( time.time() ), image_basename )
            user_personal.avatar.save( image_name, ContentFile( avatar.read() ) )

        # Sends Welcome Email to User
        # TODO Change this to a celery/signal background task
        Mailer.send_welcome_email( user )

    except ( URLError, HTTPError ):
        pass

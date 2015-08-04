#################
# Imports
#################
from __future__ import absolute_import
from celery import shared_task
from wannamigrate.core.models import User, UserStats, Notification, NotificationUser
from wannamigrate.core.mailer import Mailer
from wannamigrate.qa.models import Question, BlogPost, Answer
from django.utils import translation
from django.conf import settings
import time, os, subprocess
from django.core.management import execute_from_command_line
from datetime import timedelta
from django.utils import timezone


##########################
# Celery Tasks
##########################
@shared_task
def add_notification( compressed_message, url, users, send_email = False ):
    return Notification.add( compressed_message, url, users, send_email )


@shared_task
def send_welcome_email( user, type = 'user' ):

    # sets user language
    preferred_language = user.preferred_language
    if not preferred_language:
        preferred_language = 'en'
    translation.activate( preferred_language )

    # sends email
    return Mailer.send_welcome_email( user, type )





########################
# Cronjobs
########################
@shared_task
def clear_sessions():
    execute_from_command_line( ["manage.py", "clearsessions"] )


@shared_task
def database_backup():
    DATABASE_BACKUP_FOLDER = "/tmp"

    # Call mysqldump for each database configuration
    for k, db in settings.DATABASES.items():
        backup_path = DATABASE_BACKUP_FOLDER + '/' + db['NAME'] + '-' + time.strftime( "%Y-%m-%d-%H%M%S" ) + ".sql"
        dump_cmd = "sudo mysqldump -u {0} -p{1} {2} > {3}".format(
            db['USER'],
            db['PASSWORD'],
            db['NAME'],
            backup_path
        )
        os.system( dump_cmd )


@shared_task
def fix_counters():

    # Fix question counters
    questions = Question.objects.all()
    for q in questions:
        q.total_answers = q.answers.count()
        q.total_followers = q.followers.count()
        q.save()

    # Fix blogpost counters
    blogposts = BlogPost.objects.all()
    for b in blogposts:
        b.total_followers = b.followers.count()
        b.save()


@shared_task
def clear_notifications():
    last_month = timezone.now() - timedelta( days = 30 )
    Notification.objects.filter(created_date__lt=last_month).delete()
    NotificationUser.objects.filter(created_date__lt=last_month).delete()
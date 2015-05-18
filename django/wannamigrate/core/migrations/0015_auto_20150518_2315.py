# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings





#########################
# Migration functions
#########################
def populate_conversation_status( apps, schema_editor ):
    """
        Updates the slug value for existing topics
        :param: apps A reference to the apps.
        :param: schema_editor A reference to the schema_editor.
    """
    # Gets the vote type model manager
    ConversationStatus = apps.get_model( "core", "ConversationStatus" )

    # The ConversationStatus constants to be saved
    conversation_status = [
        { "id" : settings.CORE_CONVERSATION_STATUS_INBOX_ID, "name" : "Inbox" },
        { "id" : settings.CORE_CONVERSATION_STATUS_OUTBOX_ID, "name" : "Outbox" },
        { "id" : settings.CORE_CONVERSATION_STATUS_ARCHIVE_ID, "name" : "Archive" },
    ]
    # Save...
    for status in conversation_status:
        tmp = ConversationStatus()
        tmp.id = status[ "id" ]
        tmp.name = status[ "name" ]
        tmp.save()





#########################
# Migration configuration
#########################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20150518_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('subject', models.CharField(max_length=150, default='')),
                ('from_user', models.ForeignKey(related_name='conversations_started', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='conversations_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConversationMessage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('content', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('conversation', models.ForeignKey(related_name='messages', to='core.Conversation')),
                ('owner', models.ForeignKey(related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConversationStatus',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=50, default='')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConversationStatus_User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('conversation', models.ForeignKey(related_name='conversations_status', to='core.Conversation')),
                ('status', models.ForeignKey(related_name='conversations_status', to='core.ConversationStatus')),
                ('user', models.ForeignKey(related_name='conversations_status', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Message',
        ),

        migrations.RunPython( populate_conversation_status ),
    ]

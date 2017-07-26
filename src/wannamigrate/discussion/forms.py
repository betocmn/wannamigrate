"""
company FORMS

Form definitions used by views/templates from the product app
"""

##########################
# Imports
##########################
from django.forms import Textarea
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from wannamigrate.core.util import date_now
from wannamigrate.discussion.models import Discussion, DiscussionReply
from wannamigrate.core.forms import BaseModelForm
from wannamigrate.member.models import Member


#######################
# FORM Classes
#######################
class DiscussionForm(BaseModelForm):
    """
    Form for regular email/password login
    """

    class Meta:
        model = Discussion
        fields = ['description']

    def __init__(self, *args, **kwargs):
        """
        Injects user to the form

        :return: Model Object
        """
        if 'member_id' in kwargs:
            self.member_id = kwargs.pop("member_id")
        if 'country_id' in kwargs:
            self.country_id = kwargs.pop("country_id")
        super(DiscussionForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Set the request user before saving to the DB

        :return: Model Object
        """
        discussion = super(DiscussionForm, self).save(commit=False)
        if hasattr(self, 'member_id'):
            discussion.member_id = self.member_id
        if hasattr(self, 'country_id'):
            discussion.country_id = self.country_id
        if commit:
            discussion.content_modified_date = date_now()
            discussion.save()
        return discussion


class DiscussionUserForm(BaseModelForm):
    """
    Form for user's first and last name on Discussion
    """

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        """
        Make first name and last name required

        :return: Dictionary
        """
        super(DiscussionUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class DiscussionMemberForm(BaseModelForm):
    """
    Form for member's stage and visa on Discussion
    """

    class Meta:
        model = Member
        fields = ['stage', 'visa']

    def __init__(self, *args, **kwargs):
        """
        Make first name and last name required

        :return: Dictionary
        """
        super(DiscussionMemberForm, self).__init__(*args, **kwargs)
        self.fields['stage'].required = True


class DiscussionReplyForm(BaseModelForm):
    """
    Form for regular email/password login
    """

    class Meta:
        model = DiscussionReply
        fields = ['description']
        widgets = {
            'description': Textarea(attrs={
                'placeholder': _('Write a response...')
            })
        }

    def __init__(self, *args, **kwargs):
        """
        Injects user to the form

        :return: Model Object
        """
        if 'member_id' in kwargs:
            self.member_id = kwargs.pop("member_id")
        if 'discussion_id' in kwargs:
            self.discussion_id = kwargs.pop("discussion_id")
        super(DiscussionReplyForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Set the request user before saving to the DB

        :return: Model Object
        """
        discussion_reply = super(DiscussionReplyForm, self).save(commit=False)
        if hasattr(self, 'member_id'):
            discussion_reply.member_id = self.member_id
        if hasattr(self, 'discussion_id'):
            discussion_reply.discussion_id = self.discussion_id
        if commit:
            discussion_reply.save()
        return discussion_reply

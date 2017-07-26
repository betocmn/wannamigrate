"""
Product Views - Wines, gifts, etc...

These are the views that control logic flow for
the html templates
"""

##########################
# Imports
##########################
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import F
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from wannamigrate.discussion.models import Discussion, DiscussionReply, DiscussionReplyUpvote
from wannamigrate.discussion.forms import (
    DiscussionForm, DiscussionReplyForm, DiscussionUserForm, DiscussionMemberForm
)
from wannamigrate.member.models import Member
from wannamigrate.core.models import Country


#######################
# View Methods
#######################
def index(request, country_slug):
    """
    How it works

    :param request:
    :param country_slug:
    :return: String
    """

    # Retrieves all documents by document group
    discussions = Discussion.objects.select_related(
        'member', 'member__user', 'member__country', 'member__stage', 'member__visa'
    ).filter(
        country_id=request.session['country_id']
    ).order_by('-content_modified_date')

    # Checks if user has a discussion created
    member_discussion = None
    if request.user and request.user.is_authenticated:
        member_discussion = Discussion.objects.filter(member__user=request.user).first()

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'discussions': discussions,
        'member_discussion': member_discussion,
        'meta_title': _('Member Immigration Cases| Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'discussion/index.html', template_data)


def thread(request, country_slug, user_slug):
    """
    Discussion Thread

    :param request:
    :param country_slug:
    :param user_slug:
    :return: String
    """

    # Retrieves discussion
    discussion = Discussion.objects.select_related(
        'member', 'member__user', 'member__country', 'member__stage', 'member__visa'
    ).filter(
        member__user__slug=user_slug
    ).first()
    if not discussion:
        redirect('discussion:index', request.session['country_slug'])

    # Updates total views
    discussion.total_views = F('total_views') + 1
    discussion.save()

    # Retrieves member if logged
    member = None
    form = None
    can_edit_discussion = False
    if request.user.is_authenticated:
        member = Member.objects.filter(user=request.user).first()
        can_edit_discussion = discussion.member.user == request.user

        # Instantiates form
        form = DiscussionReplyForm(
            request.POST or None, discussion_id=discussion.id, member_id=member.id
        )

        # if FORM was submitted and is valid
        if form.is_valid():

            # Updates total replies
            discussion.total_replies = F('total_replies') + 1
            discussion.save()

            # Saves the reply
            discussion_reply = form.save()
            return redirect("%s#reply-%s" % (
                reverse(
                    'discussion:thread', args=(
                        request.session['country_slug'],
                        discussion_reply.discussion.member.user.slug
                    )
                ), discussion_reply.id
            ))

    # Retrieves all replies
    discussion_replies = DiscussionReply.objects.select_related(
        'discussion__member', 'discussion__member__user', 'discussion__member__country'
    ).filter(
        discussion=discussion
    ).order_by('-total_upvotes')

    # Retrieves all upvotes from this member on this discussion
    discussion_reply_ids = []
    if member:
        discussion_reply_ids = DiscussionReplyUpvote.objects.filter(
            member=member, discussion_reply__discussion=discussion
        ).values_list('discussion_reply_id', flat=True)

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'member': member,
        'form': form,
        'discussion_replies': discussion_replies,
        'discussion': discussion,
        'can_edit_discussion': can_edit_discussion,
        'discussion_reply_ids': discussion_reply_ids,
        'meta_title': _('Member Immigration Cases| Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'discussion/thread.html', template_data)


@login_required
def update(request, country_slug):
    """
    Add discussion for the logged-in user

    :param request:
    :param country_slug:
    :return: String
    """

    # Retrieves member
    member = Member.objects.filter(user=request.user).first()

    # Checks if user has a discussion created
    discussion = Discussion.objects.filter(member=member).first()

    # Instantiates Discussion Form
    if not discussion:
        country = Country.objects.filter(id=request.session['country_id']).first()
        discussion_form = DiscussionForm(
            request.POST or None, country_id=country.id, member_id=member.id
        )
    else:
        discussion_form = DiscussionForm(request.POST or None, instance=discussion)

    # Instantiates member and user FORMs
    user_form = DiscussionUserForm(request.POST or None, instance=member.user)
    member_initial = {}
    if not member.stage:
        member_initial['stage'] = 1
    if not member.visa:
        member_initial['visa'] = 1
    member_form = DiscussionMemberForm(
        request.POST or None, instance=member, initial=member_initial
    )

    # if FORMS were submitted
    if request.method == 'POST':

        # Saves forms
        validated = True

        if user_form.is_valid():
            user_form.save()
        else:
            validated = False

        if member_form.is_valid():
            member_form.save()
        else:
            validated = False

        if discussion_form.is_valid():
            discussion_form.save()
        else:
            validated = False

        if validated:
            messages.success(request, _('Your summary has been successfully saved.'))
            return redirect('discussion:thread', request.session['country_slug'], request.user.slug)

    # Builds template data dictionary
    template_data = {
        'discussion_form': discussion_form,
        'user_form': user_form,
        'member_form': member_form,
        'meta_title': _('Update My Case | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'discussion/update.html', template_data)


@login_required
def upvote(request, country_slug):
    """
    Updates total upvotes for the given discussion_reply_id

    :param request:
    :param country_slug:
    :return: String
    """

    # Searches for member
    member = Member.objects.get(user_id=request.user.id)

    # If upvote was submitted
    discussion_reply_id = request.POST.get('discussion_reply_id', False)
    if discussion_reply_id:

        # Searches if member has upvoted this or not
        discussion_reply_id = int(discussion_reply_id)
        discussion_reply = DiscussionReply.objects.filter(id=discussion_reply_id).first()
        if not discussion_reply:
            return JsonResponse({'status': 'error', 'message': 'Invalid reply.'})
        discussion_reply_upvote = DiscussionReplyUpvote.objects.filter(
            discussion_reply=discussion_reply, member=member
        ).first()
        if discussion_reply_upvote:

            # Removes upvote
            discussion_reply_upvote.delete()

            # Decrements total upvotes
            discussion_reply.total_upvotes = F('total_upvotes') - 1
            discussion_reply.save()

        else:

            # Adds upvote
            discussion_reply_upvote = DiscussionReplyUpvote()
            discussion_reply_upvote.member = member
            discussion_reply_upvote.discussion_reply_id = discussion_reply_id
            discussion_reply_upvote.save()

            # Increments total upvotes
            discussion_reply.total_upvotes = F('total_upvotes') + 1
            discussion_reply.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error', 'message': 'Invalid data requested'})


@login_required
def update_reply(request, country_slug, discussion_reply_id):
    """
    Edit a discussion reply

    :param request:
    :param country_slug:
    :param discussion_reply_id:
    :return: String
    """

    # Retrieves reply if it belongs to the logged user
    discussion_reply = DiscussionReply.objects.filter(
        member__user=request.user, id=discussion_reply_id
    ).first()
    if not discussion_reply:
        return redirect('discussion:index', request.session['country_slug'])

    # Instantiates form
    form = DiscussionReplyForm(request.POST or None, instance=discussion_reply)

    # if FORM was submitted and is valid
    if form.is_valid():

        # Saves the data and redirects with success message
        discussion_reply = form.save()
        messages.success(request, _('Your reply has been successfully updated.'))
        return redirect("%s#reply-%s" % (
            reverse(
                'discussion:thread',
                args=(request.session['country_slug'], discussion_reply.discussion.member.user.slug)
            ), discussion_reply.id
        ))

    # Builds template data dictionary
    template_data = {
        'form': form,
        'meta_title': _('Update My Reply | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'discussion/update_reply.html', template_data)

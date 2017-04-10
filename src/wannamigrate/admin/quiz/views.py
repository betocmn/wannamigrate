"""
Badges Views

These are the views that control logic flow for
the crud operations.
"""

##########################
# Imports
##########################
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import transaction
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from wannamigrate.admin.quiz.forms import QuizQuestionForm, QuizAnswerForm
from wannamigrate.core.decorators import restrict_internal_ips
from wannamigrate.core.util import build_datatable_json, get_object_or_false
from wannamigrate.admin.login.views import admin_check
from wannamigrate.quiz.models import QuizQuestion, QuizAnswer


#######################
# FRUIT VIEWS
#######################
@restrict_internal_ips
@permission_required('quiz.admin_add_quiz_question', login_url='admin:restricted')
@user_passes_test(admin_check)
@transaction.atomic
def add(request):
    """
    Add new Quiz Question

    :param: request
    :return: String
    """

    # Instantiates FORM
    quiz_question_form = QuizQuestionForm(request.POST or None, request.FILES or None)

    # Instantiates Formsets
    QuizAnswerInlineFormset = inlineformset_factory(
        QuizQuestion, QuizAnswer, form=QuizAnswerForm, extra=1, can_delete=True
    )
    quiz_answer_formset = QuizAnswerInlineFormset(
        request.POST or None, instance=quiz_question_form.instance
    )

    # If form was submitted, it tries to validate and save data
    if quiz_question_form.is_valid():

        # Saves Badge
        quiz_question = quiz_question_form.save()

        # Saves Badge Rules and Benefits Formsets
        if quiz_answer_formset.is_valid():
            quiz_answer_formset.save()

            # Redirects with success message
            messages.success(request, 'Quiz Question was successfully added.')
            return HttpResponseRedirect(reverse('admin:quiz:details', args=(quiz_question.id,)))

    # Template data
    template_data = {
        'quiz_question_form': quiz_question_form,
        'quiz_answer_formset': quiz_answer_formset,
        'cancel_url': reverse('admin:quiz:list')
    }

    # Print Template
    return render(request, 'admin/quiz/add.html', template_data)


@restrict_internal_ips
@permission_required('quiz.admin_delete_quiz_question', login_url='admin:restricted')
@user_passes_test(admin_check)
def delete(request, quiz_question_id):
    """
    Delete Badge action.
    In the case of quiz_questions, we never delete them, we just put as 'INACTIVE'

    :param: request
    :param: quiz_question_id
    :return: String
    """

    # Identifies database record
    quiz_question = get_object_or_404(QuizQuestion, pk=quiz_question_id)

    # Deletes quiz question
    quiz_question.delete()

    # Redirects with success message
    messages.success(request, 'Quiz Question was successfully deleted.')
    return HttpResponseRedirect(reverse('admin:quiz:list'))


@restrict_internal_ips
@permission_required('quiz.admin_view_quiz_question', login_url='admin:restricted')
@user_passes_test(admin_check)
def details(request, quiz_question_id):
    """
    View Badge page

    :param: request
    :param: quiz_question_id
    :return: String
    """

    # Identifies database record
    quiz_question = get_object_or_404(QuizQuestion, pk=quiz_question_id)

    # Template data
    context = {
        'quiz_question': quiz_question,
        'urls': {
            'back': reverse('admin:quiz:list'),
            'add': reverse('admin:quiz:add'),
            'edit': reverse('admin:quiz:edit', args=(quiz_question.id,)),
            'delete': reverse('admin:quiz:delete', args=(quiz_question.id,)),
        }
    }

    # Print Template
    return render(request, 'admin/quiz/details.html', context)


@restrict_internal_ips
@permission_required('quiz.admin_change_quiz_question', login_url='admin:restricted')
@user_passes_test(admin_check)
@transaction.atomic
def edit(request, quiz_question_id):
    """
    Edit Badge personal data

    :param: request
    :param: quiz_question_id
    :return: String
    """

    # Identifies database record
    quiz_question = get_object_or_404(QuizQuestion, pk=quiz_question_id)

    # Instantiates FORM
    quiz_question_form = QuizQuestionForm(request.POST or None, request.FILES or None,
                                          instance=quiz_question)

    # Instantiates Formsets
    QuizAnswerInlineFormset = inlineformset_factory(
        QuizQuestion, QuizAnswer, form=QuizAnswerForm, extra=1, can_delete=True
    )
    quiz_answer_formset = QuizAnswerInlineFormset(
        request.POST or None, instance=quiz_question_form.instance
    )

    # If form was submitted, it tries to validate and save data
    if quiz_question_form.is_valid():

        # Saves Badge
        quiz_question = quiz_question_form.save()

        # Saves Badge Rules and Benefits Formsets
        if quiz_answer_formset.is_valid():
            quiz_answer_formset.save()

            # Redirects with success message
            messages.success(request, 'Quiz Question was successfully updated.')
            return HttpResponseRedirect(reverse('admin:quiz:details', args=(quiz_question.id,)))

    # Template data
    template_data = {
        'quiz_question_form': quiz_question_form,
        'quiz_answer_formset': quiz_answer_formset,
        'cancel_url': reverse('admin:quiz:details', args=(quiz_question_id,))
    }

    # Print Template
    return render(request, 'admin/quiz/edit.html', template_data)


@restrict_internal_ips
@permission_required('quiz.admin_view_quiz_question', login_url='admin:restricted')
@user_passes_test(admin_check)
def list(request):
    """
    Lists all promo_codes with pagination, order by, search, etc. using www.datatables.net

    :param: request
    :return: String
    """

    context = {}
    return render(request, 'admin/quiz/list.html', context)


@restrict_internal_ips
@permission_required('quiz.admin_view_quiz_question', login_url='admin:restricted')
@user_passes_test(admin_check)
def list_json(request):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :return: String
    """

    # Query data
    objects = QuizQuestion.objects.select_related('country').order_by(
        'country__name'
    )

    # settings
    info = {
        'fields_to_select': [
            'id', 'country.name', 'sort_order', 'description'
        ],
        'fields_to_search': [
            'id', 'country__name', 'description'
        ],
        'default_order_by': 'country__name',
        'url_base_name': 'quiz',
        'namespace': 'admin:'
    }

    # builds json data and return it to the screen
    json = build_datatable_json(request, objects, info)
    return HttpResponse(json)

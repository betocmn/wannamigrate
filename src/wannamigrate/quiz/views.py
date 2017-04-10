"""
Product Views - Wines, gifts, etc...

These are the views that control logic flow for
the html templates
"""

##########################
# Imports
##########################
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import (
    login as auth_login, authenticate
)
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.util import get_object_or_false
from wannamigrate.core.models import Country
from wannamigrate.quiz.models import QuizQuestion, QuizAnswer
from wannamigrate.member.models import Member
from wannamigrate.quiz.forms import SignupQuizForm
from wannamigrate.quiz.models import QuizAnswer


#######################
# Methods
#######################
@login_required
def result(request, slug):
    """
    Quiz Result

    :param request:
    :param slug:
    :return: String
    """

    # Identifies country
    country = get_object_or_false(Country, slug=slug)
    if not country:
        return redirect('quiz:take', slug=slug)

    # Calculates total points from quiz answers
    member = get_object_or_false(Member, user=request.user)
    answers = member.quiz_answers.filter(
        quiz_question__country_id=country,
    ).aggregate(total_points=Sum('points'))
    if not answers['total_points']:
        return redirect('quiz:take', slug=slug)

    # Builds template data dictionary
    template_data = {
        'user': request.user,
        'total_points': answers['total_points'],
        'country': country,
        'meta_title': _('Quiz Results | Wanna Migrate'),
    }

    # Displays HTML template
    return render(request, 'quiz/result.html', template_data)


def take(request, slug):
    """
    Quiz landing-page.

    :param request:
    :param slug:
    :return: String
    """

    # Identifies country
    country = get_object_or_false(Country, slug=slug)
    if not country:
        return redirect('landing:home')

    # Checks if it's a member or a visitor
    member = None
    existing_member = False
    member_answers = []
    if request.user.is_authenticated():
        member = Member.objects.get(user_id=request.user.id)
        member_answers = member.quiz_answers.values_list('id', flat=True)

    # Instantiates signup form
    signup_form = SignupQuizForm(request.POST or None)

    # If form was submitted
    if request.method == 'POST':

        # Searches for all answers given by the user
        error = ''
        answer_id_list = [x for x in request.POST.getlist('answers') if x]
        member_answers = QuizAnswer.objects.filter(
            id__in=answer_id_list, quiz_question__country=country
        )

        # Saves user if not existing
        if not member:
            if signup_form.is_valid():
                member = signup_form.save()
                if member is not None:
                    user = member.user
                    auth_user = authenticate(
                        email=user.email, id=user.id, password_hash=user.password
                    )
                    auth_login(request, auth_user)

                    # Track quiz completion (only first time done)
                    request.session['track_quiz_completion'] = True

                    # Tracks user alias if first signup
                    if 'user_is_pending_tracking_alias' not in request.session:
                        request.session['user_is_pending_tracking_alias'] = True

            else:

                # Checks if it's an existing member who already signed up, if so, redirect to login
                existing_email = signup_form.cleaned_data.get('email', False)
                if existing_email:
                    user = get_object_or_false(get_user_model(), email=existing_email)
                    if user and user.has_updated_password:
                        existing_member = get_object_or_false(Member, user_id=user.id)

                # If invalid email
                if not existing_member:
                    error += "The email is invalid or already in use."

        # If everything is ok
        if not error:

            # If existing member, save in session to ask for password first
            if existing_member:

                request.session['quiz_answers_to_save'] = {
                    'quiz_answers': member_answers
                }
                request.session.modified = True
                messages.error(
                    request, "You already have an account. Please login to save your results"
                )
                return redirect(
                    '%s?next=%s' % (
                        reverse("member:login"),
                        reverse("quiz:result", args=(country.slug,))
                    )
                )

            else:

                # Saves member quiz answers
                member.quiz_answers = member_answers

            # Redirects to Quiz Results Pages
            return redirect("quiz:result", country.slug)

        else:

            # Invalid answers or email were provided
            messages.error(request, error)

    # Searches for all questions/answers to be displayed
    quiz_questions = QuizQuestion.objects.prefetch_related('quizanswer_set').filter(
        country=country
    ).order_by('sort_order')

    # Passes data and renders html template
    template_data = {
        'country': country,
        'quiz_questions': quiz_questions,
        'member_answers': member_answers,
        'total_questions': quiz_questions.count(),
        'meta_title': _('Immigration Quiz') + ' | %s | ' % _(country.name) + 'Wanna Migrate',
    }
    return render(request, 'quiz/take.html', template_data)





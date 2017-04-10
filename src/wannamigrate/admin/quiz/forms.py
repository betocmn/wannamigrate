"""
Admin FORMS

Form definitions used by views/templates from the admin app
"""

##########################
# Imports
##########################
from django.forms import ValidationError
from wannamigrate.core.forms import BaseModelForm
from wannamigrate.quiz.models import QuizQuestion, QuizAnswer


#######################
# QUIZ
#######################
class QuizQuestionForm(BaseModelForm):
    """
    Form for ADD and EDIT BADGES
    """

    class Meta:
        model = QuizQuestion
        fields = QuizQuestion.get_presentation_fields('raw')

    def clean(self):
        """
        Extra validation

        :return: Dictionary
        """
        cleaned_data = super(QuizQuestionForm, self).clean()

        # Sort Order validation
        sort_order = cleaned_data.get("sort_order", None)
        country = cleaned_data.get("country", None)
        if sort_order:
            sort_order_exists = QuizQuestion.objects.filter(
                country=country, sort_order=sort_order
            )
            if self.instance and self.instance.id:
                sort_order_exists = sort_order_exists.exclude(pk=self.instance.id)
            sort_order_exists = sort_order_exists.exists()
            if sort_order_exists:
                raise ValidationError("There's another question using this sort order.")
            
        return cleaned_data


class QuizAnswerForm(BaseModelForm):
    """
    Formset for badge rules
    """

    class Meta:
        model = QuizAnswer
        fields = QuizAnswer.get_presentation_fields('raw')

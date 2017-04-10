"""
Quiz model classes.

Magic to discover the customer's wine tastes
"""

##########################
# Imports
##########################
from stdimage.models import StdImageField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.models import BaseModel
from wannamigrate.core.util import CustomUploadToAutoSlugClassNameDir


##########################
# Classes definitions
##########################
class QuizAnswer(BaseModel):
    """
    Answer
    """

    # Model Attributes
    quiz_question = models.ForeignKey("QuizQuestion", verbose_name=_("question"))
    description = models.CharField(_("answer"), max_length=100)
    points = models.PositiveSmallIntegerField(_("points"))

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Quiz Answers',
            'fields': [
                'description', 'points'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.description))


class QuizQuestion(BaseModel):
    """
    Questions
    """

    # Model Attributes
    country = models.ForeignKey("core.Country", verbose_name=_("country"))
    description = models.CharField(_("question"), max_length=200)
    sort_order = models.PositiveSmallIntegerField(_("sort order"), default=1)
    photo = StdImageField(
        _("photo"), blank=True, null=True,
        upload_to=CustomUploadToAutoSlugClassNameDir(populate_from='description'),
        variations={
            'thumbnail': (50, 50, True),
        }
    )

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Quiz Question',
            'fields': [
                'country', 'description', 'sort_order', 'photo'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_quiz_question", "ADMIN: Can add quiz question"),
            ("admin_change_quiz_question", "ADMIN: Can change quiz question"),
            ("admin_delete_quiz_question", "ADMIN: Can delete quiz question"),
            ("admin_view_quiz_question", "ADMIN: Can view quiz questions")
        )

    # Method Definitions
    def __str__(self):
        return '%s' % (_(self.description))

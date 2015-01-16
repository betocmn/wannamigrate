from django.db import models
from wannamigrate.core.models import (
    BaseModel, Country
)
from django.utils.translation import ugettext_lazy as _


class Answer( BaseModel ):
    """
    Answer Model - These are possible answers for questions (immigration requirements)
    """

    # Model Attributes
    question = models.ForeignKey( 'Question', verbose_name = _( 'question' ) )
    description = models.CharField(  _( 'Answer' ), max_length = 255 )

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        return '%s' % ( _( self.description ) )


class CountryConfig( BaseModel ):
    """
    Country Config Model - Stores maximum immigration points per country, etc.
    """

    country = models.OneToOneField( Country, verbose_name = _( 'country' ) )
    pass_mark_points = models.IntegerField( _( "pass mark points" ), default = 0 )
    max_personal_points = models.IntegerField( _( "max personal points" ), default = 0 )
    max_language_points = models.IntegerField( _( "max language points" ), default = 0 )
    max_education_points = models.IntegerField( _( "max education points" ), default = 0 )
    max_work_points = models.IntegerField( _( "max education points" ), default = 0 )
    max_total_points = models.IntegerField( _( "max total points" ), default = 0 )

    # META Options
    class Meta:
        default_permissions = []


class CountryPoints( BaseModel ):
    """
    Country Points Model - Stores the total points for each answer in each country avaiblable
    """

    # Model Attributes
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    answer = models.ForeignKey( Answer, verbose_name = _( 'answer' ) )
    points = models.IntegerField( _( "points" ) )

    # META Options
    class Meta:
        default_permissions = []
        unique_together = ( "answer", "country" )

    @staticmethod
    def get_all_points_per_question( question_id ):
        """
        Get answers and points for every enabled country per question

        :param: self
        :param: question_id
        :return: Dictionary
        """

        sql = """ SELECT points_countrypoints.id, core_answer.id as answer_id, points_countrypoints.points, points_countrypoints.country_id
                  FROM core_answer
                  INNER JOIN points_countrypoints ON core_answer.id = points_countrypoints.answer_id
                  INNER JOIN core_country ON core_country.id = points_countrypoints.country_id
                  INNER JOIN points_question ON core_answer.question_id = points_question.id
                  WHERE core_country.immigration_enabled = 1 AND points_question.id = %s
                  ORDER BY core_country.name ASC """

        points = CountryPoints.objects.raw( sql, [question_id] )

        points_per_country = {}
        for point in points:
            if not point.country_id in points_per_country:
                points_per_country[point.country_id] = {}
            points_per_country[point.country_id][point.answer_id] = point.points

        return points_per_country


class Occupation( BaseModel ):
    """
    Occupation Model - These are the possible occupations required in the countries of destination
    """

    # Model Attributes
    occupation_category = models.ForeignKey( 'OccupationCategory', verbose_name = _( 'category' ) )
    name = models.CharField(  _( 'Name' ), max_length = 180 )
    countries = models.ManyToManyField( Country )

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_occupation", "ADMIN: Can add occupation" ),
            ( "admin_change_occupation", "ADMIN: Can change occupation" ),
            ( "admin_delete_occupation", "ADMIN: Can delete occupation" ),
            ( "admin_view_occupation", "ADMIN: Can view occupations" )
        )

    def __str__( self ):
        return '%s' % ( _( self.name ) )


class OccupationCategory( BaseModel ):
    """
    Answer Category Model - Some answers are grouped into categories
    """

    # Model Attributes
    name = models.CharField(  _( 'Name' ), max_length = 100 )

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        return '%s' % ( _( self.name ) )


class Question( BaseModel ):
    """
    Question Model - Question is a requirement asked for the immigration candidate
    """

    # Model Attributes
    description = models.CharField( _( "question" ), max_length = 255 )
    help_text = models.TextField( _( "help text" ), null = True, blank = True )
    method_name = models.CharField( _( "method name" ), max_length = 60 )
    type = models.CharField( _( "type" ), max_length = 15 )

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_immigration_rule", "ADMIN: Can add immigration rule" ),
            ( "admin_change_immigration_rule", "ADMIN: Can change immigration rule" ),
            ( "admin_delete_immigration_rule", "ADMIN: Can delete immigration rule" ),
            ( "admin_view_immigration_rule", "ADMIN: Can view immigration rules" )
        )

    def __str__( self ):
        return '%s' % ( _( self.description ) )


class QuestionGroup( BaseModel ):
    """
    Question Group Model - some questions are grouped to have a maximum number of points allowed when combined (per country)
    """

    # Model Attributes
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    name = models.TextField( _( "name" ) )
    max_points = models.IntegerField( _( "max points allowed" ), default = 0 )
    questions = models.ManyToManyField( Question )

    # META Options
    class Meta:
        default_permissions = []


class UserResult( BaseModel ):
    """
    User Restul Model - Stores the final result score of an user for each country available
    """

    # Model Attributes
    user = models.ForeignKey( 'core.User', verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    user_result_status = models.ForeignKey( 'UserResultStatus', verbose_name = _( 'result status' ) )
    score_total = models.IntegerField( _( "total score" ))
    score_personal = models.IntegerField( _( "score personal" ))
    score_language = models.IntegerField( _( "score language" ))
    score_education = models.IntegerField( _( "score education" ))
    score_work = models.IntegerField( _( "score work" ))

    # META Options
    class Meta:
        default_permissions = []
        unique_together = ( "user", "country" )


class UserResultStatus( BaseModel ):
    """
    User Result Status Model
    """

    # Model Attributes
    name = models.CharField(  _( 'Name' ), max_length = 100 )

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        return '%s' % ( _( self.name ) )
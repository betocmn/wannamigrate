from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Group
)
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID

class BaseModel( models.Model ):
    """
    BASE MODEL - The father of all :)
    """

    # META Options
    class Meta:
        abstract = True

    # Default timestamp fields to be used on all models
    created_date = models.DateTimeField( _( 'created date' ), auto_now_add = True, auto_now = False )
    modified_date = models.DateTimeField( _( 'modified date' ), auto_now = True, auto_now_add = False )


class Answer( BaseModel ):
    """
    Answer Model - These are possible answers for questions (immigration requirements)
    """

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        return '%s' % ( _( self.description ) )

    # Model Attributes
    question = models.ForeignKey( 'Question', verbose_name = _( 'question' ) )
    answer_category = models.ForeignKey( 'AnswerCategory', blank = True, null = True, verbose_name = _( 'category' ) )
    description = models.CharField(  _( 'Answer' ), max_length = 255 )


class AnswerCategory( BaseModel ):
    """
    Answer Category Model - Some answers are grouped into categories
    """

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        return '%s' % ( _( self.name ) )

    # Model Attributes
    question = models.ForeignKey( 'Question', verbose_name = _( 'question' ) )
    name = models.CharField(  _( 'Name' ), max_length = 100 )


class Continent( BaseModel ):
    """
    Continent Model - ex: Oceania, Europe, etc.
    """

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        return '%s' % ( _( self.name ) )

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 100 )


class Country( BaseModel ):
    """
    Country Model - ex: Brazil, Australia, USA, etc.
    """

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        return '%s' % ( _( self.name ) )

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 100 )
    continent = models.ForeignKey( 'Continent', verbose_name =  _( "continent" ) )
    code = models.CharField( _( "code" ), max_length = 2 )
    immigration_enabled = models.BooleanField( _( "immigration enabled?" ), default = False )


class CountryPoints( BaseModel ):
    """
    Country Points Model - Stores the total points for each answer in each country avaiblable
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    answer = models.ForeignKey( Answer, verbose_name = _( 'answer' ) )
    points = models.IntegerField( _( "points" ) )

    @staticmethod
    def get_all_points_per_question( question_id ):
        """
        Get answers and points for every enabled country per question

        :param: self
        :param: question_id
        :return: Dictionary
        """

        sql = """ SELECT core_countrypoints.id, core_answer.id as answer_id, core_countrypoints.points, core_countrypoints.country_id
                  FROM core_answer
                  INNER JOIN core_countrypoints ON core_answer.id = core_countrypoints.answer_id
                  INNER JOIN core_country ON core_country.id = core_countrypoints.country_id
                  INNER JOIN core_question ON core_answer.question_id = core_question.id
                  WHERE core_country.immigration_enabled = 1 AND core_question.id = %s
                  ORDER BY core_country.name ASC """

        points = CountryPoints.objects.raw( sql, [question_id] )

        points_per_country = {}
        for point in points:
            if not point.country_id in points_per_country:
                points_per_country[point.country_id] = {}
            points_per_country[point.country_id][point.answer_id] = point.points

        return points_per_country


class Language( BaseModel ):
    """
    Language Model - Ex: english, french, portuguese, etc.
    """

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        return '%s' % ( _( self.name ) )

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 25 )
    code = models.CharField( _( "code" ), max_length = 6 )


class Question( BaseModel ):
    """
    Question Model - Question is a requirement asked for the immigration candidate
    """

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

    # Model Attributes
    description = models.CharField( _( "question" ), max_length = 255 )
    help_text = models.TextField( _( "help text" ), null = True, blank = True )


class UserManager( BaseUserManager ):
    """
    User Manager - part of custom auth: https://docs.djangoproject.com/en/dev/topics/auth/customizing/
    """

    def create_user( self, email, name = None, password = None ):
        """
        Creates and saves a User with the given email, name and password.
        """

        if not email:
            raise ValueError( 'Users must have an email address' )

        user = self.model(
            email = self.normalize_email( email ),
            name = name,
        )

        user.set_password( password )
        user.save( using = self._db )
        return user

    def create_superuser( self, email, password, name = None ):
        """
        Creates and saves a superuser with the given email, name and password.
        """

        user = self.create_user(email,
            password = password,
            name = name
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.save( using = self._db )
        return user


class User( AbstractBaseUser, PermissionsMixin, BaseModel ):
    """
    User Model - part of custom auth: https://docs.djangoproject.com/en/dev/topics/auth/customizing/
    """

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ( "admin_add_user", "ADMIN: Can add user" ),
            ( "admin_change_user", "ADMIN: Can change user" ),
            ( "admin_delete_user", "ADMIN: Can delete user" ),
            ( "admin_view_user", "ADMIN: Can view users" ),
            ( "admin_add_admin_user", "ADMIN: Can add admin user" ),
            ( "admin_change_admin_user", "ADMIN: Can change admin user" ),
            ( "admin_delete_admin_user", "ADMIN: Can delete admin user" ),
            ( "admin_view_admin_user", "ADMIN: Can view admin users" )
        )

    # Model Attributes
    email = models.EmailField( _( "e-mail" ), max_length = 255, unique = True )
    name = models.CharField( _( "name" ), max_length = 120, null = True, default = '' )
    is_active = models.BooleanField( _( "is active?" ), default = True )
    is_admin = models.BooleanField( _( "is admin?" ), default = False )

    # Manager
    objects = UserManager()

    # Name of field that should be used as username
    USERNAME_FIELD = 'email'

    def get_full_name( self ):
        # The user is identified by their email address
        return self.name if self.name else self.email

    def get_short_name( self ):
        # The user is identified by their email address
        return self.email

    def __str__( self ):
        return self.email

    @property
    def is_staff( self ):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserEducation( BaseModel ):
    """
    User Education Model - Ex: Stores education related information
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    regional_australia_study = models.BooleanField( _( "studied in regional australia?" ), default = False )
    partner_education_level_answer = models.ForeignKey( Answer, related_name = 'partner_education_level_answer', verbose_name = _( 'partner education level' ), blank = True, null = True )


class UserEducationHistory( BaseModel ):
    """
    User Education History Model - Ex: Stores each education achieved (ex: bachelors, in brazil, universidade UFMA, from 2003-2007
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    education_level_answer = models.ForeignKey( Answer, related_name = 'education_level', verbose_name = _( 'education level' ) )
    school = models.CharField( _( "school" ), max_length = 100 )
    year_start = models.CharField( _( "start year" ), max_length = 4 )
    year_end = models.CharField( _( "end year" ), max_length = 4 )


class UserLanguage( BaseModel ):
    """
    User Language Model - Ex: Stores language related information
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    australian_community_language = models.BooleanField( _( "credentialled community language in australia?" ), default = False )
    partner_english_level_answer = models.ForeignKey( Answer, related_name = 'partner_english_level_answer', verbose_name = _( 'partner english level' ), on_delete = models.PROTECT, blank = True, null = True  )
    partner_french_level_answer = models.ForeignKey( Answer, related_name = 'partner_french_level_answer', verbose_name = _( 'partner french level' ), on_delete = models.PROTECT, blank = True, null = True  )

class UserLanguageProficiency( BaseModel ):
    """
    User Language Proficiency Model - Ex: Stores each language and level the user can speak
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    language = models.ForeignKey( Language, verbose_name = _( 'language' ) )
    language_level_answer = models.ForeignKey( Answer, verbose_name = _( 'language level' ), on_delete = models.PROTECT )


class UserLoginHistory( BaseModel ):
    """
    User Login History - Ex: Records every time an user logs in to the system
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    is_logout = models.BooleanField( _( "is logout" ), default = False )


class UserPersonal( BaseModel ):
    """
    User Personal Model - Ex: Stores personal information from the user, such as age, gender, etc..

    Using this for image resize: https://github.com/codingjoe/django-stdimage
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    GENDERS = (
        ( 'F', _( 'Female' ) ),
        ( 'M', _( 'Male' ) )
    )
    BOOLEAN_CHOICES = (
        ( True, _( 'Yes' ) ),
        ( False, _( 'No' ) )
    )

    user = models.OneToOneField( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country of residence' ), blank = True, null = True )
    avatar = StdImageField( _( "avatar" ), upload_to = settings.UPLOAD_USER_PICTURE_FOLDER, blank = True, null = True, variations = {
        'large': (600, 400),
        'thumbnail': (40, 40, True ),
        'medium': (300, 200),
    })
    birth_date = models.DateField( _( "birth date" ), blank = True, null = True  )
    gender = models.CharField( _( "gender" ), max_length = 1, choices = GENDERS, blank = True, null = True, default = None )
    australian_regional_immigration = models.NullBooleanField( _( "Would you be willing to live in Regional Australia?" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )
    family_overseas = models.NullBooleanField( _( "Any family members who are citizens in other countries?" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )


class UserPersonalFamily( BaseModel ):
    """
    User Personal Family Model - Ex: Stores countries where the user has relatives as citizens
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )


class UserResult( BaseModel ):
    """
    User Restul Model - Stores the final result score of an user for each country available
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    score_total = models.IntegerField( _( "total score" ))
    score_personal = models.IntegerField( _( "score personal" ))
    score_language = models.IntegerField( _( "score language" ))
    score_education = models.IntegerField( _( "score education" ))
    score_work = models.IntegerField( _( "score work" ))


class UserWork( BaseModel ):
    """
    User Work Model - Ex: Stores work related information
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    occupation_answer = models.ForeignKey( Answer, verbose_name = _( 'occupation' ), blank = True, null = True )
    partner_skills = models.BooleanField( _( "partner skills?" ), default = False )
    willing_to_invest = models.BooleanField( _( "willing to invest?" ), default = False )
    canadian_startup_letter = models.BooleanField( _( "startup letter from canada?" ), default = False )
    australian_professional_year = models.BooleanField( _( "professional year course in australia?" ), default = False )
    canadian_partner_work_study_experience = models.BooleanField( _( "has partner worked or studied in canada?" ), default = False )


class UserWorkOffer( BaseModel ):
    """
    User Work Offer Model - Ex: Stores countries where the user has written job offers
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )


class UserWorkExperience( BaseModel ):
    """
    User Work Experience Model - Ex: Stores each work experience
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    occupation_answer = models.ForeignKey( Answer, verbose_name = _( 'occupation' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    company = models.CharField( _( "company" ), max_length = 100 )
    start_date = models.DateField( _( "start date" ) )
    end_date = models.DateField( _( "end date" ) )
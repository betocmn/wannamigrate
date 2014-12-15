from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Group
)
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID
import math
from wannamigrate._settings.base import LANGUAGES

class BaseModel( models.Model ):
    """
    BASE MODEL - The father of all :)
    """

    # Default timestamp fields to be used on all models
    created_date = models.DateTimeField( _( 'created date' ), auto_now_add = True, auto_now = False )
    modified_date = models.DateTimeField( _( 'modified date' ), auto_now = True, auto_now_add = False )

    # META Options
    class Meta:
        abstract = True


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


class Continent( BaseModel ):
    """
    Continent Model - ex: Oceania, Europe, etc.
    """

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 100 )

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        return '%s' % ( _( self.name ) )


class Country( BaseModel ):
    """
    Country Model - ex: Brazil, Australia, USA, etc.
    """

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 100 )
    continent = models.ForeignKey( 'Continent', verbose_name =  _( "continent" ) )
    code = models.CharField( _( "code" ), max_length = 2 )
    immigration_enabled = models.BooleanField( _( "immigration enabled" ), default = False )
    points = models.ManyToManyField( Answer, through = 'CountryPoints' )

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        """
        String representation of this model
        :return: String
        """
        return '%s' % ( _( self.name ) )

    @staticmethod
    def get_translated_tuple():
        """
        Returns a tuple of records ordered by name, after translation.
        It's used on dropdowns on forms
        :return: String
        """
        countries = Country.objects.order_by( 'name' )
        result = []
        for country in countries:
            result.append( ( country.id, _( country.name ) ) )
        result = sorted( result, key = lambda x: x[1] )
        return tuple( [( '', _( 'Select Country' ) )] + result  )


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

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 25 )
    code = models.CharField( _( "code" ), max_length = 6 )

    # META Options
    class Meta:
        default_permissions = []

    def __str__( self ):
        return '%s' % ( _( self.name ) )

    @staticmethod
    def get_translated_tuple():
        """
        Returns a tuple of records ordered by name, after translation.
        It's used on dropdowns on forms
        :return: String
        """
        languages = Language.objects.order_by( 'name' )
        result = []
        for language in languages:
            result.append( ( language.id, language.name ) )
        result = sorted( result, key = lambda x: x[1] )
        return tuple( [( '', _( 'Select Language' ) )] + result  )


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

    # Model Attributes
    email = models.EmailField( _( "e-mail" ), max_length = 255, unique = True )
    name = models.CharField( _( "name" ), max_length = 120, null = True, default = '' )
    is_active = models.BooleanField( _( "is active" ), default = True )
    is_admin = models.BooleanField( _( "is admin" ), default = False )
    results = models.ManyToManyField( Country, through = 'UserResult' )
    preferred_language = models.CharField( _( "Language" ), max_length = 6, choices = LANGUAGES, default = 'en' )

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

    # Model Attributes
    BOOLEAN_CHOICES = (
        ( True, _( 'Yes' ) ),
        ( False, _( 'No' ) )
    )
    user = models.OneToOneField( User, verbose_name = _( 'user' ) )
    regional_australia_study = models.NullBooleanField( _( "Did you complete any studies in a regional part of Australia" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )
    partner_education_level_answer = models.ForeignKey( Answer, related_name = 'partner_education_level_answer', verbose_name = _( 'partner/spouse education level' ), blank = True, null = True )

    # META Options
    class Meta:
        default_permissions = []

    def get_completed_percentage( self ):
        """
        Check how many fields are filled on user_language tables and get the total percentage of completion

        :return: Int
        """

        # Fields to check for values inserted by user
        fields = [ 'regional_australia_study', 'partner_education_level_answer' ]

        # Total is number of fileds + 1 for the UserEducationHistory table
        total = len( fields ) + 1
        completed = 0

        # Check on user_language fields
        for field in fields:
            value = getattr( self, field )
            if value is not None:
                completed += 1

        # Check if there is at least one record on user_language_proficiency
        if self.user.usereducationhistory_set.count():
            completed += 1

        return math.floor( ( completed * 100 ) / total )


class UserEducationHistory( BaseModel ):
    """
    User Education History Model - Ex: Stores each education achieved (ex: bachelors, in brazil, universidade UFMA, from 2003-2007
    """

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    education_level_answer = models.ForeignKey( Answer, related_name = 'education_level', verbose_name = _( 'education level' ) )
    school = models.CharField( _( "school/university" ), max_length = 100 )
    year_start = models.CharField( _( "start year" ), max_length = 4 )
    year_end = models.CharField( _( "end year" ), max_length = 4 )

    # META Options
    class Meta:
        default_permissions = []


class UserLanguage( BaseModel ):
    """
    User Language Model - Ex: Stores language related information
    """

    # Model Attributes
    user = models.OneToOneField( User, verbose_name = _( 'user' ) )
    partner_english_level_answer = models.ForeignKey( Answer, related_name = 'partner_english_level_answer', verbose_name = _( 'partner/spouse english level' ), on_delete = models.PROTECT, blank = True, null = True  )
    partner_french_level_answer = models.ForeignKey( Answer, related_name = 'partner_french_level_answer', verbose_name = _( 'partner/spouse french level' ), on_delete = models.PROTECT, blank = True, null = True  )

    # META Options
    class Meta:
        default_permissions = []

    def get_completed_percentage( self ):
        """
        Check how many fields are filled on user_language tables and get the total percentage of completion

        :return: Int
        """

        # Fields to check for values inserted by user
        fields = [ 'partner_english_level_answer', 'partner_french_level_answer' ]

        # Total is number of fileds + 1 for the UserLanguageProficiency table
        total = len( fields ) + 1
        completed = 0

        # Check on user_language fields
        for field in fields:
            value = getattr( self, field )
            if value is not None:
                completed += 1

        # Check if there is at least one record on user_language_proficiency
        if self.user.userlanguageproficiency_set.count():
            completed += 1

        return math.floor( ( completed * 100 ) / total )


class UserLanguageProficiency( BaseModel ):
    """
    User Language Proficiency Model - Ex: Stores each language and level the user can speak
    """

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    language = models.ForeignKey( Language, verbose_name = _( 'language' ) )
    language_level_answer = models.ForeignKey( Answer, verbose_name = _( 'language level' ), on_delete = models.PROTECT )

    # META Options
    class Meta:
        default_permissions = []


class UserLoginHistory( BaseModel ):
    """
    User Login History - Ex: Records every time an user logs in to the system
    """

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    is_logout = models.BooleanField( _( "is logout" ), default = False )

    # META Options
    class Meta:
        default_permissions = []


class UserPersonal( BaseModel ):
    """
    User Personal Model - Ex: Stores personal information from the user, such as age, gender, etc..

    Using this for image resize: https://github.com/codingjoe/django-stdimage
    """

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
    country = models.ForeignKey( Country, verbose_name = _( 'country of citizenship' ), blank = True, null = True )
    avatar = StdImageField( _( "avatar" ), upload_to = settings.UPLOAD_USER_PICTURE_FOLDER, blank = True, null = True, variations = {
        'large': ( 600, 400 ),
        'thumbnail': ( 40, 40, True ),
        'medium': ( 300, 200 ),
    })
    birth_date = models.DateField( _( "birth date" ), blank = True, null = True  )
    gender = models.CharField( _( "gender" ), max_length = 1, choices = GENDERS, blank = True, null = True, default = None )
    australian_regional_immigration = models.NullBooleanField( _( "Would you be willing to live in Regional Australia" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )
    family_overseas = models.NullBooleanField( _( "Any family members who are citizens in other countries" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )

    # META Options
    class Meta:
        default_permissions = []

    def get_completed_percentage( self ):
        """
        Check how many fields are filled on user_personal tables and get the total percentage of completion

        :return: Int
        """

        fields = [ 'birth_date', 'gender', 'australian_regional_immigration', 'country', 'family_overseas' ]

        total = len( fields )
        completed = 0
        for field in fields:
            value = getattr( self, field )
            if value is not None:
                completed += 1

        return math.floor( ( completed * 100 ) / total )



class UserPersonalFamily( BaseModel ):
    """
    User Personal Family Model - Ex: Stores countries where the user has relatives as citizens
    """

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )

    # META Options
    class Meta:
        default_permissions = []


class UserResult( BaseModel ):
    """
    User Restul Model - Stores the final result score of an user for each country available
    """

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    #user_result_status = models.ForeignKey( 'UserResultStatus', verbose_name = _( 'result status' ) )
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


class UserStats( BaseModel ):
    """
    User Stats Model - Stores the stats about each user (percentage completed, etc)
    """

    # Model Attributes
    user = models.OneToOneField( User, verbose_name = _( 'user' ) )
    percentage_personal = models.IntegerField( _( "percentage personal" ), blank = True, null = True, default = 0 )
    percentage_language = models.IntegerField( _( "percentage language" ), blank = True, null = True, default = 0 )
    percentage_education = models.IntegerField( _( "percentage education" ), blank = True, null = True, default = 0 )
    percentage_work = models.IntegerField( _( "percentage work" ), blank = True, null = True, default = 0 )
    updating_now = models.BooleanField( _( 'updating now' ), default = False )


class UserWork( BaseModel ):
    """
    User Work Model - Ex: Stores work related information
    """

    # Model Attributes
    BOOLEAN_CHOICES = (
        ( True, _( 'Yes' ) ),
        ( False, _( 'No' ) )
    )
    user = models.OneToOneField( User, verbose_name = _( 'user' ) )
    occupation = models.ForeignKey( Occupation, verbose_name = _( 'occupation' ), blank = True, null = True )
    partner_skills = models.NullBooleanField( _( "Do you have a partner/spouse with proved skills" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )
    willing_to_invest = models.NullBooleanField( _( "are you willing to invest money on the country of destination" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )
    canadian_startup_letter = models.NullBooleanField( _( "do you have a startup recommendation letter approved by canada" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )
    australian_professional_year = models.NullBooleanField( _( "Did you complete a Professional Year Course in Australia" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )
    canadian_partner_work_study_experience = models.NullBooleanField( _( "If you have a partner/spouse, has he/she worked or studied in Canada" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )
    work_offer = models.NullBooleanField( _( "Do you have a work offer overseas" ), choices = BOOLEAN_CHOICES, blank = True, null = True, default = None )

    # META Options
    class Meta:
        default_permissions = []

    def get_completed_percentage( self ):
        """
        Check how many fields are filled on user_work tables and get the total percentage of completion

        :return: Int
        """

        # Fields to check for values inserted by user
        fields = [ 'willing_to_invest', 'canadian_startup_letter', 'australian_professional_year', 'canadian_partner_work_study_experience', 'occupation', 'work_offer', 'partner_skills' ]

        # Total is number of fileds + 1 for the UserWorkExperience table
        total = len( fields ) + 1
        completed = 0

        # Check on user_language fields
        for field in fields:
            value = getattr( self, field )
            if value is not None:
                completed += 1

        # Check if there is at least one record on user_language_proficiency
        if self.user.userworkexperience_set.count():
            completed += 1

        return math.floor( ( completed * 100 ) / total )


class UserWorkOffer( BaseModel ):
    """
    User Work Offer Model - Ex: Stores countries where the user has written job offers
    """

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )

    # META Options
    class Meta:
        default_permissions = []


class UserWorkExperience( BaseModel ):
    """
    User Work Experience Model - Ex: Stores each work experience
    """

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    company = models.CharField( _( "company" ), max_length = 100 )
    months = models.PositiveSmallIntegerField( _( "Duration of Employment" ) )

    # META Options
    class Meta:
        default_permissions = []
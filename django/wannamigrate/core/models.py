"""
Core model classes.

These are the models shared by all apps
"""

##########################
# Imports
##########################
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





##########################
# Classes definitions
##########################
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
    points = models.ManyToManyField( 'Country', through = 'points.CountryPoints' )

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
    def get_translated_tuple( **kwargs ):
        """
        Returns a tuple of records ordered by name, after translation.
        It's used on dropdowns on forms

        :return: String
        """
        countries = Country.objects.filter( **kwargs ).order_by( 'name' )
        result = []
        for country in countries:
            result.append( ( country.id, _( country.name ) ) )
        result = sorted( result, key = lambda x: x[1] )
        return tuple( [( '', _( 'Select Country' ) )] + result  )



class Goal( BaseModel ):
    """
    Goal Model - Possible goals that user may have. E.g: "Move permanently to", "Study english in", "Visit..."
    """

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 60 )
    is_active = models.BooleanField( _( "is active" ), default = True )

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
    def get_translated_tuple( **kwargs ):
        """
        Returns a tuple of records ordered by name, after translation.
        It's used on dropdowns on forms
        :return: String
        """
        goals = Goal.objects.filter( **kwargs ).order_by( 'name' )
        result = []
        for goal in goals:
            result.append( ( goal.id, _( goal.name ) ) )
        result = sorted( result, key = lambda x: x[1] )
        return tuple( [( '', _( 'Select Goal' ) )] + result  )





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



class Message( BaseModel ):
    """
    Inbox Messages - Messages between users
    """

    # Model Attributes
    from_user = models.ForeignKey( 'User', related_name = 'message_from_user', verbose_name = _( 'from user' ) )
    to_user = models.ForeignKey( 'User', related_name = 'message_to_user', verbose_name = _( 'to user' ) )
    content = models.TextField( _( "comment" ) )
    is_read = models.BooleanField( _( "is read" ), default = False )

    # META Options
    class Meta:
        default_permissions = []



class Situation( BaseModel ):
    """
    Situation - Stores a migration situation (e.g. "I'm From Brazil and want to study english in Canada")
    """

    # Model Attributes
    from_country = models.ForeignKey( 'Country', verbose_name =  _( "from country" ), related_name = 'visitor_from_country' )
    to_country = models.ForeignKey( 'Country', verbose_name =  _( "to country" ), related_name = 'visitor_to_country' )
    goal = models.ForeignKey( 'Goal', verbose_name =  _( "goal" ) )
    total_users = models.IntegerField( _( "total users" ), default = 1 )
    total_visitors = models.IntegerField( _( "total visitors" ), default = 1 )



class UserManager( BaseUserManager ):
    """
    User Manager - part of custom auth: https://docs.djangoproject.com/en/dev/topics/auth/customizing/
    """

    def create_user( self, email, name = None, password = None ):
        """
        Creates and saves a User with the given email, name and password.

        :param: email
        :param: name
        :param: password
        :return: User Object
        """


        if not email:
            raise ValueError( 'Users must have an email address' )

        user = self.model(
            email = self.normalize_email( email ),
            name = name,
        )

        user.set_password( password )
        user.is_superuser = False
        user.is_admin = False
        user.is_active = True
        user.save( using = self._db )
        return user

    def create_superuser( self, email, password, name = None ):
        """
        Creates and saves a superuser with the given email, name and password.

        :param: email
        :param: password
        :param: name
        :return: User Object
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
    results = models.ManyToManyField( Country, through = 'points.UserResult' )
    preferred_language = models.CharField( _( "Language" ), max_length = 6, choices = LANGUAGES, default = 'en' )
    preferred_timezone = models.CharField( _( "Timezone" ), max_length = 100, null = True, blank = True )

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
        """ Return the user's full name """
        # The user is identified by their email address
        return self.name if self.name else self.email


    def get_short_name( self ):
        """ Return the user's short name """
        # The user is identified by their email address
        return self.email


    def __str__( self ):
        return self.email


    @property
    def is_staff( self ):
        """Is the user a member of staff?"""
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
    partner_education_level_answer = models.ForeignKey( 'points.Answer', related_name = 'partner_education_level_answer', verbose_name = _( 'partner/spouse education level' ), blank = True, null = True )

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
    education_level_answer = models.ForeignKey( 'points.Answer', related_name = 'education_level', verbose_name = _( 'education level' ) )
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
    partner_english_level_answer = models.ForeignKey( 'points.Answer', related_name = 'partner_english_level_answer', verbose_name = _( 'partner/spouse english level' ), on_delete = models.PROTECT, blank = True, null = True  )
    partner_french_level_answer = models.ForeignKey( 'points.Answer', related_name = 'partner_french_level_answer', verbose_name = _( 'partner/spouse french level' ), on_delete = models.PROTECT, blank = True, null = True  )

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
    language_level_answer = models.ForeignKey( 'points.Answer', verbose_name = _( 'language level' ), on_delete = models.PROTECT )

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
        'size100x100': ( 100, 100, True ),
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



class UserSituation( BaseModel ):
    """
    User Situation - Stores the immigration situation of an specific user (e.g. "I'm From Brazil and want to study english in Canada")
    """

    # Model Attributes
    user = models.OneToOneField( User, verbose_name = _( 'user' ) )
    situation = models.ForeignKey( 'Situation', verbose_name =  _( "situation" ) )



class UserStats( BaseModel ):
    """
    User Stats Model - Stores the stats about each user (percentage completed, etc)
    """

    # Model Attributes
    user = models.OneToOneField( User, verbose_name = _( 'user' ), related_name = "userstats" )
    percentage_personal = models.IntegerField( _( "percentage personal" ), blank = True, null = True, default = 0 )
    percentage_language = models.IntegerField( _( "percentage language" ), blank = True, null = True, default = 0 )
    percentage_education = models.IntegerField( _( "percentage education" ), blank = True, null = True, default = 0 )
    percentage_work = models.IntegerField( _( "percentage work" ), blank = True, null = True, default = 0 )
    updating_now = models.BooleanField( _( 'updating now' ), default = False )
    total_answers = models.IntegerField( _( "total answers" ), blank = True, null = True, default = 0 )
    total_questions = models.IntegerField( _( "total questions" ), blank = True, null = True, default = 0 )
    total_profile_views = models.IntegerField( _( "total profile views" ), blank = True, null = True, default = 0 )
    total_contracts = models.IntegerField( _( "total contracts" ), blank = True, null = True, default = 0 )
    total_reviews = models.IntegerField( _( "total reviews" ), blank = True, null = True, default = 0 )
    total_topics_following = models.IntegerField( _( "total topics following" ), blank = True, null = True, default = 0 )
    total_posts_following = models.IntegerField( _( "total posts following" ), blank = True, null = True, default = 0 )
    total_users_following = models.IntegerField( _( "total users following" ), blank = True, null = True, default = 0 )
    total_users_followers = models.IntegerField( _( "total users followers" ), blank = True, null = True, default = 0 )





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
    occupation = models.ForeignKey( 'points.Occupation', verbose_name = _( 'occupation' ), blank = True, null = True )
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
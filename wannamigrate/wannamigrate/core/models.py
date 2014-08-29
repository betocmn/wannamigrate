from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Group
)
from django.utils.translation import ugettext_lazy as _

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

    # Model Attributes
    question = models.ForeignKey( 'Question', verbose_name = _( 'question' ) )
    description = models.CharField(  _( 'description' ), max_length = 255 )


class Country( BaseModel ):
    """
    Country Model - ex: Brazil, Australia, USA, etc.
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 100 )
    continent = models.CharField( _( "continent" ), max_length = 30 )
    code = models.CharField( _( "code" ), max_length = 2 )

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
    
class Language( BaseModel ):
    """
    Language Model - Ex: english, french, portuguese, etc.
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    name = models.CharField( _( "name" ), max_length = 15 )
    code = models.CharField( _( "code" ), max_length = 5 )

class Question( BaseModel ):
    """
    Question Model - Question is a requirement asked for the immigration candidate
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    description = models.CharField( _( "description" ), max_length = 255 )
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

    # On Python 3: def __str__(self):
    def __unicode__( self ):
        return self.email

    @property
    def is_staff( self ):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class UserEducation( BaseModel ):
    """
    User Education Model - Ex: Stores each education achieved (ex: bachelors, in brazil, universidade UFMA, from 2003-2007
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    education_level_answer = models.ForeignKey( Answer, related_name = 'education_level', verbose_name = _( 'education level' ) )
    education_field_answer = models.ForeignKey( Answer, related_name = 'education_field', verbose_name = _( 'education field' ) )
    school = models.CharField( _( "school" ), max_length = 100 )
    year_start = models.CharField( _( "start year" ), max_length = 4 )
    year_end = models.CharField( _( "end year" ), max_length = 4 )

class UserLanguage( BaseModel ):
    """
    User Language Model - Ex: Stores each language and level the user can speak
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    user = models.ForeignKey( User, verbose_name = _( 'user' ) )
    language = models.ForeignKey( Language, verbose_name = _( 'language' ) )
    language_level_answer = models.ForeignKey( Answer, verbose_name = _( 'language level' ) )

class UserPersonal( BaseModel ):
    """
    User Personal Model - Ex: Stores personal information from the user, such as age, gender, etc..
    """

    # META Options
    class Meta:
        default_permissions = []

    # Model Attributes
    GENDERS = (
        ( 'F', 'Femanle' ),
        ( 'M', 'Male' ),
    )
    user = models.OneToOneField( User, verbose_name = _( 'user' ) )
    country = models.ForeignKey( Country, verbose_name = _( 'country' ) )
    birth_date = models.DateField( _( "birth date" ) )
    gender = models.CharField( _( "gender" ), max_length = 1, choices = GENDERS )

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
    score = models.IntegerField( _( "score" ))

class UserWork( BaseModel ):
    """
    User Work Model - Ex: Stores each work experience
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
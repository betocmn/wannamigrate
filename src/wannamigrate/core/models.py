"""
Core model classes.

These are the models shared by all apps
"""

##########################
# Imports
##########################
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.template.defaultfilters import slugify
import itertools
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


##########################
# Classes definitions
##########################
class BaseModel(models.Model):
    """
    BASE MODEL - The father of all :)
    """

    # Base Model Attributes (fields to be used on all models)
    created_date = models.DateTimeField(_('created date'), auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(_('modified date'), auto_now=True, auto_now_add=False)

    # META Options
    class Meta:
        abstract = True

    # Method Definitions
    @classmethod
    def get_presentation_fields(cls, mode='fieldsets'):
        """
        Returns the model fields for forms and view pages as either a list or dictionary.

        The response will vary accordingly to the mode:

            raw - A raw list with fields to be used in the form
            fieldsets - A dictionary for displaying data in forms

        :param: mode - either 'raw', 'fieldsets'
        :return: Mixed
        """
        fieldsets = cls.fieldsets
        if mode == 'raw':
            fields = []
            for fieldset in fieldsets:
                fields.extend(fieldset['fields'])
            return fields

        elif mode == 'fieldsets':
            return fieldsets

        return False

    def get_display_fields(self):
        """
        Returns all fields for display in crud 'view' pages.

        It includes both the form data + all other excluded atts, excepted internal timestamps

        :return: Mixed
        """

        fieldsets = self.get_presentation_fields('fieldsets')
        fieldsets_new = []
        for fieldset in fieldsets:
            temp = {'title': fieldset['title'], 'fields': []}
            for field in fieldset['fields']:
                value = getattr(self, field, None)
                if isinstance(value, models.manager.Manager):
                    new = []
                    for item in value.all():
                        new.append(str(item))
                    value = " / ".join(new)

                temp['fields'].append({
                    'name': field,
                    'label': self._meta.get_field(field).verbose_name.capitalize(),
                    'value': value
                })
            fieldsets_new.append(temp)
        return fieldsets_new


class Continent(BaseModel):
    """
    Continent Model - e.g. Oceania, Europe, etc.
    """

    # Model Attributes
    name = models.CharField(_("name"), max_length=100)

    # META Options
    class Meta:
        default_permissions = []

    # Method definitions
    def __str__(self):
        return '%s' % (_(self.name))


class Country(BaseModel):
    """
    Country Model - e.g. Brazil, Australia, USA, etc.
    """

    # Model Attributes
    name = models.CharField(_("name"), max_length=100)
    continent = models.ForeignKey('Continent', verbose_name=_("continent"))
    code = models.CharField(_("code"), max_length=2)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    # META Options
    class Meta:
        default_permissions = []
        ordering = ['name']

    # Method definitions
    def __str__(self):
        """
        String representation of this model
        :return: String
        """
        return '%s' % (_(self.name))

    @staticmethod
    def get_translated_tuple(**kwargs):
        """
        Returns a tuple of records ordered by name, after translation.
        It's used on dropdowns on forms

        :return: String
        """
        countries = Country.objects.filter(**kwargs).order_by('name')
        result = []
        for country in countries:
            result.append((country.id, _(country.name)))
        result = sorted(result, key=lambda x: x[1])
        return tuple([('', _('Select Country'))] + result)


class Language(BaseModel):
    """
    Language Model - Ex: english, french, portuguese, etc.
    """

    # Model Attributes
    name = models.CharField(_("name"), max_length=25)
    code = models.CharField(_("code"), max_length=6)

    # META Options
    class Meta:
        default_permissions = []

    # Method definitions
    def __str__(self):
        return '%s' % (_(self.name))

    @staticmethod
    def get_translated_tuple():
        """
        Returns a tuple of records ordered by name, after translation.
        It's used on dropdowns on forms
        :return: String
        """
        languages = Language.objects.order_by('name')
        result = []
        for language in languages:
            result.append((language.id, language.name))
        result = sorted(result, key = lambda x: x[1])
        return tuple([('', _('Select Language'))] + result )


class UserManager(BaseUserManager):
    """
    User Manager - part of custom auth
    """

    def create_user(self, email, password=None, first_name=None, last_name=None,
                    facebook_id=None, language='en', timezone='Australia/Sydney'):
        """
        Creates and saves a User with the given email, name and password.

        :param: email
        :param: name
        :param: password
        :return: User Object
        """

        # Validates and identifies user
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email), first_name=first_name, last_name=last_name
        )

        # If no password was given, generate a random one
        has_updated_password = True
        if not password:
            password = self.make_random_password()
            has_updated_password = False

        # inserts user
        user.set_password(password)
        user.facebook_id = facebook_id
        user.preferred_language = language
        user.preferred_timezone = timezone
        user.has_updated_password = has_updated_password
        user.is_superuser = False
        user.is_admin = False
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name=None, last_name=None):
        """
        Creates and saves a superuser with the given email, name and password.

        :param: email
        :param: password
        :param: name
        :return: User Object
        """

        user = self.create_user(email, password=password, fist_name=first_name, last_name=last_name)
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    User Model
    """

    # Model Attributes (db fields)
    email = models.EmailField(_("e-mail"), max_length=255, unique=True)
    first_name = models.CharField(_("first name"), max_length=60, null=True, blank=True)
    last_name = models.CharField(_("last name"), max_length=60, null=True, blank=True)
    facebook_id = models.BigIntegerField(_("facebook id"), null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_active = models.BooleanField(_("is active"), default=True)
    is_admin = models.BooleanField(_("is admin"), default=False)
    has_updated_password = models.BooleanField(_("has updated password"), default=True)
    preferred_language = models.CharField(
        _("preferred language"), max_length=6, choices=settings.LANGUAGES, default='en'
    )
    preferred_timezone = models.CharField(
        _("timezone"), max_length=100, choices=settings.TIMEZONES, null=True, blank=True
    )

    # Fields organised for crud operations
    fieldsets = [
        {
            'title': 'Account Settings',
            'fields': [
                'first_name', 'last_name', 'email', 'password', 'is_active', 'is_admin',
                'is_superuser', 'preferred_language', 'preferred_timezone', 'slug', 'groups'
            ]
        }
    ]

    # META Options
    class Meta:
        default_permissions = []
        permissions = (
            ("admin_add_admin_user", "ADMIN: Can add admin user"),
            ("admin_change_admin_user", "ADMIN: Can change admin user"),
            ("admin_delete_admin_user", "ADMIN: Can delete admin user"),
            ("admin_view_admin_user", "ADMIN: Can view admin users")
        )

    # Manager
    objects = UserManager()

    # Name of field that should be used as username
    USERNAME_FIELD = 'email'

    # Method definitions
    def get_full_name(self):
        """ Return the user's full name """
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        return None

    def get_short_name(self):
        """ Return the user's short name """
        return self.first_name

    def __str__(self):
        full_name = self.get_full_name()
        if full_name:
            return full_name
        return self.email

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

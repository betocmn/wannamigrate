"""
CORE FORMS

Here you can include base forms that will be used as parents of application
forms.

Also you can create custom form fields or methods

"""

##########################
# Imports
##########################
from django import forms
from wannamigrate.core.models import Country, Language
from django.forms import ModelChoiceField





##########################
# Class definitions
##########################
class _BaseForm( object ):
    """
    The BASE form.  All forms in the system should extend this class
    """

    def get_required_fields( self, compare_with_html_id = True ):
        """
        Creates a Comma separated list of required fields
        :return: String
        """
        required_fields = []
        for field in self.fields:
            if self.fields[field].required and 'password' not in field:
                if compare_with_html_id:
                    field = 'id_' + field
                required_fields.append( field )

        return ','.join( required_fields )



class BaseModelForm( _BaseForm, forms.ModelForm ):
    """
    Making the Base Model Form use our _BaseForm
    """
    pass



class BaseForm( _BaseForm, forms.Form ):
    """
    Making the Base Form use our _BaseForm
    """
    pass



class CountryChoiceField( ModelChoiceField ):
    """
    Custom Model for countries, to get translation
    """

    choices = Country.get_translated_tuple()



class LanguageChoiceField( ModelChoiceField ):
    """
    Custom Model for languages, to get translation
    """

    choices = Language.get_translated_tuple()
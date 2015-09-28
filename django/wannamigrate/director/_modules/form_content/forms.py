from django import forms
from django.utils.translation import ugettext_lazy as _

class GenericForm( forms.Form ):

    choice = forms.ChoiceField( widget=forms.RadioSelect )

    def __init__( self, *args, **kwargs):
        choices = kwargs.pop( "choices" )
        super( GenericForm, self ).__init__( *args, **kwargs )

        # Translates all the form choices
        translated_choices = []
        for k,v in choices:
            translated_choices.append( ( k, _(v) ) )

        self.fields["choice"].choices = translated_choices

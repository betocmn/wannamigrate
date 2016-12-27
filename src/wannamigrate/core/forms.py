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
from django.forms import ModelChoiceField, ModelMultipleChoiceField


##########################
# Base Forms
##########################
class _BaseForm(object):
    """
    The BASE form.  All forms in the system should extend this class
    """

    def get_required_fields(self, compare_with_html_id=True):
        """
        Creates a Comma separated list of required fields
        :return: String
        """
        required_fields = []
        for field in self.fields:
            if self.fields[field].required and 'password' not in field:
                if compare_with_html_id:
                    field = 'id_' + field
                required_fields.append(field)

        return ','.join(required_fields)


class BaseModelForm(_BaseForm, forms.ModelForm):
    """
    Making the Base Model Form use our _BaseForm
    """

    def get_fieldsets(self):
        """
        Returns a dictionary of fields organized by groups based on the model fieldsets attribute

        :return: Dictionary
        """
        if not hasattr(self.instance, 'get_presentation_fields'):
            fieldsets = {'title': 'Form Data', 'fields': []}
            for field in self:
                fieldsets['fields'].append(field.name)
            return [fieldsets, ]

        return self.instance.get_presentation_fields('fieldsets')


class BaseForm(_BaseForm, forms.Form):
    """
    Making the Base Form use our _BaseForm
    """
    pass


##########################
# Base Fields
##########################
class ModelChoiceFlexibleField(ModelChoiceField):
    """
    Custom Model field with the flexibility to accept and insert new values
    """

    def __init__(self, model, *args, **kwargs):
        self.model = model
        super(ModelChoiceFlexibleField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ModelChoiceFlexibleField, self).deconstruct()
        kwargs['model'] = self.model
        return name, path, args, kwargs

    def to_python(self, value):

        if value and isinstance(value, str):
            obj = None
            if value.isdigit():
                try:
                    obj = self.model.objects.get(pk=int(value))
                except self.model.DoesNotExist:
                    pass
            if not obj:
                try:
                    obj = self.model.objects.get(name=value)
                except self.model.DoesNotExist:
                    obj = self.model()
                    obj.name = value
                    obj.save()
            value = obj
        return value


class ModelMultipleChoiceFlexibleField(ModelMultipleChoiceField):
    """
    Custom Model field with the flexibility to accept and insert new values
    """

    def __init__(self, model, *args, **kwargs):
        self.model = model
        super(ModelMultipleChoiceFlexibleField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ModelMultipleChoiceFlexibleField, self).deconstruct()
        kwargs['model'] = self.model
        return name, path, args, kwargs

    """
    def to_python(self, value):

        if not value:
            return []
        if value:
            values = []
            for single in value:
                if single and isinstance(single, str):
                    obj = None
                    if single.isdigit():
                        try:
                            obj = self.model.objects.get(pk=int(single))
                        except self.model.DoesNotExist:
                            pass
                    if not obj:
                        try:
                            obj = self.model.objects.get(name=single)
                        except self.model.DoesNotExist:
                            obj = self.model()
                            obj.name = single
                            obj.save()
                    values.append(obj.id)
                else:
                    values.append(int(single))
        return super(ModelMultipleChoiceFlexibleField, self).to_python(values)

    """
    def clean(self, value):
        if value:
            values = []
            for single in value:
                if single and isinstance(single, str):
                    obj = None
                    if single.isdigit():
                        try:
                            obj = self.model.objects.get(pk=int(single))
                        except self.model.DoesNotExist:
                            pass
                        aviao = obj
                    if not obj:
                        try:
                            obj = self.model.objects.get(name=single)
                        except self.model.DoesNotExist:
                            obj = self.model()
                            obj.name = single
                            last = obj
                            last_id = obj.id
                            last_name = obj.name
                            obj.save()
                    values.append(obj.id)
                else:
                    values.append(int(single))
            value = values
        return super(ModelMultipleChoiceFlexibleField, self).clean(value)

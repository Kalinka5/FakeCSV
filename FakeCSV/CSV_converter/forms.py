from django import forms

from .models import Schema


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ['schema_name', 'column_separator', 'string_character']

    def save(self, commit=True):
        schema = super(SchemaForm, self).save(commit=False)
        if commit:
            schema.save()
        return schema

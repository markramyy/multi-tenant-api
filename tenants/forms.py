from django import forms
from .models import Tenant, Domain
from django.core.exceptions import ValidationError

class TenantForm(forms.ModelForm):
    schema_name = forms.CharField()

    class Meta:
        model = Tenant
        fields = ['name', 'schema_name']

    def clean_schema_name(self):
        schema_name = self.cleaned_data['schema_name']
        if not schema_name.isidentifier():
            raise ValidationError('Enter a valid schema name')
        return schema_name

class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ['domain', 'is_primary']

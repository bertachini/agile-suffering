from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'whatsapp', 'facebook']

class LeadFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by name or email...'
        })
    ) 
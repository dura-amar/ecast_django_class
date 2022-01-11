from django import forms
from django.forms import fields
from .models import Destination, District

class destForm(forms.ModelForm):
    class Meta:
        model=Destination
        fields='__all__'

class distForm(forms.ModelForm):
    class Meta:
        model=District
        fields='__all__'

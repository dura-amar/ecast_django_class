from django import forms
from django.forms import fields
from .models import Destination

class destForm(forms.ModelForm):
    class Meta:
        model=Destination
        fields='__all__'
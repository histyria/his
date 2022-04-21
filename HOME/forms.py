from django import forms
from .models import *
from django.forms.widgets import NumberInput
from django.contrib.admin.widgets import AutocompleteSelect

class patiant_fileForm(forms.ModelForm):

   
    class Meta:
        model = patient_file
        fields = '__all__'

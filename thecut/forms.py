from django import forms
from .models import *

class CarForm(forms.ModelForm):
    class Meta:
        fields = ['car_model', 'manufacturer']
        model = Car

class ManufacturerForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'description']
        model = Manufacturer
from django import forms

from application.models import *

class RealEstateForm(forms.ModelForm):

    class Meta:
        model = RealEstate
        fields = '__all__'
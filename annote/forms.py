from django import forms
from .models import AnnoteModel

class AnnoteFileForm(forms.ModelForm):
    class Meta:
        model = AnnoteModel
        fields = ('image','LisenceNumber','company','carmodel','coordinates',)
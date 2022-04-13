from django import forms
from .models import *
  
class ImageForm(forms.ModelForm):
  
    class Meta:
        model = profileImage
        fields = ['name', 'imageFile']
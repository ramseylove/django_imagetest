from django import forms
from .models import Image

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['media_image']
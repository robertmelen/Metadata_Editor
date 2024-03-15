from django import forms
from .models import Uploaded_Image

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Uploaded_Image
        fields = ['image']
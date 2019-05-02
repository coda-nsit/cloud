from django import forms

class UploadForm(forms.Form):
    name       = forms.CharField(label='Your name', max_length=100)
    location   = forms.CharField(label='Location', max_length=100)
    address    = forms.CharField(label='address', max_length=100)
    photo      = forms.ImageField()   
    photo_name = forms.CharField(label="photo name", max_length=100)
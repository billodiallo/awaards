from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,10)]

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude =['posted_by','profile']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        design= forms.IntegerField(label="Design Rating")
        usability = forms.IntegerField(label="Usability Rating")
        content = forms.IntegerField(label="Content Rating")
        widget=forms.Select(choices=INTEGER_CHOICES)
        exclude =['project','juror']

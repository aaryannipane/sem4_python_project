from attr import field
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from . import models

# this is model form use to make form from model(database table)
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = models.Enquiry
        fields = ('name', 'email', 'detail')
        
class SignUp(UserCreationForm): 
    class meta:
        model=User
        fields = ['username', 'email','password1','password2']

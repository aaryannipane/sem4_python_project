from attr import field
from django import forms
from . import models

# this is model form use to make form from model(database table)
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = models.Enquiry
        fields = ('name', 'email', 'detail')
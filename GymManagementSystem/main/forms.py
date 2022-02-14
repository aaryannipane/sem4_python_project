from attr import field
from django import forms
from . import models

# nhi samja
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = models.Enquiry
        fields = ('name', 'email', 'detail')
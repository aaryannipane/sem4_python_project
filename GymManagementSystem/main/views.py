from django import forms
from django.shortcuts import render
import service_identity
from . import models
from . import forms

# Create your views here.
def home(request):
    banners = models.Banners.objects.all()
    # to fetch only three row
    services = models.Service.objects.all()[:3]
    return render(request, 'home.html', {'banners': banners, 'services':services})


# view with get method
def page_detail(req, id):
    page = models.Page.objects.get(id=id)
    return render(req, 'page.html', {'page':page})

# faq page
def faq(req):
    faq = models.Faq.objects.all()
    return render(req, 'faq.html', {'faqs':faq})

# Enquiry form page
def enquiry(req):
    # nhi samja
    msg = ''
    if req.method == 'POST':
        form = forms.EnquiryForm(req.POST)
        if form.is_valid:
            form.save()
            msg = 'data has been saved'

    form = forms.EnquiryForm
    print(form)
    return render(req, 'enquiry.html', {'form':form, 'msg':msg})


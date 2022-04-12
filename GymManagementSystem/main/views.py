from contextlib import nullcontext
from gettext import NullTranslations
from django import forms
from django.shortcuts import render
from pkg_resources import NullProvider
import service_identity
from . import models
from . import forms
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    banners = models.Banners.objects.all()
    # to fetch only three row
    services = models.Service.objects.all()[:3]
    galleryImages = models.GalleryImage.objects.all().order_by('-id')[:9]
    return render(request, 'home.html', {'banners': banners, 'services':services, 'gallery': galleryImages})


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
    # handling post method from form 
    msg = ''
    if req.method == 'POST':
        form = forms.EnquiryForm(req.POST)
        if form.is_valid:
            form.save()
            msg = 'data has been saved'

    form = forms.EnquiryForm
    return render(req, 'enquiry.html', {'form':form, 'msg':msg})

# show galleries
def gallery(req):
    gallery = models.Gallery.objects.all().order_by('-id')
    return render(req, 'gallery.html', {'galleries':gallery})

# show galleries detail
def gallery_detail(req, id):
    # fetch title of gallery with their id
    gallery = models.Gallery.objects.get(id=id)
    # get only object containing that gallery in decending order
    galleryImages = models.GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    return render(req, 'gallery_images.html', {'galleryImages':galleryImages, 'gallery':gallery})


# subscription plan
def pricing(req):
    plan = models.SubPlan.objects.all().order_by('price')
    dfeature = models.SubPlanFeature.objects.all()
    return render(req, 'pricing.html', {'plans':plan, 'dfeature':dfeature})

# Signup 
def signup(request):
    msg=None      
    if request.method=='POST':
       form=forms.SignUp(request.POST)
       if form.is_valid():
           form.save()
           msg='thank you for register.'

    form=forms.SignUp
    return render(request,'registration/signup.html', {'form':form,'msg':msg})

# Checkout 
def checkout(request,plan_id):
    planDetail = models.SubPlan.objects.get(pk=plan_id)
    return render(request, 'checkout.html', {'plan':planDetail})

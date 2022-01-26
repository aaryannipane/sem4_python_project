from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    banners = models.Banners.objects.all()
    return render(request, 'home.html', {'banners': banners})

from turtle import title
from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
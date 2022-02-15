from distutils.command.upload import upload
from turtle import title
from django.db import models
from django.utils.html import mark_safe


# Create your models here.

# banner table to store image and alt_text for image
class Banners(models.Model):
    img = models.ImageField(upload_to='banners/')
    alt_text = models.CharField(max_length=150)

    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))


# service table to store title, detail and image
class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to='service/', null=True)
    
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))


# pages
class Page(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()

    def __str__(self):
        return self.title

# faq
class Faq(models.Model):
    question = models.TextField()
    ans = models.TextField()

    def __str__(self):
        return self.question

# Enquiry
class Enquiry(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    detail = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)

    # default column in admin page to show object
    def __str__(self):
        return self.name


# Gallery model 
class Gallery(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to="gallery/", null=True)

    def __str__(self) -> str:
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))

# GalleryImage model 
class GalleryImage(models.Model):
    # foreign key 
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    alt_text = models.CharField(max_length=150)
    img = models.ImageField(upload_to="gallery_img/", null=True)

    def __str__(self) -> str:
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))


# subscription plan model
class SubPlan(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return self.title

# subscription features in plan
class SubPlanFeature(models.Model):
    subplan = models.ForeignKey(SubPlan, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title
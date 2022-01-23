from django.contrib import admin
from . import models

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_text', 'image_tag')

admin.site.register(models.Banners, BannerAdmin)
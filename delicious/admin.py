from django.contrib import admin
from . models import sliderModel,ContactModel,BlogPost,BlogCategory
# Register your models here.
admin.site.register(sliderModel)
admin.site.register(ContactModel)
admin.site.register(BlogPost)
admin.site.register(BlogCategory)
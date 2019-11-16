from django.contrib import admin
from .models import User, Image, Tag, Image2tag

# Register your models here.
admin.site.register(User)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Image2tag)
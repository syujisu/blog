from django.contrib import admin
from .models import Blog
from .models import Pictures

admin.site.register(Pictures)
admin.site.register(Blog)

# Register your models here.

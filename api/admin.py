from django.contrib import admin
from .models import Category, Job, Resume

admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Resume)
from django.contrib import admin
from .models import Reviews, Profile, Project
# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Reviews)

# admin.py
from django.contrib import admin
from .models import Roadmap, Course

admin.site.register(Roadmap)
admin.site.register(Course)

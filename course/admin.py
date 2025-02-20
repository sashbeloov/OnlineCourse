from django.contrib import admin

from .models import Course, Subject

admin.site.register(Subject)
admin.site.register(Course)
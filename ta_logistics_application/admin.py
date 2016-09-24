from django.contrib import admin
from .models import Applications, OpenClasses

class ApplicationsInline(admin.TabularInline):
    model = Applications

class OpenClassesAdmin(admin.ModelAdmin):
    model = OpenClasses

admin.site.register(OpenClasses, OpenClassesAdmin)

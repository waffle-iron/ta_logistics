from django.contrib import admin
from .models import Application, OpenClass

#class ApplicationAdmin(admin.ModelAdmin):
    #model = Application

#class OpenClassAdmin(admin.ModelAdmin):
    #model = OpenClass

admin.site.register(OpenClass)
admin.site.register(Application)
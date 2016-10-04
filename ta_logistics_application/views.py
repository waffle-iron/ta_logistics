from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

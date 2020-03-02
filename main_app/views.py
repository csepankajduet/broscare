from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name='main_app_templates/index.html'



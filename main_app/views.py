from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name='main_app_templates/index.html'

class About(TemplateView):
    template_name='main_app_templates/about.html'    

class Doctors(TemplateView):
    template_name='main_app_templates/doctor.html' 

class Services(TemplateView):
    template_name='main_app_templates/services.html'     

class Reviews(TemplateView):
    template_name='main_app_templates/review.html'  

class Contact(TemplateView):
    template_name='main_app_templates/contact.html'      
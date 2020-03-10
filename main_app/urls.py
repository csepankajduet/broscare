from django.urls import path
from . import views
urlpatterns = [
    path('home', views.Home.as_view(), name='home'),
    path('about', views.About.as_view(), name='about'),
    path('doctor', views.Doctors.as_view(), name='doctor'),
    path('services', views.Services.as_view(), name='services'),
    path('review', views.Reviews.as_view(), name='review'),
    path('contact', views.Contact.as_view(), name='contact'),
]

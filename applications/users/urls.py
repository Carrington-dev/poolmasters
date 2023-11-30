from django.contrib import admin
from django.urls import path, include
from applications.users import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    # path('contact', views.contact, name="contact"),
    path('testimony', views.testimony, name="testimony"),
    path('portfolio', views.portfolio, name="portfolio"),
]

from django.urls import path
from applications.book import views


urlpatterns = [
    path('', views.contact, name='contact'),
    path('subscribe', views.subscribe, name='subscribe'),
]
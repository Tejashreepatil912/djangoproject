from django.contrib import admin
from django.urls import path ,include
from biryani import views
urlpatterns = [
    path("", views.home),
    path("home/",views.home),
    path('index/',views.index),
    path('about/',views.about),
    path('services/',views.services),
    path('contact/',views.contact, name='contact'),
]
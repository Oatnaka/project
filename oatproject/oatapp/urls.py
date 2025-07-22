from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = {
    path('', views.index, name='name'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('form', views.form, name='form'),
    path('person', views.person, name='person'),
}
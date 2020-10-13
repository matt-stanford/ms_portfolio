from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.my_courses, name='my_courses'),
    path('contact', views.contact, name='contact'),
]
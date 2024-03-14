# person/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_person, name='add_person'),
    path('', views.all_people, name='all_people'),
]

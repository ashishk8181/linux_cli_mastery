from django.urls import path
from . import views

urlpatterns = [
    path('terminal/', views.terminal, name='terminal'),
]

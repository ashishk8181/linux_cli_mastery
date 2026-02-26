from django.urls import path
from . import views

urlpatterns = [
    path('', views.module_list, name='module_list'),
    path('complete/<int:lesson_id>/', views.mark_complete, name='mark_complete'),
    path('<slug:module_slug>/<slug:lesson_slug>/', views.lesson_detail, name='lesson_detail'),
]

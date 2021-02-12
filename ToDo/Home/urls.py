from django.contrib import admin
from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>/remove/', views.delete_task, name="delete_task"),
    path('delete/remove/', views.delete_all, name="delete_all"),
]

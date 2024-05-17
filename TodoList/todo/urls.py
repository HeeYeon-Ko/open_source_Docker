from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('complete_todo/<int:pk>/', views.complete_todo, name='complete_todo'),
]


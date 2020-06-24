from django.urls import path
from . import views


app_name = 'note_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_note, name='add_note'),
    path('update/<str:pk>/', views.update_note, name='update_note'),
    path('delete/<str:pk>/', views.delete_note, name='delete_note'),
]

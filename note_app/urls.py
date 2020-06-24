from django.urls import path
from . import views


app_name = 'note_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_note, name='add_note'),
]

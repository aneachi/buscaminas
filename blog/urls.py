from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='crea_tablero'),
]
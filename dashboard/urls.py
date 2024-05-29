from django.urls import path
from . import views

urlpatterns = [
    path('', views.Seleccionar, name="Seleccionar"),
]
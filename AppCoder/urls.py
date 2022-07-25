
from django.urls import path, include
from AppCoder.views import *
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path("disciplinasDeportivas/", views.disciplinasDeportivas, name='disciplinasDeportivas'),
    path("Profesores/", views.profesores, name='profesores'),
    path("Alumnos/", views.alumnos, name='alumnos'),
    path('inscripcion_deporte/', views.inscripcion_deporte, name='inscripcion'),
    path('busqueda_deporte/', views.busqueda_deporte, name='busqueda_deporte'),
    #path("base/", base),
    
]
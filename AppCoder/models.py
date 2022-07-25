from django.db import models

class Inicio(models.Model):
    donde = models.CharField(max_length=30)

class DisiplinasDeportivas(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField("Precio $")

class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    deporte = models.CharField(max_length=30)

class Alumnos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    deporte = models.CharField(max_length=30)

    
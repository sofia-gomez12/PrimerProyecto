from django.contrib import admin

from .models import *


class DisiplinasDeportivasAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")
    search_fields = ("nombre", "precio")
    

class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "deporte")
    search_fields = ("nombre", "apellido", "deporte")
    

class AlumnosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "edad", "deporte")
    search_fields = ("nombre", "apellido", "edad", "deporte")
       

admin.site.register(DisiplinasDeportivas, DisiplinasDeportivasAdmin)
admin.site.register(Profesores, ProfesoresAdmin)
admin.site.register(Alumnos, AlumnosAdmin)
from django.contrib import admin
from .models import Profesor, Entregable, Estudiante, Curso

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Estudiante)
admin.site.register(Curso)

from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)

class TareaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "estado", "prioridad")  # columnas visibles en la lista
    list_filter = ("estado", "prioridad")             # filtros laterales
    search_fields = ("titulo", "descripcion")         # búsqueda rápida
    filter_horizontal = ("usuarios",)                 # selector múltiple mejorado

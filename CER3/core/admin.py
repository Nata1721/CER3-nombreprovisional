from django.contrib import admin
from .models import Evento
# Register your models here.

class datos_evento(admin.ModelAdmin):
    list_display = ("titulo", "descripcion", "tipo", "segmento", "fechaInicio", "fechaTermino")
    list_filter = ("fechaInicio", "fechaTermino", )

admin.site.register(Evento, datos_evento)


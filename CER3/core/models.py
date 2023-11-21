from django.db import models

# Create your models here.

class Evento(models.Model):
    TIPO = [
        ("Vacaciones"),
        ("Feriado"),
        ("Suspensión de actividades"),
        ("Suspensión de actividades PM"),
        ("Periodo Lectivo"),
        ("Suspensión de evaluaciones"),
        ("Ceremonia"),
        ("EDDA"),
        ("Evaluación"),
        ("Ayudantías"),
        ("Hito Académico"),
        ("Secretaría Académica"),
        ("OAI"),
    ]

    SEGMENTO = [
        ("Comunidad USM"),
        ("Estudiante"),
        ("Profesor"),
        ("Jefe de Carrera"),
    ]

    fechaInicio = models.DateTimeField(auto_now_add=False)
    fechaTermino = models.DateTimeField(auto_now_add=False)
    titulo = models.CharField(max_length=55)
    descripcion = models.CharField(max_length=100)
    tipo = TIPO
    segmento = SEGMENTO

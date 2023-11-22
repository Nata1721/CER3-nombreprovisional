from django.db import models

# Create your models here.

class Evento(models.Model):
    TIPO_CHOICES = [
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

    SEGMENTO_CHOICES = [
        ("Comunidad USM"),
        ("Estudiante"),
        ("Profesor"),
        ("Jefe de Carrera"),
    ]

    fechaInicio = models.DateTimeField(auto_now_add=False)
    fechaTermino = models.DateTimeField(auto_now_add=False)
    titulo = models.CharField(max_length=55)
    descripcion = models.CharField(max_length=100)
    tipo =  models.CharField(max_length=1, choices=TIPO_CHOICES)
    segmento =  models.CharField(max_length=1, choices=SEGMENTO_CHOICES)

    def __str__(self):
        return self.titulo
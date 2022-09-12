from django.db import models


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    apellido = models.CharField("Apellido", max_length=100)
    activo = models.BooleanField("Esta Activo", default=True)
    fecha_nacimiento = models.DateField()
from django.db import models


class Persona(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    edad = models.IntegerField("Edad")
    apellido = models.CharField("Apellido", max_length=100)
    activo = models.BooleanField("Esta Activo", default=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField("Direción", max_length=100, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
